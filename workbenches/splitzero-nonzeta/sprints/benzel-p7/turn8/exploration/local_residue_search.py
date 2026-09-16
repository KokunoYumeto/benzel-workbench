from remainder_residues import *
from collections import defaultdict
import heapq

def exact_cells(cells,cap=100000):
 cells=set(cells);ps=sorted(cells);idx={p:i for i,p in enumerate(ps)};T=[];by=[[]for _ in ps];masks=[]
 for x,y in ps:
  for kind in ['H','V','D']:
   t=G.tile(kind,x,y)
   if set(t[1])<=cells:
    z=len(T);T.append(t);mask=sum(1<<idx[p]for p in t[1]);masks.append(mask)
    for p in t[1]:by[idx[p]].append(z)
 nodes=0;bad=set()
 def rec(rem):
  nonlocal nodes
  nodes+=1
  if nodes>cap:raise TimeoutError
  if not rem:return ()
  if rem in bad:return None
  mm=rem;best=None
  while mm:
   b=mm&-mm;mm-=b;i=b.bit_length()-1
   cand=[j for j in by[i]if rem&masks[j]==masks[j]]
   if not cand:bad.add(rem);return None
   if best is None or len(cand)<len(best):best=cand
   if len(cand)==1:break
  for j in best:
   ans=rec(rem^masks[j])
   if ans is not None:return (j,)+ans
  bad.add(rem);return None
 try:ids=rec((1<<len(ps))-1)
 except TimeoutError:return None,'CAP'
 if ids is None:return None,'EXHAUSTED'
 out=tuple(T[j]for j in ids);G.check_partition(out,cells);return out,'POSITIVE'

if __name__=='__main__':
 for k in range(1,5):
  for r in [1,2]:
   m=30*k+10;rem,A,S,B,info=setup(k,r,m)
   print(k,r,info['components'],flush=True)
   for i,c in enumerate(components(rem)):
    ts,status=exact_cells(c)
    print(i,status,sorted(c),G.encode_anchors(ts)if ts else'')
