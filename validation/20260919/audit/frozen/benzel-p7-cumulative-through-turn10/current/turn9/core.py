"""Original positive q=3k+1 repair: k>=4, m>=3k+3, d>=m.

Every removal names a source generator; no search, fitting or optimizer is used.
The source table, Laurent identity and exact affine receipts are independent checks.
"""
from __future__ import annotations
from pathlib import Path
import sys
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'turn8'))
import geometry as G,packing as P,construction as C,families
import source_table as S

def shift(t,s):return t[0],tuple(sorted((x+s[0],y+s[1])for x,y in t[1]))
LOW_OLD=[('H',-1,0),('H',2,3),('V',-2,1),('V',-1,1),('V',-1,4),('V',0,2),('V',0,5),('V',1,-3),('V',1,3),('V',2,-5),('V',2,-2),('V',3,-4),('V',4,-3),('V',4,0)]
LOW_NEW=[('D',0,-3),('D',0,-2),('D',1,-2),('D',1,-1),('D',2,-1),('H',-3,0),('H',-3,1),('H',-2,2),('H',-2,3),('H',-1,4),('H',-1,5),('H',0,0),('H',1,3),('V',4,-2),('V',4,1)]
UP_OLD=[('H',0,2),('H',0,3),('V',3,2)]
UP_NEW=[('H',-1,3),('H',1,2),('V',-1,0),('V',0,0),('V',2,3),('V',3,3)]
P0_OLD=[('V',1,0),('V',2,-2),('V',3,-1),('V',4,0)]
P0_NEW=[('D',0,0),('D',0,1),('D',1,1),('D',3,3),('H',1,2),('H',2,1),('H',3,0)]

def move(kind,x,y):
 if kind=='D':return [('V',x+1,y),('V',x+2,y-2)],[('D',x,y),('D',x,y+1)]
 if kind=='U':return [('V',x,y+2),('V',x+1,y)],[('V',x,y),('V',x+1,y-1)]
 if kind=='R':return [('H',x+2,y),('H',x+1,y+1)],[('H',x,y),('H',x,y+1)]
 if kind=='B':return [('V',x,y+1),('V',x+1,y+2)],[('V',x,y),('V',x+1,y)]
 raise ValueError('Unknown original move')
def trans(rows,x,y):return [(kind,x+a,y+b)for kind,a,b in rows]
def as_tiles(rows):return tuple(G.tile(*r)for r in rows)

def stages(k,m):
 G.require(type(k)is int and type(m)is int and k>=4 and m>=3*k+3,'Original parameter domain')
 length=m-3*k-3
 old=[('V',3*k+2+j,j-m)for j in range(length+1)]+[('V',3*k+2+j,j+3-m)for j in range(length)]
 new=[('D',3*k+1+j,3-m+j+b)for j in range(length)for b in[0,1]]
 yield 'channel',0,as_tiles(old),as_tiles(new)
 for i in range(k-1):yield 'p0D',i,*map(as_tiles,move('D',2*k-2+i,4-4*k-m+i))
 for i in range(k-1):yield 'p0U',i,*map(as_tiles,move('U',3*k-3,3-3*k-m+3*i))
 yield'p0T',0,as_tiles(trans(P0_OLD,3*k-3,-m)),as_tiles(trans(P0_NEW,3*k-3,-m))
 for i in range(2*k-2):yield'p2D',i,*map(as_tiles,move('D',m-2+i,-3*k+i))
 for i in range(k-1):yield'p2R',i,*map(as_tiles,move('R',m-k-4+3*i,1-k))
 x,y=m+2*k-4,1-k
 yield'lower',0,as_tiles(trans(LOW_OLD,x,y)),as_tiles(trans(LOW_NEW,x,y))
 for i in range(k-4):yield'beta',i,*map(as_tiles,move('B',x-1,y+6+3*i))
 yield'upper',0,as_tiles(trans(UP_OLD,x,2*k-5)),as_tiles(trans(UP_NEW,x,2*k-5))

def common_labels(k,m):
 q=3*k+1
 for p in range(3):
  for y in range(1,m+q+1):
   rr=m-1 if y<=q else m
   for ell in range(min(y,q)):
    yield p,y,ell,G.reflect_tile(G.rotate_tile(G.tile('H',y-rr-2-3*ell,y),p))
def retained(k,m):
 old=C.retained_stones(m,k);extra=G.tile('R',m-2-k,-k)
 G.require(extra in old,'Original extra deleted stone')
 return tuple(shift(t,(-2,1))for t in old if t!=extra)
def initial(k,m):
 labels=list(common_labels(k,m));common={t for p,y,l,t in labels};a0={t for p,y,l,t in S.labels(m,k)}
 G.require(a0<=common,'Source table outside original common bands')
 bs=tuple(shift(t,(-2,1))for t in C.new_bones(m,k));states=Counter(common-a0);states.update(bs)
 G.require(all(v==1 for v in states.values()),'Initial duplicate original generator')
 return common,states,retained(k,m)
def core(k,m,check=True):
 common,states,stones=initial(k,m)
 for name,i,old,new in stages(k,m):
  for t in old:
   G.require(states[t]==1,f'Missing source at {name} {i}: {t}')
   states[t]-=1
  states.update(new)
  G.require(all(n in(0,1)for n in states.values()),'Repeated tile generator in repair')
 bones=tuple(t for t,n in states.items()if n)
 if check:G.check_partition(bones+stones,G.omega(G.triangular(m)-3*k-1)|set(G.incidence(common)))
 return tuple(common),bones,stones

def complete(d,m,k,check=True):
 G.require(type(d)is int and d>=m,'Original exterior parameter')
 q=3*k+1;delta=G.triangular(m)-q;h=G.triangular(d)-delta
 old,bones,stones=core(k,m,check)
 packing=set(P.packing(d,h));G.require(set(old)<=packing,'Original source-to-tail receiving map')
 out=tuple(packing-set(old))+bones+stones
 if check:G.check_partition(out,G.region(d,h))
 return out
