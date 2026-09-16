from regular2 import G
import numpy as np,json,time,sys
from pathlib import Path
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
ROOT=Path('/mnt/data/benzel-p7-turn8/turn8/exploration')

def solve(C,old,secs=5):
 idx={p:i for i,p in enumerate(sorted(C))};ts=[]
 for x,y in sorted(C):
  for kind in ['H','V','D']:
   t=G.tile(kind,x,y)
   if set(t[1])<=C:ts.append(t)
 row=[idx[p]for t in ts for p in t[1]];col=[i for i,t in enumerate(ts)for p in t[1]]
 mat=coo_matrix((np.ones(len(row)),(row,col)),shape=(len(idx),len(ts))).tocsc()
 res=milp(np.array([0 if t in old else 1 for t in ts]),integrality=np.ones(len(ts)),bounds=Bounds(0,1),constraints=LinearConstraint(mat,1,1),options={'time_limit':secs})
 if res.x is None:return None,int(res.status)
 B=[t for z,t in zip(res.x,ts)if z>.5]
 try:G.check_partition(B,C);return set(B),int(res.status)
 except:return None,int(res.status)
if __name__=='__main__':
 old=set();delta=(-1,-1)
 for k in range(1,11):
  C=set(map(tuple,json.loads((ROOT/f'forced-{k}.json').read_text())['residual']))
  source={(t[0],tuple(sorted((x+delta[0],y+delta[1])for x,y in t[1])))for t in old}
  G.require(all(set(t[1])<=C for t in source),'Source outside')
  B,status=solve(C,source,4)
  if B is None:print(k,'FAIL',status,flush=True);break
  release=source-B;new=B-source
  print(k,'released',len(release),'new',len(new),'status',status,flush=True)
  (ROOT/f'recur-{k}.json').write_text(json.dumps({'k':k,'shift':delta,'tiles':G.encode_anchors(B),'release':G.encode_anchors(release),'new':G.encode_anchors(new),'solver_status':status}))
  old=B
