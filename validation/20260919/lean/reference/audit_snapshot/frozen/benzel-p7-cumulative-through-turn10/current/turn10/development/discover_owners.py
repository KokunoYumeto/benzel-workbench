"""Development only: discover exact owner maps and rational affine certificates."""
from pathlib import Path
import sys,json,itertools
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog
import sympy as sp
from build_edits import A,transform_row
import source10 as S
import argparse,importlib.util
parser=argparse.ArgumentParser();parser.add_argument("--k",type=int);parser.add_argument("--r",type=int,default=2);ARGS=parser.parse_args()
RR=ARGS.r
SUFFIX="" if ARGS.k is None else f"-k{ARGS.k}-r{RR}"
SHIFT=(-1,-1) if RR==2 else (-2,1)
if RR==1:
 spec=importlib.util.spec_from_file_location("source9",Path(__file__).resolve().parents[1]/"turn9/source_table.py");S=importlib.util.module_from_spec(spec);spec.loader.exec_module(S)
ROOT=Path(__file__).resolve().parent
families=json.loads((ROOT.parent/'turn8/families.json').read_text())
Z=A();M=A((1,0,0,0));K=A((0,1,0,0));I=A((0,0,1,0))
BASE=[K-4,M-3*K-4] if ARGS.k is None else [K-ARGS.k,ARGS.k-K,M-3*K-RR-2]
def count(c):return A((c[0],c[1],0,c[2]))
def bound(dom,v):
 # Return exact nonnegative coefficients, including constant 1.
 rows=list(dom)+[A(1)];v=A(v)
 rr=linprog(np.zeros(len(rows)),A_eq=np.array(rows,dtype=float).T,b_eq=np.array(v,dtype=float),bounds=(0,None),method='highs')
 if rr.x is None:return None
 cs=[F(float(x)).limit_denominator(1000000)for x in rr.x]
 if min(cs)<0 or any(sum(a*r[j]for a,r in zip(cs,rows))!=v[j]for j in range(4)):return None
 return list(map(str,cs))
def nointer(dom):return bound(dom,A(-1))
def owner_constraints(o,old,count0):
 dom=BASE+[I,count(count0)-1-I];obs=[]
 def b(name,v):obs.append((name,dom,A(v)))
 if o['type']=='common':
  y,l=A(o['row']),A(o['depth']);
  for name,v in [('y0',y-1),('y1',M+3*K+RR-y),('l0',l),('l1',y-1-l),('lq',3*K+RR-1-l)]:b(name,v)
  b('branch',3*K+RR-y if o['branch']=='prefix'else y-3*K-RR-1)
  for j,(p,el,eh,lo,hi,_)in enumerate(S.ROWS):
   if p!=o['p']:continue
   rlo=M*lo[0]+K*lo[1]+l*lo[2]+lo[3];rhi=M*hi[0]+K*hi[1]+l*hi[2]+hi[3]
   subdom=dom+[l-(K*el[0]+el[1]),K*eh[0]+eh[1]-l,y-rlo,rhi-y]
   obs.append(('outside-A0-'+str(j),subdom,A(-1)))
 elif o['type']=='parent':
  row=families[o['part']][o['family']];a,bidx=A(o['i']),A(o['j']);ni=count(row['I']);nj=A(1)if row['J']is None else count(row['J'][:3])+a*row['J'][3]
  for name,v in [('i0',a),('i1',ni-1-a),('j0',bidx),('j1',nj-1-bidx)]:b(name,v)
 else:
  new=groups[o['group']];i=A(o['i'])
  b('n0',i);b('n1',count(new['count'])-1-i)
 return obs

def common_candidates(old):
 kind,x,y=old;x,y=A(x),A(y)
 if kind=='D':p,Y,X=0,1-x-y,x
 elif kind=='V':p,Y,X=1,x,y
 elif kind=='H':p,Y,X=2,y,-x-y-1
 else:return
 for part,off in [('prefix',1),('tail',2)]:
  ell=Y-M-off-X
  if any(a%3 for a in ell):continue
  yield {'type':'common','p':p,'row':list(Y),'depth':[a//3 for a in ell],'branch':part}

def transformed_parent(part,fn,p):
 row=families[part][fn];xy=[]
 for v in (row['x'],row['y']):xy.append(tuple(v))
 if part=='corner':xy[1]=(xy[1][0]-1,*xy[1][1:])
 # Five coefficient slots m,k,a,b,const. Transform original tile anchor.
 kind=row['kind'];x,y=xy
 def add(x,y):return tuple(a+b for a,b in zip(x,y))
 def neg(x):return tuple(-a for a in x)
 one=(0,0,0,0,1)
 for _ in range(p):
  if kind=='R':kind,x,y='R',y,neg(add(x,y))
  elif kind=='H':kind,x,y='V',y,neg(add(add(x,y),one))
  elif kind=='V':kind,x,y='D',y,add(one,neg(add(x,y)))
  else:kind,x,y='H',add(y,(0,0,0,0,-2)),add(one,neg(add(x,y)))
 x,y=add(x,(0,0,0,0,SHIFT[0])),add(y,(0,0,0,0,SHIFT[1]))
 if ARGS.k is not None:
  x=(x[0],0,x[2],x[3],x[4]+ARGS.k*x[1]);y=(y[0],0,y[2],y[3],y[4]+ARGS.k*y[1])
 return kind,x,y

def parent_candidates(old):
 for part in ['corner','long']:
  for fn,row in enumerate(families[part]):
   for p in range(3):
    kind,x,y=transformed_parent(part,fn,p)
    if kind!=old[0]:continue
    rx=A(old[1])-A((x[0],x[1],0,x[4]));ry=A(old[2])-A((y[0],y[1],0,y[4]));det=x[2]*y[3]-x[3]*y[2]
    if det:
     ai=[F(rx[j]*y[3]-ry[j]*x[3],det)for j in range(4)];bi=[F(ry[j]*x[2]-rx[j]*y[2],det)for j in range(4)]
    else:
     # Free parameter fixed by a count-one axis.
     ni=count(row['I']);jj=row['J']
     if ni==A(1):
      ai=[F(0)]*4
      slope=x[3]or y[3]
      if not slope:continue
      bi=[F(t,slope)for t in (rx if x[3]else ry)]
     elif jj is None or jj==[0,0,1,0]:
      bi=[F(0)]*4;slope=x[2]or y[2]
      if not slope:continue
      ai=[F(t,slope)for t in (rx if x[2]else ry)]
     else:continue
    if any(t.denominator!=1 for t in ai+bi):continue
    ai,bi=A([int(t)for t in ai]),A([int(t)for t in bi])
    if ai*x[2]+bi*x[3]!=rx or ai*y[2]+bi*y[3]!=ry:continue
    yield {'type':'parent','part':part,'family':fn,'p':p,'i':list(ai),'j':list(bi)}
def new_candidates(old,gidx):
 for j,g in enumerate(groups[:gidx]):
  for r,new in enumerate(g['new']):
   if new[0]!=old[0]:continue
   x,y=A(new[1]),A(new[2]);dx=A(old[1])-A((x[0],x[1],0,x[3]));dy=A(old[2])-A((y[0],y[1],0,y[3]));c=x[2]or y[2]
   if not c:
    if dx==Z and dy==Z:yield {'type':'new','group':j,'row':r,'i':list(Z)}
    continue
   qi=[F(t,c)for t in (dx if x[2]else dy)]
   if any(t.denominator!=1 for t in qi):continue
   qi=A([int(t)for t in qi])
   if qi*x[2]!=dx or qi*y[2]!=dy:continue
   yield {'type':'new','group':j,'row':r,'i':list(qi)}

if __name__=='__main__':
 groups=json.loads((ROOT/f'edits{SUFFIX}.json').read_text());fails=[];allobs=[]
 for gi,g in enumerate(groups):
  owners=[]
  for oi,old in enumerate(g['old']):
   found=None
   for o in itertools.chain(common_candidates(old),parent_candidates(old),new_candidates(old,gi)):
    obs=owner_constraints(o,old,g['count']);receipt=[]
    for name,dom,t in obs:
     cc=bound(dom,t)
     if cc is None:break
     receipt.append({'name':g['name']+'/'+str(oi)+'/'+name,'multipliers':cc})
    else:found=o;allobs+=receipt;break
   owners.append(found)
   print(g['name'],oi,found,flush=True)
   if found is None:fails.append([gi,oi,old])
  g['owners']=owners
 (ROOT/f'edits{SUFFIX}-with-owners.json').write_text(json.dumps(groups,indent=2)+'\n')
 (ROOT/f'owner-bounds{SUFFIX}.json').write_text(json.dumps(allobs,separators=(',',':'))+'\n')
 print('FAILS',fails)
