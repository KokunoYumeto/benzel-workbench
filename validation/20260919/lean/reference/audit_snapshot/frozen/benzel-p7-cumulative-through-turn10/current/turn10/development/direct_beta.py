from pathlib import Path
import sys,json
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT),str(ROOT.parent/'turn8'),str(ROOT.parent/'turn9')]
import geometry as G,packing as P,construction as C
# Avoid module source-table aliases: use only literal edit JSON from parent.
from core10 import shift,expand
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import csc_matrix

def initial(k,m,r=1):
 q=3*k+r;common=[]
 for p in range(3):
  for y in range(1,m+q+1):
   for ell in range(min(y,q)):
    rr=m-1 if y<=q else m
    common.append(G.reflect_tile(G.rotate_tile(G.tile('H',y-rr-2-3*ell,y),p)))
 base=set(C.retained_stones(m,k));extra={G.rotate_tile(G.tile('R',m-2-k,-k),p)for p in([0]if r==1 else[0,2])}
 ss=(-2,1)if r==1 else(-1,-1);stones=tuple(shift(t,ss)for t in base-extra);bones=tuple(shift(t,ss)for t in C.new_bones(m,k))
 covered=set(G.incidence(stones+bones));A0={t for t in common if covered&set(t[1])};states=set(common)-A0|set(bones);target=G.omega(G.triangular(m)-q)|set(G.incidence(common));holes=target-set(G.incidence(tuple(states)+stones))
 return states,stones,set(holes),common,A0

def apply(st,holes,old,new):
 assert set(old)<=st,('old missing',G.encode_anchors(set(old)-st))
 oldcs=set(G.incidence(old));newcs=set(G.incidence(new));assert newcs<=oldcs|holes,('collision',newcs-(oldcs|holes))
 st.difference_update(old);st.update(new);holes.difference_update(newcs);holes.update(oldcs-newcs)

def beforelower(k,m,r=1):
 states,stones,holes,common,a0=initial(k,m,r)
 gs=json.loads((ROOT.parent/'turn9/edits.json').read_text())
 from build_edits import transform_row
 for g in gs:
  if g['name']=='lower':break
  n=g['count'][0]*m+g['count'][1]*k+g['count'][2]
  for i in range(n):
   old=[expand(row if r==1 else transform_row(row,0,(1,-2)),m,k,i)for row in g['old']]
   new=[expand(row if r==1 else transform_row(row,0,(1,-2)),m,k,i)for row in g['new']]
   apply(states,holes,old,new)
 return states,stones,holes

def cover(cells,original,limit=20):
 cells=set(cells);cc=sorted(cells);index={p:i for i,p in enumerate(cc)};tiles=set()
 for kind,offsets in G.OFFSETS.items():
  if kind=='R':continue
  for x,y in cells:
   for u,v in offsets:
    t=G.tile(kind,x-u,y-v)
    if set(t[1])<=cells:tiles.add(t)
 tiles=sorted(tiles);ri=[];cj=[]
 for j,t in enumerate(tiles):
  for p in t[1]:ri.append(index[p]);cj.append(j)
 A=csc_matrix((np.ones(len(ri)),(ri,cj)),shape=(len(cc),len(tiles)));original=set(original)
 res=milp(np.array([0 if t in original else 1 for t in tiles],dtype=float),integrality=np.ones(len(tiles)),bounds=Bounds(0,1),constraints=LinearConstraint(A,1,1),options={'time_limit':limit})
 if res.x is None:return None
 out=tuple(t for t,x in zip(tiles,res.x)if x>.5);G.check_partition(out,cells);return out

def find(k,m,rad):
 # q=3k+2 first-endpoint setting: the later upper vacancy cells are NOT holes.
 states,stones,holes=beforelower(k,m,2);c=m+2*k-3;b=-k-1
 oldhole={(c,b-3),(c,b-2),(c+1,b-4),(c-3,b),(c-2,b),(c-3,b+1)}
 assert oldhole<=holes
 target={(m+2*k-4,2*k-1),(m+2*k-3,2*k-1),(m+2*k-3,2*k)}
 xlo=min(x for x,y in oldhole|target)-rad;xhi=max(x for x,y in oldhole|target)+rad
 ylo=min(y for x,y in oldhole|target)-rad;yhi=max(y for x,y in oldhole|target)+rad
 release={t for t in states if any(xlo<=x<=xhi and ylo<=y<=yhi for x,y in t[1])}
 support=set(G.incidence(release))|oldhole
 if not target<=support:return None
 out=cover(support-target,release)
 if not out:return None
 a=release-set(out);bb=set(out)-release
 # relative to c,b (q2, first pass)
 rel=lambda ts:[[kind,G.anchor((kind,cs))[0]-c,G.anchor((kind,cs))[1]-b]for kind,cs in sorted(ts)]
 return {'k':k,'anchor_q2':['m+2k-3','-k-1'],'old':rel(a),'new':rel(bb),'oldholes':[[x-c,y-b]for x,y in sorted(oldhole)],'newholes':[[x-c,y-b]for x,y in sorted(target)]}
if __name__=='__main__':
 for k in [3,2]:
  for rad in [1,2,3,4,5]:
   try:ans=find(k,3*k+4,rad)
   except AssertionError as e:print('pre-error',k,e);break
   print('k,rad,found',k,rad,bool(ans),flush=True)
   if ans:
    (ROOT/f'small-direct-{k}.json').write_text(json.dumps(ans,indent=2));print(json.dumps(ans));break
