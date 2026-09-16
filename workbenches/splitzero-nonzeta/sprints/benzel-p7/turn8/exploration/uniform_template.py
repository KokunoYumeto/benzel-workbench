from regular2 import G,P
from collections import Counter,defaultdict

def corner_new(k):
 T=[]
 # Horizontal caps
 T += [G.tile('H',2+3*j,2)for j in range(k-1)]
 T += [G.tile('H',y+3*j,y)for y in range(3,k+1)for j in range(k-y+1)]
 T += [G.tile('H',3+2*r+3*j,1-r)for r in range(k-1)for j in range(k-1-r)]
 # Diagonal blocks
 T += [G.tile('D',1-k+3*j,4-k-3*j)for j in range(k)]
 for n in range(1,k):
  for j in range(n):
   x=2-n+3*j
   T += [G.tile('D',x,4-2*n-x),G.tile('D',x,5-2*n-x)]
 # Vertical blocks
 T += [G.tile('V',-2*k+1+i,k-2*i+3*j)for i in range(k)for j in range(k)]
 T += [G.tile('V',1-k,5-k+3*j)for j in range(k-1)]
 T += [G.tile('V',2-k+i,4-k+i+3*j)for i in range(k-1)for j in range(k-1-i)]
 T += [G.tile('V',x,2-3*k-2*x)for x in range(1-k,0)]
 for i in range(k):
  T += [G.tile('V',2*i,3-3*k-i),G.tile('V',2*i+1,2-3*k-i)]
 for i in range(1,k-1):
  for j in range(i):T += [G.tile('V',2*i+2,2-4*i+3*j),G.tile('V',2*i+3,1-4*i+3*j)]
 T += [G.tile('V',2*k,6-4*k+3*j)for j in range(k-1)]
 return T

def new_bones(m,k):
 G.require(type(k)is int and k>=1 and m>=3*k+2,'m>=3k+2')
 out=[]
 for l in range(k):
  for y in range(1-m+k-l,1-2*k):
   out.extend(G.rotate_tile(G.tile('H',y+m+3*l,y),p)for p in range(3))
 for t in corner_new(k):
  knd,cc=t;t=(knd,tuple(sorted((x,y-m)for x,y in cc)))
  out.extend(G.rotate_tile(t,p)for p in range(3))
 return tuple(out)

def deleted(m,k):return tuple(G.rotate_tile(G.tile('R',m-2-a,-a),p)for a in range(k)for p in range(3))
def recover(m,k):
 q=3*k;delta=G.triangular(m)-q;B=new_bones(m,k);Del=deleted(m,k)
 c=G.incidence(B);dc=G.incidence(Del)
 for p,n in dc.items():c[p]-=n
 M=set(p for j in range(q)for p in G.orbit((q-j,q+1-m-j)))
 for p in M:c[p]+=1
 if any(v not in(0,1)for v in c.values()):return False,('coeff',next((p,n)for p,n in c.items()if n not in(0,1)))
 cells={p for p,n in c.items()if n};owners={}
 for p in cells:
  o=P.stable_owner(delta,p)
  if o is None:return False,('NoOwner',p)
  label=o[:3];owners[label]=o[3]
 A=list(owners.values())
 if G.incidence(A)!=Counter({p:1 for p in cells}):return False,('NotWholeBones',len(cells),len(A)*3)
 return True,(A,B,sorted(owners))
if __name__=='__main__':
 import json,sys
 from pathlib import Path
 for k in range(1,21):
  for m in [3*k+2,4*k+7,8*k+11]:
   ok,out=recover(m,k)
   if not ok:print('FAILED',k,m,out,flush=True);break
   A,B,labels=out
   print('PASS',k,m,len(A),len(B),flush=True)
   if m==3*k+2:
    Path(f'/mnt/data/benzel-p7-turn8/turn8/exploration/uniform-template-{k}.json').write_text(json.dumps({'m':m,'k':k,'labels':labels}))
  if not ok:break
