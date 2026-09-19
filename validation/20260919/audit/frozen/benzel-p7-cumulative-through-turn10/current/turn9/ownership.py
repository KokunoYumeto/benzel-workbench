"""Exact affine source maps and finite Farkas certificates of their domains.

Vectors are (m,k,i,j,constant); inequalities mean vector dot (m,k,i,j,1)>=0.
No optimization package is used to verify a certificate.
"""
from pathlib import Path
from fractions import Fraction
import json,sys,itertools,hashlib
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'turn8'))
import geometry as G,families
from source_table import ROWS
Z=(0,0,0,0,0)
def v(a=0):return(0,0,0,0,a)if type(a)is int else tuple(a)
def add(a,b):return tuple(x+y for x,y in zip(v(a),v(b)))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(v(b)))
def scale(a,n):return tuple(n*x for x in a)
def aff(a,slot=2):return (a[0],a[1],a[2]if slot==2 else 0,a[2]if slot==3 else 0,a[3])
M=(1,0,0,0,0);K=(0,1,0,0,0);I=(0,0,1,0,0);J=(0,0,0,1,0)
BASE=[sub(K,4),sub(sub(M,scale(K,3)),3)]
def countvec(c):return(c[0],c[1],0,0,c[2])
def domain(c,slot=2):
 n=I if slot==2 else J
 return BASE+[n,sub(sub(countvec(c),1),n)]
def pointcells(kind,x,y):return {(add(x,a),add(y,b))for a,b in {'R':((0,0),(1,0),(0,1)),'H':((0,0),(1,0),(2,0)),'V':((0,0),(0,1),(0,2)),'D':((0,0),(1,-1),(2,-2))}[kind]}
def rotate(cells):return{(y,sub(sub(v(1),x),y))for x,y in cells}
def reflect(cells):return{(x,sub(sub(v(1),x),y))for x,y in cells}
def parent_cells(own):
 if own['type']=='common':
  y=aff(own['row']);ell=aff(own['depth']);off=1 if own['branch']=='prefix'else 2
  x=sub(sub(sub(y,M),off),scale(ell,3));cells=pointcells('H',x,y)
  for _ in range(own['p']):cells=rotate(cells)
  return reflect(cells)
 row=families.specifications()['corner'][own['family']];a,b=aff(own['i']),aff(own['j'])
 def lin(z):return add(add(scale(M,z[0]),scale(K,z[1])),add(add(scale(a,z[2]),scale(b,z[3])),z[4]))
 cells=pointcells(row['kind'],lin(row['x']),sub(lin(row['y']),M))
 for _ in range(own['p']):cells=rotate(cells)
 return{(sub(x,2),add(y,1))for x,y in cells}

def obligations():
 groups=json.loads(Path(__file__).with_name('edits.json').read_text());certs=[];atoms=[];identities=0
 def bound(name,dom,target):certs.append({'name':name,'kind':'bound','constraints':dom+[v(1)],'target':target})
 def impossible(name,dom):certs.append({'name':name,'kind':'contradiction','constraints':dom,'target':v(-1)})
 for group in groups:
  name=group['name'];count=group['count'];bound(name+'/nonnegative-count',BASE,countvec(count))
  dom=domain(count)
  G.require(len(group['old'])==len(group['owners']),'Missing original source owner')
  for n,(old,own)in enumerate(zip(group['old'],group['owners'])):
   aname=f'{name}/{n}';kind,x,y=old
   G.require(pointcells(kind,aff(x),aff(y))==parent_cells(own),'Original generator map mismatch '+aname);identities+=1
   atoms.append((aname,count,own))
   if own['type']=='common':
    yy,ll=aff(own['row']),aff(own['depth'])
    for suffix,g in [('row-low',sub(yy,1)),('row-high',sub(add(add(M,scale(K,3)),1),yy)),('depth-low',ll),('depth-below-row',sub(sub(yy,1),ll)),('depth-below-q',sub(scale(K,3),ll))]:bound(aname+'/'+suffix,dom,g)
    g=sub(add(scale(K,3),1),yy)if own['branch']=='prefix'else sub(yy,add(scale(K,3),2));bound(aname+'/branch',dom,g)
    for r,(p,elo,ehi,lo,hi,_)in enumerate(ROWS):
     if p!=own['p']:continue
     lowell=add(scale(K,elo[0]),elo[1]);hiell=add(scale(K,ehi[0]),ehi[1])
     def f(a):return add(add(scale(M,a[0]),scale(K,a[1])),add(scale(ll,a[2]),a[3]))
     impossible(aname+f'/outside-A0-{r}',dom+[sub(ll,lowell),sub(hiell,ll),sub(yy,f(lo)),sub(f(hi),yy)])
   else:
    row=families.specifications()['corner'][own['family']];a,b=aff(own['i']),aff(own['j']);ic=countvec(row['I'])
    jc=v(1)if row['J']is None else add(countvec(row['J'][:3]),scale(a,row['J'][3]))
    for suffix,g in [('i-low',a),('i-high',sub(sub(ic,1),a)),('j-low',b),('j-high',sub(sub(jc,1),b))]:bound(aname+'/'+suffix,dom,g)
 # Within each source atom, parameter injectivity follows from a nonzero coefficient.
 for name,count,o in atoms:
  if count==(0,0,1)or count==[0,0,1]:continue
  coordinates=[o['row'],o['depth']]if o['type']=='common'else[o['i'],o['j']]
  G.require(any(z[2]!=0 for z in coordinates),'Noninjective original-index family '+name)
 for (na,ca,a),(nb,cb,b)in itertools.combinations(atoms,2):
  if a['type']!=b['type']or a['p']!=b['p']:continue
  if a['type']=='corner'and a['family']!=b['family']:continue
  dom=domain(ca)+domain(cb,3)
  keys=('row','depth')if a['type']=='common'else('i','j')
  for key in keys:
   diff=sub(aff(a[key]),aff(b[key],3));dom.extend([diff,neg(diff)])
  impossible(na+'!= '+nb,dom)
 return certs,{'original_generator_identities':identities,'atomic_old_families':len(atoms),'obligations':len(certs)}

def verify(path=None):
 certs,summary=obligations();path=Path(path)if path else Path(__file__).with_name('ownership-certificates.json');saved=json.loads(path.read_text())
 G.require(len(saved)==len(certs),'Missing or extra affine certificate')
 for ob,rec in zip(certs,saved):
  G.require(ob['name']==rec['name'],'Certificate order or identity changed')
  coeff=[Fraction(x)for x in rec['multipliers']];G.require(len(coeff)==len(ob['constraints'])and all(x>=0 for x in coeff),'Invalid dual coefficient')
  ans=[sum(c*row[j]for c,row in zip(coeff,ob['constraints']))for j in range(5)]
  G.require(tuple(ans)==tuple(ob['target']),'Exact affine contradiction/identity failed '+ob['name'])
 return dict(summary,status='PASS')
if __name__=='__main__':print(json.dumps(verify(),indent=2))
