from regular2 import G,solve_cells
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
import json,numpy as np,time,sys
from pathlib import Path
ROOT=Path('/mnt/data/benzel-p7-turn8/turn8/exploration')
def top(k):return [G.tile('H',1+3*j,2)for j in range(k-1)]+[G.tile('H',y+3*j,y)for y in range(3,k+1)for j in range(k-y+1)]
def bottom(k,dx=0,dy=0):return [G.tile('H',1+r+3*j+dx,1-r+dy)for r in range(k-1)for j in range(k-1-r)]
if __name__=='__main__':
 for k in map(int,sys.argv[1:]):
  C=set(map(tuple,json.loads((ROOT/f'forced-{k}.json').read_text())['residual']));T=top(k)+bottom(k);cov=G.incidence(T)
  if max(cov.values())!=1 or not set(cov)<=C:print(k,'BADTOP');continue
  C-=set(cov);idx={p:i for i,p in enumerate(sorted(C))};ts=[G.tile(kind,x,y)for x,y in sorted(C)for kind in ['V','D']if set(G.tile(kind,x,y)[1])<=C]
  rows=[idx[p]for t in ts for p in t[1]];col=[j for j,t in enumerate(ts)for p in t[1]];mat=coo_matrix((np.ones(len(rows)),(rows,col)),shape=(len(C),len(ts))).tocsc()
  res=milp(np.zeros(len(ts)),integrality=np.ones(len(ts)),bounds=Bounds(0,1),constraints=LinearConstraint(mat,1,1),options={'time_limit':6})
  print(k,'status',res.status,flush=True)
  if res.x is not None:
   B=[t for z,t in zip(res.x,ts)if z>.5];G.check_partition(B,C)
   (ROOT/f'twotri-{k}.json').write_text(json.dumps({'k':k,'tiles':G.encode_anchors(B+T),'VD':G.encode_anchors(B)}))
