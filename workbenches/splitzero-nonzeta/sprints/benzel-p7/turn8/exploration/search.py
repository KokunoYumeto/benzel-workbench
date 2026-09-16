import sys, time, json
from pathlib import Path
sys.path.insert(0,'/mnt/data/benzel-p7-turn7/turn7')
import construction as C,geometry as G,parent_construction as P
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix

def deleted(m,q):
 shift={0:(0,0),1:(-2,1),2:(-1,-1)}[q%3]
 out=[]
 for i in range(q):
  a,p=divmod(i,3);t=G.rotate_tile(G.tile('R',m-2-a,-a),p)
  out.append(('R',tuple(sorted((x+shift[0],y+shift[1])for x,y in t[1]))))
 return tuple(out)

def make_region(m,q):
 A=C.common_body(m,q);O=G.omega(G.triangular(m)-q)
 shift={0:(0,0),1:(-2,1),2:(-1,-1)}[q%3]
 stones=set(('R',tuple(sorted((x+shift[0],y+shift[1])for x,y in t[1])))for t in P.base_stones(m))
 rem=set(deleted(m,q));G.require(rem<=stones,'Delete not found');stones-=rem
 cells=set(O)|{p for t in A for p in t[1]}
 G.require({p for t in stones for p in t[1]}<=cells,'Stones outside common body')
 cells-={p for t in stones for p in t[1]}
 return frozenset(cells),A,tuple(stones)

def solve(m,q,seconds=10,mode=0):
 cells,A,stones=make_region(m,q);sym=q%3==0
 rep=lambda p:min(G.orbit(p)) if sym else p
 orbit_cells=sorted({rep(p)for p in cells});idx={p:i for i,p in enumerate(orbit_cells)}
 groups=[]
 for x,y in sorted(cells):
  for kind in (['H'] if sym else ['H','V','D']):
   t=G.tile(kind,x,y)
   if not set(t[1])<=cells:continue
   ts=tuple(G.rotate_tile(t,j)for j in range(3))if sym else (t,)
   flat=[p for tt in ts for p in tt[1]]
   if len(set(flat))<len(flat):continue
   reps=[rep(p)for p in t[1]]
   if sym and len(set(reps))!=3:continue
   groups.append((ts,reps))
 rows=[];cols=[]
 for j,(ts,reps)in enumerate(groups):
  for p in reps:rows.append(idx[p]);cols.append(j)
 Aeq=coo_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(idx),len(groups))).tocsc()
 old=set(A)
 costs=[]
 for ts,reps in groups:
  # preserve original source unless strict objective encourages a different support
  t=ts[0];x,y=G.anchor(t)
  if mode==0:c=0 if t in old else 1
  elif mode==1:c=abs(2*x+y-1)+0.001*abs(x-y)
  elif mode==2:c=abs(x+y-1)
  else:c=abs(x)+abs(y)
  costs.append(c)
 start=time.monotonic();res=milp(np.array(costs),integrality=np.ones(len(groups)),bounds=Bounds(0,1),constraints=LinearConstraint(Aeq,1,1),options={'time_limit':seconds,'mip_rel_gap':0.0})
 out={'m':m,'q':q,'cells':len(cells),'variables':len(groups),'status':int(res.status),'message':res.message,'seconds':time.monotonic()-start,'mode':mode}
 if res.x is not None:
  chosen=tuple(t for z,(ts,reps)in zip(res.x,groups)if z>0.5 for t in ts)
  try:G.check_partition(chosen,cells)
  except Exception as e:out['invalid']=str(e);return out
  out['replacement']=G.encode_anchors(chosen)
  out['released']=G.encode_anchors(set(A)-set(chosen))
  out['new']=G.encode_anchors(set(chosen)-set(A))
  out['success']=True
  print('tiles',len(chosen),'changed',len(out['new']))
 return out
if __name__=='__main__':
 m,q,mode=map(int,sys.argv[1:4]);out=solve(m,q,15,mode)
 print({k:v for k,v in out.items() if k not in ['replacement','released','new']})
 Path(f'/mnt/data/benzel-p7-turn8/turn8/exploration/solve-{m}-{q}-{mode}.json').write_text(json.dumps(out))
