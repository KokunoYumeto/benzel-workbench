from regular import *
from collections import defaultdict

def body(m,q,K):
 out=[]
 for y in range(1,m+q+1):
  r=m-1 if y<=q else m
  for dep in range(min(y,K,q)):
   t=G.tile('H',y-r-2-3*dep,y)
   out.extend(G.reflect_tile(G.rotate_tile(t,p))for p in range(3))
 return out

def try_make(k,K,crop1=0,crop2=0):
 q=3*k;m=25*q+5
 A=body(m,q,K);om=G.omega(G.triangular(m)-q)
 remstones={G.rotate_tile(G.tile('R',m-2-a,-a),p)for a in range(k)for p in range(3)}
 stones=set(P.base_stones(m))-remstones
 R=(set(om)|{p for t in A for p in t[1]})-{p for t in stones for p in t[1]}
 bs=[G.rotate_tile(G.tile('H',y+m+3*ell,y),p)for ell in range(K)for y in range(2-m+crop1,2-crop2)for p in range(3)]
 cov=G.incidence(bs)
 if set(cov)-R or any(v!=1 for v in cov.values()):return None,{'outside':len(set(cov)-R),'overlap':sum(v-1 for v in cov.values())}
 remain=R-set(cov)
 C={(x,y+m)for x,y in remain if y<-m//2}
 if 3*len(C)!=len(remain):return None,{'noncorner':len(remain)-3*len(C)}
 return C,{'size':len(C)}

def solve_cells(C,secs=5):
 import numpy as np
 from scipy.optimize import milp,Bounds,LinearConstraint
 from scipy.sparse import coo_matrix
 idx={p:i for i,p in enumerate(sorted(C))};ts=[]
 for x,y in sorted(C):
  for k in ['H','V','D']:
   t=G.tile(k,x,y)
   if set(t[1])<=C:ts.append(t)
 rows=[idx[p]for t in ts for p in t[1]];cols=[j for j,t in enumerate(ts)for p in t[1]]
 mat=coo_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(idx),len(ts))).tocsc()
 res=milp(np.ones(len(ts)),integrality=np.ones(len(ts)),bounds=Bounds(0,1),constraints=LinearConstraint(mat,1,1),options={'time_limit':secs})
 if res.x is not None:
  B=[t for z,t in zip(res.x,ts)if z>.5]
  try:G.check_partition(B,C);return B
  except:pass
 return None
if __name__=='__main__':
 import sys,json,time
 k,K,c1,c2=map(int,sys.argv[1:5]);C,inf=try_make(k,K,c1,c2);print(k,K,c1,c2,inf,flush=True)
 if C is not None:
  B=solve_cells(C,15);print('SOLVED',B is not None)
  if B:open(f'/mnt/data/benzel-p7-turn8/turn8/exploration/newcorner-{k}-{K}-{c1}-{c2}.json','w').write(json.dumps({'k':k,'K':K,'crop1':c1,'crop2':c2,'cells':sorted(C),'tiles':G.encode_anchors(B)}))
