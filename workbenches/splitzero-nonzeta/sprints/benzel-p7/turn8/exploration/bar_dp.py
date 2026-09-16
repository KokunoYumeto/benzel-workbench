from regular3 import calc
from regular2 import G
from uniform_corner import caps
from collections import defaultdict
import sys,time,json
from pathlib import Path
ROOT=Path('/mnt/data/benzel-p7-turn8/turn8/exploration')
def solve(C,W=2):
 rows=defaultdict(set)
 for x,y in C:rows[y].add(x)
 frontier={(frozenset(),frozenset()):()};counts=[]
 for y in range(min(rows),max(rows)+1):
  row=rows[y];edges=set()
  for x in row:
   if x-1 not in row or x+1 not in row:edges.update(range(x-W+1,x+W))
  nxt={}
  for (busy,nextbusy),path in frontier.items():
   stack=[(set(busy),set(nextbusy),set(),[])]
   while stack:
    b0,b1,b2,ts=stack.pop();empty=row-b0
    if not empty:
     key=(frozenset(b1),frozenset(b2))
     if key not in nxt:nxt[key]=path+tuple(ts)
     continue
    x=min(empty)
    opts=[('h',((x,y),(x+1,y),(x+2,y)))]
    if x in edges:opts.append(('v',((x,y),(x,y+1),(x,y+2))))
    for t in opts:
     lay=[set(),set(),set()];good=True
     for u,v in t[1]:
      z=v-y
      if u not in rows[v] or u in (b0,b1,b2)[z]:good=False;break
      lay[z].add(u)
     if good:stack.append((b0|lay[0],b1|lay[1],b2|lay[2],ts+[t]))
  frontier=nxt;counts.append((y,len(nxt)))
  if not frontier:return None,counts
 return frontier.get((frozenset(),frozenset())),counts
if __name__=='__main__':
 for k in map(int,sys.argv[1:]):
  C,inf=calc(k);H=caps(k);C-=set(G.incidence(H));bar={(x,x+y)for x,y in C}
  start=time.monotonic();B,count=solve(bar,3);print(k,B is not None,'max',max(n for y,n in count),'last',count[-1],'s',time.monotonic()-start,flush=True)
  if B:
   old=[(('D' if kind=='h' else 'V'),tuple(sorted((u,v-u)for u,v in cells)))for kind,cells in B];G.check_partition(old,C)
   (ROOT/f'bardp-{k}.json').write_text(json.dumps({'k':k,'tiles':G.encode_anchors(old+H),'counts':count}))
