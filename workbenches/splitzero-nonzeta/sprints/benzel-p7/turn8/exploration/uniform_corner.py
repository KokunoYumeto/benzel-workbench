from regular3 import calc
from regular2 import G
from triangle_search import exact
from forcefast import force
from collections import Counter,defaultdict
from pathlib import Path
import json,sys,time,heapq
ROOT=Path('/mnt/data/benzel-p7-turn8/turn8/exploration')
def caps(k):
 out=[G.tile('H',2+3*j,2)for j in range(k-1)]+[G.tile('H',y+3*j,y)for y in range(3,k+1)for j in range(k-y+1)]
 out += [G.tile('H',3+2*r+3*j,1-r)for r in range(k-1)for j in range(k-1-r)]
 return out

def force_vd(C):
 remaining=set(C);by=defaultdict(set);tiles=[]
 for x,y in sorted(C):
  for kind in ['V','D']:
   t=G.tile(kind,x,y)
   if set(t[1])<=C:
    i=len(tiles);tiles.append(t)
    for p in t[1]:by[p].add(i)
 active=set(range(len(tiles)));heap=[p for p in C if len(by[p])<=1];heapq.heapify(heap);out=[]
 while heap:
  p=heapq.heappop(heap)
  if p not in remaining:continue
  if not by[p]:return out,remaining,False
  if len(by[p])>1:continue
  i=next(iter(by[p]));t=tiles[i];out.append(t)
  deletes=set().union(*(by[p]for p in t[1]));remaining-=set(t[1])
  for k in deletes:
   if k not in active:continue
   active.remove(k)
   for p in tiles[k][1]:
    by[p].remove(k)
    if p in remaining and len(by[p])<=1:heapq.heappush(heap,p)
 return out,remaining,True
if __name__=='__main__':
 for k in map(int,sys.argv[1:]):
  C,inf=calc(k);H=caps(k);cov=G.incidence(H);G.require(not cov or max(cov.values())==1,'Caps overlap');G.require(set(cov)<=C,'Caps outside')
  F,R,ok=force_vd(C-set(cov));print(k,'caps',len(H),'forcedVD',len(F),'remaining',len(R),'ok',ok,flush=True)
  if ok:
   B=exact(R,500000)if R else[]
   if B is not None:
    ts=H+F+B;G.check_partition(ts,C)
    (ROOT/f'uniform-{k}.json').write_text(json.dumps({'k':k,'tiles':G.encode_anchors(ts),'types':dict(Counter(t[0]for t in ts)),'forcing_complete':not R}))
