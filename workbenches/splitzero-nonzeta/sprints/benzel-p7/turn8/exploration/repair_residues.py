from remainder_residues import *
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix

def solve_patch(cells,old,seconds=8):
 ps=sorted(cells);idx={p:i for i,p in enumerate(ps)};T=[]
 for x,y in ps:
  for kind in ['H','V','D']:
   t=G.tile(kind,x,y)
   if set(t[1])<=cells:T.append(t)
 if not cells:return (),{'status':0}
 mat=coo_matrix((np.ones(3*len(T)),([idx[p]for t in T for p in t[1]],[j for j,t in enumerate(T)for _ in t[1]])),shape=(len(ps),len(T))).tocsc()
 cost=np.array([0.0 if t in old else 1.0 for t in T])
 res=milp(cost,integrality=np.ones(len(T)),bounds=Bounds(0,1),constraints=LinearConstraint(mat,1,1),options={'time_limit':seconds,'mip_rel_gap':0.0})
 info={'status':int(res.status),'message':res.message,'variables':len(T),'cells':len(cells)}
 if res.x is None:return None,info
 chosen=tuple(t for z,t in zip(res.x,T)if z>.5)
 try:G.check_partition(chosen,cells)
 except ValueError:return None,info
 info.update(changed=len(set(chosen)-old),positive=True)
 return chosen,info

def attempt(k,r,m,radius,p):
 rem,A,S,old,info=setup(k,r,m)
 centers=[(0,1-m),(1-m,m),(m,0)];center=centers[p]
 def distance(z):x,y=z;return max(abs(x-center[0]),abs(y-center[1]),abs(x+y-center[0]-center[1]))
 holes={z for z in rem if distance(z)<=radius}
 take={t for t in old if any(distance(z)<=radius for z in t[1])}
 cells=holes|set(G.incidence(take))
 new,inf=solve_patch(cells,take,12)
 if new is not None:
  removed=take-set(new);added=set(new)-take
  d={'k':k,'r':r,'m':m,'p':p,'radius':radius,'info':inf,'holes':sorted(holes),'remove':G.encode_anchors(removed),'add':G.encode_anchors(added)}
  (ROOT/'exploration'/f'repair-r{r}-k{k}-p{p}.json').write_text(json.dumps(d))
 return inf

if __name__=='__main__':
 import sys
 ks=list(map(int,sys.argv[1:]))or[1,2,3,4,5]
 for k in ks:
  for r in [1,2]:
   for p in ([0,2]if r==1 else[0,1,2]):
    inf=attempt(k,r,30*k+10,8*k+6,p)
    print(k,r,p,inf,flush=True)
