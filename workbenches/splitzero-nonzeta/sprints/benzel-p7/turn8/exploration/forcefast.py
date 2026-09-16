from regular3 import calc
from regular2 import G,solve_cells
from collections import defaultdict
import heapq,json
from pathlib import Path
ROOT=Path('/mnt/data/benzel-p7-turn8/turn8/exploration')

def force(C):
 remaining=set(C);by=defaultdict(set);tiles=[]
 for x,y in sorted(C):
  for kind in ['H','V','D']:
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
  removes=set().union(*(by[p]for p in t[1]));remaining-=set(t[1])
  for k in removes:
   if k not in active:continue
   active.remove(k)
   for p in tiles[k][1]:
    by[p].remove(k)
    if p in remaining and len(by[p])<=1:heapq.heappush(heap,p)
 return out,remaining,True
if __name__=='__main__':
 for k in range(1,11):
  C,inf=calc(k);F,R,ok=force(C)
  print(k,len(C),len(R),len(F),ok,flush=True)
  (ROOT/f'forced-{k}.json').write_text(json.dumps({'k':k,'forced':G.encode_anchors(F),'residual':sorted(R),'ok':ok,'full':sorted(C)}))
