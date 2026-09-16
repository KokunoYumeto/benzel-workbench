from uniform_template import *
from collections import defaultdict,Counter

def counts(A,B):
 owner=defaultdict(list);adj=[set()for _ in range(len(A)+len(B))];marked=set()
 for i,t in enumerate(A+tuple(B) if isinstance(A,tuple) else list(A)+list(B)):
  for p in t[1]:owner[p].append(i)
 for p,ns in owner.items():
  if len(ns)==1:marked.update(ns)
  elif len(ns)==2:
   a,b=ns;adj[a].add(b);adj[b].add(a)
  else:raise ValueError('not matchings')
 todo=set(range(len(adj)));closed=[];open_=[]
 while todo:
  i=todo.pop();cc={i};stack=[i]
  while stack:
   i=stack.pop()
   for j in adj[i]:
    if j in todo:todo.remove(j);cc.add(j);stack.append(j)
  (open_ if cc&marked else closed).append(cc)
 return len(closed),len(open_),Counter(len(c)for c in closed),Counter(len(c)for c in open_)
if __name__=='__main__':
 for k in range(1,11):
  for m in [3*k+2,3*k+3,6*k+7]:
   ok,(A,B,l)=recover(m,k);print(k,m,len(A),counts(A,B),flush=True)
