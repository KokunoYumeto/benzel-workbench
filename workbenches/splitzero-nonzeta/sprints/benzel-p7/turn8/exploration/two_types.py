from regular2 import G
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
import json,numpy as np,time,sys
from pathlib import Path
ROOT=Path('/mnt/data/benzel-p7-turn8/turn8/exploration')
for k in range(1,11):
 C=set(map(tuple,json.loads((ROOT/f'forced-{k}.json').read_text())['residual']));idx={p:i for i,p in enumerate(sorted(C))}
 ts=[G.tile(kind,x,y)for x,y in sorted(C)for kind in ['V','D']if set(G.tile(kind,x,y)[1])<=C]
 row=[idx[p]for t in ts for p in t[1]];col=[j for j,t in enumerate(ts)for p in t[1]]
 mat=coo_matrix((np.ones(len(row)),(row,col)),shape=(len(C),len(ts))).tocsc()
 res=milp(np.ones(len(ts)),integrality=np.ones(len(ts)),bounds=Bounds(0,1),constraints=LinearConstraint(mat,1,1),options={'time_limit':3})
 print(k,res.status,flush=True)
 if res.x is not None:
  B=[t for z,t in zip(res.x,ts)if z>.5]
  try:G.check_partition(B,C)
  except:continue
  (ROOT/f'twotypes-{k}.json').write_text(json.dumps({'k':k,'tiles':G.encode_anchors(B)}))
