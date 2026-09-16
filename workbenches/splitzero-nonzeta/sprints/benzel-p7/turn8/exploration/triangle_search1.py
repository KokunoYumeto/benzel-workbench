from regular2 import G
from collections import defaultdict
from pathlib import Path
import json,time
ROOT=Path('/mnt/data/benzel-p7-turn8/turn8/exploration')
Rs={k:set(map(tuple,json.loads((ROOT/f'forced-{k}.json').read_text())['residual']))for k in range(2,11)}
def top(k):return [G.tile('H',2+3*j,2)for j in range(k-1)]+[G.tile('H',y+3*j,y)for y in range(3,k+1)for j in range(k-y+1)]
Cs={k:Rs[k]-set(G.incidence(top(k)))for k in Rs}
def exact(C,cap=20000):
 cells=sorted(C);idx={p:i for i,p in enumerate(cells)};ts=[];by=[[]for _ in cells];masks=[]
 for x,y in cells:
  for kind in ['V','D']:
   t=G.tile(kind,x,y)
   if set(t[1])<=C:
    mask=sum(1<<idx[p]for p in t[1]);i=len(ts);ts.append(t);masks.append(mask)
    for p in t[1]:by[idx[p]].append(i)
 failed=set();nodes=0
 def dfs(rem):
  nonlocal nodes
  nodes+=1
  if nodes>cap:raise TimeoutError
  if not rem:return ()
  if rem in failed:return None
  mm=rem;best=None
  while mm:
   b=mm&-mm;i=b.bit_length()-1;mm-=b
   cand=[j for j in by[i]if masks[j]&rem==masks[j]]
   if not cand:failed.add(rem);return None
   if best is None or len(cand)<len(best):best=cand
   if len(best)==1:break
  for j in best:
   sub=dfs(rem^masks[j])
   if sub is not None:return (j,)+sub
  failed.add(rem);return None
 try:ids=dfs((1<<len(cells))-1)
 except TimeoutError:return None
 if ids is None:return None
 B=[ts[i]for i in ids];G.check_partition(B,C);return B

def tri(k,x,y,u,v):return [G.tile('H',x+u*r+3*j,y+v*r)for r in range(k-1)for j in range(k-1-r)]
def test(k,x,y,u,v,cap=5000):
 T=tri(k,x,y,u,v);cnt=G.incidence(T)
 if any(n!=1 for n in cnt.values())or not set(cnt)<=Cs[k]:return None
 return exact(Cs[k]-set(cnt),cap)
if __name__=='__main__':
 poss2=[]
 for x,y in sorted(Cs[2]):
  if test(2,x,y,0,1) is not None:poss2.append((x,y))
 print('possible2',poss2,flush=True)
 passes=[];start=time.monotonic();done=0
 for x,y in sorted(Cs[3]):
  for u in range(-4,7):
   for v in [-3,-2,-1,1,2,3]:
    T=tri(3,x,y,u,v);cnt=G.incidence(T)
    if any(n!=1 for n in cnt.values())or not set(cnt)<=Cs[3]:continue
    rr=Cs[3]-set(cnt);cc=[sum(z%3==r for a,z in rr)for r in range(3)]
    if len(set(cc))>1:continue
    done+=1
    if exact(rr,5000) is None:continue
    for x2,y2 in poss2:
     a=x-x2;c=y-y2;b=x-3*a;d=y-3*c
     if all(test(k,a*k+b,c*k+d,u,v,30000)is not None for k in range(4,7)):
      par=(a,b,c,d,u,v);print('PASS6',par,flush=True);passes.append(par)
 print('trials',done,'passes',passes,'s',time.monotonic()-start)
 (ROOT/'triangle-formulas1.json').write_text(json.dumps(passes))
