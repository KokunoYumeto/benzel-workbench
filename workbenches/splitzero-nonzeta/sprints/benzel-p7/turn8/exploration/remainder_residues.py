import sys,json,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import construction as C,geometry as G,packing as P
from collections import Counter,defaultdict

def common(m,q):
 out=[]
 for y in range(1,m+q+1):
  r=m-1 if y<=q else m
  for ell in range(min(y,q)):
   t=G.tile('H',y-r-2-3*ell,y)
   out.extend(G.reflect_tile(G.rotate_tile(t,p))for p in range(3))
 return out

def shift(t,s):return(t[0],tuple(sorted((x+s[0],y+s[1])for x,y in t[1])))

def fixed_stones(m,q):
 s={0:(0,0),1:(-2,1),2:(-1,-1)}[q%3]
 base={shift(t,s)for t in P.base_stones(m)}
 rem={shift(G.rotate_tile(G.tile('R',m-2-a,-a),p),s)for a,p in(map(lambda j:divmod(j,3),range(q)))}
 G.require(rem<=base,'Deleted stone absent')
 return base-rem

def components(cells):
 rem=set(cells);out=[]
 while rem:
  seed=next(iter(rem));comp={seed};rem.remove(seed);Q=[seed]
  while Q:
   x,y=Q.pop()
   for p in [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y-1),(x-1,y+1)]:
    if p in rem:rem.remove(p);comp.add(p);Q.append(p)
  out.append(comp)
 return sorted(out,key=lambda c:(-len(c),min(c)))

def setup(k,r,m,margin=0):
 q=3*k+r;s={1:(-2,1),2:(-1,-1)}[r];A=common(m,q)
 R=set(G.omega(G.triangular(m)-q))|set(G.incidence(A))
 stones=fixed_stones(m,q);G.require(set(G.incidence(stones))<=R,'Retained stone outside source')
 R-=set(G.incidence(stones))
 shifted=[shift(t,s)for t in C.new_bones(m,k)]
 B=[t for t in shifted if set(t[1])<=R];used=set(G.incidence(B))
 centers=[G.rho((0,1-m)),G.rho(G.rho((0,1-m))),(0,1-m)]
 def near(t):return any(max(abs(x-cx),abs(y-cy),abs(x+y-cx-cy))<=margin*k for x,y in t[1]for cx,cy in centers)
 keep=[t for t in A if set(t[1])<=R and not set(t[1])&used and not near(t)]
 used|=set(G.incidence(keep));rem=R-used
 return rem,A,stones,B+keep,{'k':k,'r':r,'m':m,'margin':margin,'old':len(A),'shift_B':len(B),'cut':len(shifted)-len(B),'residual':len(rem),'components':[len(c)for c in components(rem)]}

if __name__=='__main__':
 for k in range(1,5):
  for r in [1,2]:
   m=30*k+10
   rem,A,S,B,info=setup(k,r,m);print(info,flush=True)
   (ROOT/'exploration'/f'residue-{k}-{r}.json').write_text(json.dumps({'info':info,'residual':sorted(rem),'fixed':G.encode_anchors(B)}))
