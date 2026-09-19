"""Original q=3k+2 positive tilings: k>=4, m>=3k+4, d>=m."""
from pathlib import Path
import sys,json
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'turn8'))
import geometry as G,packing as P,construction as C
import source10 as S
ROOT=Path(__file__).resolve().parent
def shift(t,s):return t[0],tuple(sorted((x+s[0],y+s[1])for x,y in t[1]))
def common_labels(k,m):
 q=3*k+2
 for p in range(3):
  for y in range(1,m+q+1):
   rr=m-1 if y<=q else m
   for ell in range(min(y,q)):
    yield p,y,ell,G.reflect_tile(G.rotate_tile(G.tile('H',y-rr-2-3*ell,y),p))
def retained(k,m):
 base=set(C.retained_stones(m,k));extra={G.rotate_tile(G.tile('R',m-2-k,-k),p)for p in(0,2)}
 G.require(len(extra)==2 and extra<=base,'Extra source stones missing')
 return tuple(shift(t,(-1,-1))for t in sorted(base-extra))
def affine(v,m,k,i=0):return v[0]*m+v[1]*k+v[2]*i+v[3]
def expand(row,m,k,i=0):return G.tile(row[0],affine(row[1],m,k,i),affine(row[2],m,k,i))
def stages(k,m):
 G.require(type(k)is int and type(m)is int and k>=4 and m>=3*k+4,'Use integers k>=4,m>=3k+4')
 for g in json.loads((ROOT/'edits.json').read_text()):
  a,b,c=g['count'];n=a*m+b*k+c;G.require(n>=0,'Negative family length')
  for i in range(n):yield g['name'],i,tuple(expand(r,m,k,i)for r in g['old']),tuple(expand(r,m,k,i)for r in g['new'])
def initial(k,m):
 common=tuple(t for *_,t in common_labels(k,m));a0={t for *_,t in S.labels(m,k)}
 G.require(a0<=set(common),'Initial source outside common labels')
 B=tuple(shift(t,(-1,-1))for t in C.new_bones(m,k))
 states=Counter(set(common)-a0);states.update(B)
 return common,states,retained(k,m)
def core(k,m,check=True):
 common,states,stones=initial(k,m)
 if check:G.check_partition(tuple(states.elements())+stones, (G.omega(G.triangular(m)-3*k-2)|set(G.incidence(common)))-S.residual(m,k))
 for name,i,old,new in stages(k,m):
  for t in old:
   G.require(states[t]==1,f'Original source missing at {name}/{i}: {t}')
   states[t]-=1
  states.update(new)
  G.require(all(n>=0 for n in states.values()),'Negative intermediate tile coefficient')
 bones=tuple(states.elements())
 if check:G.check_partition(bones+stones,G.omega(G.triangular(m)-3*k-2)|set(G.incidence(common)))
 return common,bones,stones
def complete(d,m,k,check=True):
 G.require(type(d)is int and type(m)is int and type(k)is int and k>=4 and d>=m>=3*k+4,'Original domain')
 q=3*k+2;h=G.triangular(d)-G.triangular(m)+q
 old,bones,stones=core(k,m,check);outer=set(P.packing(d,h));G.require(set(old)<=outer,'Receiving source inclusion failed')
 out=tuple(sorted(outer-set(old)))+bones+stones
 if check:G.check_partition(out,G.region(d,h))
 return out
