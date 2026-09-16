from channel_residues import *
from repair_residues import solve_patch

def attempt2(k,r,m,radius,p):
 data,info=setup_channel(k,r,m)
 if data is None:return info
 rem,A,S,old=data;centers=[(0,1-m),(1-m,m),(m,0)];center=centers[p]
 def distance(z):x,y=z;return max(abs(x-center[0]),abs(y-center[1]),abs(x+y-center[0]-center[1]))
 holes={z for z in rem if distance(z)<=radius}
 take={t for t in old if any(distance(z)<=radius for z in t[1])}
 cells=holes|set(G.incidence(take))
 new,inf=solve_patch(cells,take,5)
 if new is not None:
  removed=take-set(new);added=set(new)-take
  d={'k':k,'r':r,'m':m,'p':p,'radius':radius,'info':inf,'holes':sorted(holes),'remove':G.encode_anchors(removed),'add':G.encode_anchors(added)}
  (ROOT/'exploration'/f'channel-repair-r{r}-k{k}-p{p}.json').write_text(json.dumps(d))
 return inf

if __name__=='__main__':
 import sys
 for k in list(map(int,sys.argv[1:]))or[1,2,3,4,5,6]:
  for r in [1,2]:
   for p in ([0,2]if r==1 else[0,1,2]):
    inf=attempt2(k,r,30*k+10,8*k+6,p)
    print(k,r,p,inf,flush=True)
