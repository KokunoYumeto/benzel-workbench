from regular2 import G
from itertools import product
from collections import defaultdict

def moves(dx,dy,maxold=3):
 R0=G.tile('R',0,0);R1=G.tile('R',dx,dy);a=set(R0[1]);b=set(R1[1]);by={}
 for p in b-a:
  candidates=set()
  x,y=p
  for k in ['H','V','D']:
   for u,v in G.OFFSETS[k]:
    t=G.tile(k,x-u,y-v)
    if not(set(t[1])&a):candidates.add(t)
  by[p]=sorted(candidates)
 out=[]
 for picks in product(*by.values()):
  A=set(picks)
  if len(A)>maxold:continue
  cnt=G.incidence(A)
  if any(n!=1 for n in cnt.values()):continue
  U=a|set(cnt)
  if not b<=U:continue
  C=U-b
  def solve(rem):
   if not rem:return ()
   p=min(rem)
   for kind in ['H','V','D']:
    for u,v in G.OFFSETS[kind]:
     t=G.tile(kind,p[0]-u,p[1]-v)
     if set(t[1])<=rem:
      x=solve(rem-set(t[1]))
      if x is not None:return (t,)+x
   return None
  B=solve(C)
  if B is not None:out.append((tuple(sorted(A)),tuple(sorted(B))))
 return sorted(set(out),key=lambda z:len(z[0]))
if __name__=='__main__':
 for xy in [(1,1),(2,-1),(-1,2),(1,0)]:
  out=moves(*xy);print('shift',xy,'n',len(out))
  for A,B in out[:3]:print(' old',G.encode_anchors(A),'new',G.encode_anchors(B))
