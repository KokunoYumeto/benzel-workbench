from channel_residues import *
from collections import defaultdict
import heapq

def force(C,kinds='VD'):
 rem=set(C);T=[];by=defaultdict(set)
 for x,y in sorted(C):
  for kind in kinds:
   t=G.tile(kind,x,y)
   if set(t[1])<=C:
    i=len(T);T.append(t)
    for p in t[1]:by[p].add(i)
 active=set(range(len(T)));Q=[p for p in C if len(by[p])<=1];heapq.heapify(Q);out=[]
 while Q:
  p=heapq.heappop(Q)
  if p not in rem:continue
  if not by[p]:return out,rem,False
  if len(by[p])>1:continue
  i=next(iter(by[p]));t=T[i];out.append(t)
  dead=set().union(*(by[z]for z in t[1]));rem-=set(t[1])
  for j in dead:
   if j not in active:continue
   active.remove(j)
   for z in T[j][1]:
    by[z].remove(j)
    if z in rem and len(by[z])<=1:heapq.heappush(Q,z)
 return out,rem,True

if __name__=='__main__':
 for k in range(1,21):
  m=30*k+10;data,info=setup_channel(k,1,m);rem,A,S,old=data
  center=(0,1-m);radius=8*k+6
  dist=lambda z:max(abs(z[0]),abs(z[1]-center[1]),abs(sum(z)-center[1]))
  holes={z for z in rem if dist(z)<=radius}
  cap=[G.tile('H',3*k-2+j,2-j-m)for j in range(3)]
  R=rem|set(G.incidence(old));cc=set(G.incidence(cap))
  if not cc<=R:print(k,'Hout');continue
  take={t for t in old if (t[0]=='V'and any(dist(z)<=radius for z in t[1]))or set(t[1])&cc}
  C0=holes|set(G.incidence(take));target=C0-cc
  F,left,ok=force(target)
  print(k,'old',len(take),'holes',len(holes),'F',len(F),'left',len(left),'ok',ok,flush=True)
  if ok and not left:
   new=F+cap;G.check_partition(new,C0)
   (ROOT/'exploration'/f'forced-r1p0-{k}.json').write_text(json.dumps({'k':k,'m':m,'remove':G.encode_anchors(take-set(new)),'add':G.encode_anchors(set(new)-take)}))
