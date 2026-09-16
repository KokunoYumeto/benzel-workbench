from regular import *
from collections import defaultdict,Counter
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix

def corner(k):
 m=12*k+5;R,A,S=build(m,k)
 chosen=[G.rotate_tile(G.tile('H',y+m+3*l,y),p)for l in range(k) for y in range(2-m,2)for p in range(3)]
 cov=G.incidence(chosen);G.require(max(cov.values())==1 and set(cov)<=R,'Long strip partition')
 rem=R-set(cov)
 C={(x,y+m)for x,y in rem if y< -m//2}
 G.require(len(C)*3==len(rem),'Corner cutoff')
 return C

def intervals(row):
 groups=[]
 for x in sorted(row):
  if groups and groups[-1][-1]==x-1:groups[-1].append(x)
  else:groups.append([x])
 return [(a[0],a[-1])for a in groups]

def solve_corner(k,seconds=10):
 cells=corner(k);idx={p:i for i,p in enumerate(sorted(cells))};ts=[]
 for x,y in sorted(cells):
  for kind in ['H','V','D']:
   t=G.tile(kind,x,y)
   if set(t[1])<=cells:ts.append(t)
 rows=[idx[p]for t in ts for p in t[1]];cols=[j for j,t in enumerate(ts)for p in t[1]]
 mat=coo_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(idx),len(ts))).tocsc()
 res=milp(np.array([{'H':1,'V':2,'D':3}[t[0]]for t in ts]),integrality=np.ones(len(ts)),bounds=Bounds(0,1),constraints=LinearConstraint(mat,1,1),options={'time_limit':seconds})
 out={'k':k,'status':int(res.status),'message':res.message}
 if res.x is not None:
  chosen=tuple(t for x,t in zip(res.x,ts)if x>.5);G.check_partition(chosen,cells)
  out['tiles']=G.encode_anchors(chosen);out['success']=True
 return out
if __name__=='__main__':
 import sys,json
 k=int(sys.argv[1]);C=corner(k);rows=defaultdict(list)
 for x,y in C:rows[y].append(x)
 print('rows:',[(y,intervals(v))for y,v in sorted(rows.items())])
 out=solve_corner(k,15);print(out)
 open(f'/mnt/data/benzel-p7-turn8/turn8/exploration/corner-{k}.json','w').write(json.dumps(out))
