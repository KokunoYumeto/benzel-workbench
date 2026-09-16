import sys
sys.path.insert(0,'/mnt/data/benzel-p7-turn7/turn7')
import geometry as G,parent_construction as P

def build(m,k):
 q=3*k;delta=G.triangular(m)-q
 G.require(m>=q+2,'range')
 A=[]
 for y in range(1,m+q+1):
  r=m-1 if y<=q else m
  for dep in range(min(y,k)):
   t=G.tile('H',y-r-2-3*dep,y)
   A.extend(G.reflect_tile(G.rotate_tile(t,p))for p in range(3))
 holes=set(p for n in range(q)for p in G.orbit((q-n,q+1-m-n)))
 removed=set(G.rotate_tile(G.tile('R',m-2-a,-a),p)for a in range(k)for p in range(3))
 stones=set(P.base_stones(m))-removed
 target=(set(G.omega(delta))|{p for t in A for p in t[1]})-{p for t in stones for p in t[1]}
 G.require(len(target)==3*len(A),'count')
 return target,A,stones

if __name__=='__main__':
 for k in range(1,7):
  m=60;R,A,S=build(m,k)
  print('k',k,'size',len(R))
  for ell in range(k):
   ys=[y for y in range(-m-3*k,m+3*k)if set(G.tile('H',y+m+3*ell,y)[1])<=R]
   intervals=[]
   for y in ys:
    if intervals and intervals[-1][-1]==y-1:intervals[-1].append(y)
    else:intervals.append([y])
   print(' ell',ell,[(x[0],x[-1])for x in intervals])
