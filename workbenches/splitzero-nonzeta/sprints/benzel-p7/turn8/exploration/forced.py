from regular3 import calc
from regular2 import G,solve_cells
from collections import defaultdict,Counter
import sys,json

def forced(C):
 R=set(C);chosen=[]
 while R:
  by=defaultdict(list)
  for x,y in R:
   for kind in ['H','V','D']:
    t=G.tile(kind,x,y)
    if set(t[1])<=R:
     for p in t[1]:by[p].append(t)
  bad=next((p for p in R if not by[p]),None)
  if bad is not None:return chosen,R,False
  t=next((by[p][0]for p in sorted(R)if len(by[p])==1),None)
  if t is None:return chosen,R,True
  chosen.append(t);R-=set(t[1])
 return chosen,R,True
if __name__=='__main__':
 for k in range(1,11):
  C,inf=calc(k);F,R,ok=forced(C)
  print(k,'core',len(R),'forced',len(F),Counter(t[0]for t in F),'ok',ok,flush=True)
  open(f'/mnt/data/benzel-p7-turn8/turn8/exploration/forced-{k}.json','w').write(json.dumps({'k':k,'forced':G.encode_anchors(F),'residual':sorted(R),'ok':ok}))
