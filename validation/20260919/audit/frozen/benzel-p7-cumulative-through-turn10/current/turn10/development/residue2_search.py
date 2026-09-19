from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'turn8'))
import geometry as G
from scipy.optimize import milp,LinearConstraint,Bounds
from scipy.sparse import csc_matrix
import numpy as np

def solve(n,k,s):
 outer=G.region_ab(n+3*k,2*n+3*k-1);inner={(x+s[0],y+s[1])for x,y in G.region_ab(n+3*k-3,2*n+3*k-4)}
 assert inner<=outer
 cs=outer-inner;ix={c:i for i,c in enumerate(sorted(cs))};ts=set()
 for kind,offs in G.OFFSETS.items():
  for x,y in cs:
   for a,b in offs:
    t=G.tile(kind,x-a,y-b)
    if set(t[1])<=cs:ts.add(t)
 ts=sorted(ts);rr=[];cc=[]
 for j,t in enumerate(ts):
  for c in t[1]:rr.append(ix[c]);cc.append(j)
  if t[0]=='R':rr.append(len(cs));cc.append(j)
 mat=csc_matrix((np.ones(len(rr)),(rr,cc)),shape=(len(cs)+1,len(ts)))
 res=milp(np.array([1.+.001*j for j,t in enumerate(ts)]),integrality=np.ones(len(ts)),bounds=Bounds(0,1),constraints=LinearConstraint(mat,1,1),options={'time_limit':5})
 if res.x is None:return None
 ans=[t for t,x in zip(ts,res.x)if x>.5];G.check_partition(ans,cs);return G.encode_anchors(ans)
if __name__=='__main__':
 for s in[(-2,1),(1,1),(1,-2),(0,0)]:
  for n,k in[(3,1),(4,2),(5,3),(3,3),(8,2)]:
   a=solve(n,k,s);print('n,k,s',n,k,s,'tiling',a,flush=True)
