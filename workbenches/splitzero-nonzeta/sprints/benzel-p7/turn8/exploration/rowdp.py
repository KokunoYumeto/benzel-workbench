from regular3 import calc
from regular2 import G
from collections import defaultdict
import sys,time,json

def solve(C,W=3,maxstates=100000):
 rows=defaultdict(set)
 for x,y in C:rows[y].add(x)
 lo=min(rows);hi=max(rows)
 # state: occupied current row, next row; recover after every transition
 frontier={(frozenset(),frozenset()):()};counts=[]
 for y in range(lo,hi+1):
  row=rows[y]
  edges=set()
  for x in row:
   if x-1 not in row or x+1 not in row:
    edges.update(range(x-W+1,x+W))
  nxt={}
  for (busy,nextbusy),path in frontier.items():
   stack=[(set(busy),set(nextbusy),set(),[])]
   while stack:
    b0,b1,b2,tiles=stack.pop()
    empty=row-b0
    if not empty:
     key=(frozenset(b1),frozenset(b2))
     if key not in nxt:nxt[key]=path+tuple(tiles)
     continue
    x=min(empty)
    # restrict nonhorizontal start positions to boundary edges
    options=[G.tile('H',x,y)]
    if x in edges:options.extend([G.tile('V',x,y),G.tile('D',x-2,y+2)])
    for t in options:
     layers=[set(),set(),set()]
     good=True
     for u,v in t[1]:
      z=v-y
      if u not in rows[v] or u in (b0,b1,b2)[z]:good=False;break
      layers[z].add(u)
     if good:stack.append((b0|layers[0],b1|layers[1],b2|layers[2],tiles+[t]))
  frontier=nxt;counts.append([y,len(nxt)])
  if not frontier or len(frontier)>maxstates:return None,counts
 key=(frozenset(),frozenset());out=frontier.get(key)
 if out:G.check_partition(out,C)
 return out,counts
if __name__=='__main__':
 k,W=map(int,sys.argv[1:3]);C,inf=calc(k);start=time.monotonic();B,count=solve(C,W)
 print('k',k,'W',W,'pass',B is not None,'statesmax',max(n for y,n in count),'stopped',count[-1],'s',time.monotonic()-start,flush=True)
 if B:open(f'/mnt/data/benzel-p7-turn8/turn8/exploration/dp-{k}-{W}.json','w').write(json.dumps({'k':k,'W':W,'counts':count,'tiles':G.encode_anchors(B)}))
