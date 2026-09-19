"""Exact original-source maps and affine certificates. Standard library only."""
from pathlib import Path
from fractions import Fraction
import json,itertools,sys,importlib.util
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'turn8'))
import geometry as G,families
from source10 import ROWS as ROWS10
ROWS=ROWS10
RR=2;KFIX=None;SUFFIX="";SHIFT=(-1,-1)
ROOT=Path(__file__).resolve().parent
def configure(k=None,r=2):
 global BASE,ROWS,RR,KFIX,SUFFIX,SHIFT
 RR=r;KFIX=k;SUFFIX='' if k is None else f'-k{k}-r{r}';SHIFT=(-1,-1)if r==2 else(-2,1)
 BASE=[sub(K,4),sub(sub(M,scale(K,3)),4)]if k is None else[sub(K,k),sub(k,K),sub(sub(M,scale(K,3)),r+2)]
 if r==1:
  spec=importlib.util.spec_from_file_location('source9_for_ownership',ROOT.parent/'turn9/source_table.py');obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);ROWS=obj.ROWS
 else:ROWS=ROWS10

Z=(0,0,0,0,0)
def v(a=0):return(0,0,0,0,a)if type(a)is int else tuple(a)
def add(a,b):return tuple(x+y for x,y in zip(v(a),v(b)))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(v(b)))
def scale(a,n):return tuple(x*n for x in a)
def aff(a,slot=2):return(a[0],a[1],a[2]if slot==2 else 0,a[2]if slot==3 else 0,a[3])
M=(1,0,0,0,0);K=(0,1,0,0,0);I=(0,0,1,0,0);J=(0,0,0,1,0)
BASE=[sub(K,4),sub(sub(M,scale(K,3)),4)]
def count(c):return(c[0],c[1],0,0,c[2])
def domain(c,slot=2):
 n=I if slot==2 else J
 return BASE+[n,sub(sub(count(c),1),n)]
def cells(kind,x,y):return{(add(x,a),add(y,b))for a,b in G.OFFSETS[kind]}
def rotate(cs):return{(y,sub(sub(1,x),y))for x,y in cs}
def reflect(cs):return{(x,sub(sub(1,x),y))for x,y in cs}
def owner_cells(o):
 if o['type']=='common':
  y,l=aff(o['row']),aff(o['depth']);off=1 if o['branch']=='prefix'else 2
  x=sub(sub(sub(y,M),off),scale(l,3));cs=cells('H',x,y)
  for _ in range(o['p']):cs=rotate(cs)
  return reflect(cs)
 G.require(o['type']=='parent','Unexpected non-initial generator owner')
 f=families.specifications()[o['part']][o['family']];a,b=aff(o['i']),aff(o['j'])
 def lin(z):return add(add(scale(M,z[0]),scale(K,z[1])),add(add(scale(a,z[2]),scale(b,z[3])),z[4]))
 x,y=lin(f['x']),lin(f['y'])
 if o['part']=='corner':y=sub(y,M)
 cs=cells(f['kind'],x,y)
 for _ in range(o['p']):cs=rotate(cs)
 return{(add(x,SHIFT[0]),add(y,SHIFT[1]))for x,y in cs}
def obligations():
 groups=json.loads((ROOT/f'edits{SUFFIX}.json').read_text());out=[];atoms=[];identities=0
 def specialized(cs):
  if KFIX is None:return cs
  def sp(x):return(x[0],0,x[2],x[3],x[4]+KFIX*x[1])
  return{(sp(x),sp(y))for x,y in cs}
 def bound(name,dom,target):out.append({'name':name,'constraints':dom+[v(1)],'target':target})
 def impossible(name,dom):out.append({'name':name,'constraints':dom,'target':v(-1)})
 for g in groups:
  name=g['name'];c=g['count'];bound(name+'/count',BASE,count(c));dom=domain(c)
  G.require(len(g['old'])==len(g.get('owners',[])),'Missing original owner map')
  for j,(old,o)in enumerate(zip(g['old'],g['owners'])):
   nm=name+'/'+str(j)
   G.require(specialized(cells(old[0],aff(old[1]),aff(old[2])))==specialized(owner_cells(o)),'Original generator mismatch '+nm);identities+=1;atoms.append((nm,c,o))
   if o['type']=='common':
    yy,ll=aff(o['row']),aff(o['depth'])
    for suffix,t in [('y0',sub(yy,1)),('y1',sub(add(add(M,scale(K,3)),RR),yy)),('l0',ll),('ly',sub(sub(yy,1),ll)),('lq',sub(add(scale(K,3),RR-1),ll)),('branch',sub(add(scale(K,3),RR),yy)if o['branch']=='prefix'else sub(yy,add(scale(K,3),RR+1)))]:bound(nm+'/'+suffix,dom,t)
    for j,(p,elo,ehi,lo,hi,_)in enumerate(ROWS):
     if p!=o['p']:continue
     def r(z):return add(add(scale(M,z[0]),scale(K,z[1])),add(scale(ll,z[2]),z[3]))
     impossible(nm+'/outside-A0-'+str(j),dom+[sub(ll,add(scale(K,elo[0]),elo[1])),sub(add(scale(K,ehi[0]),ehi[1]),ll),sub(yy,r(lo)),sub(r(hi),yy)])
   else:
    f=families.specifications()[o['part']][o['family']];a,b=aff(o['i']),aff(o['j']);ni=count(f['I']);nj=v(1)if f['J']is None else add(count(f['J'][:3]),scale(a,f['J'][3]))
    for suffix,t in [('i0',a),('i1',sub(sub(ni,1),a)),('j0',b),('j1',sub(sub(nj,1),b))]:bound(nm+'/'+suffix,dom,t)
 for name,c,o in atoms:
  if c==[0,0,1]:continue
  coords=[o['row'],o['depth']]if o['type']=='common'else[o['i'],o['j']]
  G.require(any(z[2]for z in coords),'Repeated source index '+name)
 comparisons=0
 for (na,ca,a),(nb,cb,b)in itertools.combinations(atoms,2):
  if a['type']!=b['type']or a['p']!=b['p']:continue
  if a['type']=='parent'and(a['part'],a['family'])!=(b['part'],b['family']):continue
  dom=domain(ca)+domain(cb,3)
  for key in (('row','depth')if a['type']=='common'else('i','j')):
   diff=sub(aff(a[key]),aff(b[key],3));dom += [diff,neg(diff)]
  impossible(na+' != '+nb,dom);comparisons+=1
 return out,{'original_generator_identities':identities,'source_atoms':len(atoms),'source_distinctness_comparisons':comparisons,'affine_certificates':len(out)}
def verify(path=None):
 obs,rec=obligations();data=json.loads(Path(path or ROOT/f'ownership-certificates{SUFFIX}.json').read_text());G.require(len(data)==len(obs),'Certificate count drift')
 for o,c in zip(obs,data):
  G.require(c['name']==o['name'],'Certificate association changed');co=[Fraction(s)for s in c['multipliers']]
  G.require(len(co)==len(o['constraints'])and all(z>=0 for z in co),'Nonpositive or missing multiplier')
  result=tuple(sum(q*r[j]for q,r in zip(co,o['constraints']))for j in range(5))
  G.require(result==tuple(o['target']),'Exact affine certificate failed '+o['name'])
 return dict(rec,status='PASS',domain=('integers k>=4,m>=3k+4' if KFIX is None else f'k={KFIX}, integers m>={3*KFIX+RR+2}'),optimizer_used_by_verifier=False)
if __name__=='__main__':
 import argparse
 a=argparse.ArgumentParser();a.add_argument('--k',type=int);a.add_argument('--r',type=int,default=2);arg=a.parse_args();configure(arg.k,arg.r);print(json.dumps(verify(),indent=2))
