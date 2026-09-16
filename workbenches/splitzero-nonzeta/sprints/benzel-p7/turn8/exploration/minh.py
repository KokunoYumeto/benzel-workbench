from regular2 import G
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
import json,numpy as np,time,sys
from pathlib import Path
ROOT=Path('/mnt/data/benzel-p7-turn8/turn8/exploration')
for k in map(int,sys.argv[1:]):
 C=set(map(tuple,json.loads((ROOT/f'forced-{k}.json').read_text())['residual']));idx={p:i for i,p in enumerate(sorted(C))}
 ts=[G.tile(kind,x,y)for x,y in sorted(C)for kind in ['H','V','D']if set(G.tile(kind,x,y)[1])<=C]
 row=[idx[p]for t in ts for p in t[1]];col=[j for j,t in enumerate(ts)for p in t[1]]
 mat=coo_matrix((np.ones(len(row)),(row,col)),shape=(len(C),len(ts))).tocsc()
 res=milp(np.array([1 if t[0]=='H'else 0 for t in ts]),integrality=np.ones(len(ts)),bounds=Bounds(0,1),constraints=LinearConstraint(mat,1,1),options={'time_limit':8})
 if res.x is not None:
  B=[t for z,t in zip(res.x,ts)if z>.5]
  try:G.check_partition(B,C)
  except:continue
  H=[G.anchor(t)for t in B if t[0]=='H'];print(k,'H',len(H),'bound',res.mip_gap,'status',res.status,H,flush=True)
  (ROOT/f'minh-{k}.json').write_text(json.dumps({'k':k,'tiles':G.encode_anchors(B),'H':H,'solver_status':int(res.status)}))
 else:print(k,'NO',res.status,flush=True)
