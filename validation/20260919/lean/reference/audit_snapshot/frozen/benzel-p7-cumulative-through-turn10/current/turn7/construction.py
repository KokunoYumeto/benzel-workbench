"""Full original benzel tilings from certified corner-deletion templates.

No optimizer is used by these constructors. The source-to-tail comparison
makes each template available even at its smallest exterior parameter d=m.
"""
from __future__ import annotations
from pathlib import Path
import json
import geometry as G,parent_construction as P

ROOT=Path(__file__).resolve().parent


def specifications():return json.loads((ROOT/'templates.json').read_text())


def spec(q):
    G.require(type(q)is int and str(q)in specifications(),'Unsupported certified corner-deletion count')
    return specifications()[str(q)]


def parameters(m,q):
    s=spec(q);G.require(type(m)is int and m>=s['m_min'],'Outside the certified original parameter domain')
    return s,G.triangular(m)-q


def source_labels(m,q):
    s,delta=parameters(m,q);out=[]
    for p,depth,ym,y0,nm,n0 in s['source_families']:
        for j in range(nm*m+n0):
            y=ym*m+y0+j
            G.require(1<=y<=m+q and 0<=depth<min(y,q),'Original common-body label outside range')
            r=m-1 if y<=q else m
            G.require(G.block(y+delta)==r,'Triangular inverse changed branch')
            x=y-r-2-3*depth
            tile=G.reflect_tile(G.rotate_tile(G.tile('H',x,y),p))
            out.append((p,y,depth,tile))
    return tuple(out)


def source(m,q):
    out=tuple(z[3]for z in source_labels(m,q))
    G.require(len(out)==len(set(out)),'Repeated original source tile')
    return out


def deleted(m,q):
    s,_=parameters(m,q);sx,sy=s['shift'];out=[]
    for i in range(q):
        a,p=divmod(i,3);t=G.rotate_tile(G.tile('R',m-2-a,-a),p)
        out.append(('R',tuple(sorted((x+sx,y+sy)for x,y in t[1]))))
    return tuple(out)


def stones(m,q):
    s,_=parameters(m,q);sx,sy=s['shift']
    ts=tuple(('R',tuple(sorted((x+sx,y+sy)for x,y in t[1])))for t in P.base_stones(m))
    rem=set(deleted(m,q));G.require(len(rem)==q and rem<=set(ts),'Corner-chain source mismatch')
    return tuple(t for t in ts if t not in rem)


def bones(m,q):
    s,_=parameters(m,q);out=[]
    for kind,xm,xj,x0,ym,yj,y0,nm,n0 in s['bone_families']:
        N=nm*m+n0;G.require(N>=0,'Negative original index range')
        out.extend(G.tile(kind,xm*m+xj*j+x0,ym*m+yj*j+y0)for j in range(N))
    return tuple(out)


def patch(m,q):return stones(m,q)+bones(m,q)


def common_body(m,q):
    G.require(type(m)is int and type(q)is int and 1<=q<=m-2,'Original common-body domain')
    out=[]
    for y in range(1,m+q+1):
        for depth in range(min(y,q)):
            r=m-1 if y<=q else m
            t=G.tile('H',y-r-2-3*depth,y)
            out.extend(G.reflect_tile(G.rotate_tile(t,p))for p in range(3))
    return tuple(out)


def terminal_fans(m,q):
    """The original finite tail beyond the common body; all tiles retained."""
    G.require(type(m)is int and type(q)is int and 1<=q<=m-2,'Original terminal-fan domain')
    out=[]
    for ell in range(1,q):
        y=m+q+ell
        for j in range(q-ell):
            t=G.tile('H',ell-2*q+1+3*j,y)
            out.extend(G.reflect_tile(G.rotate_tile(t,p))for p in range(3))
    return tuple(out)


def embedding_index(d,m,q,p,y,depth):
    """Both original finite index roles, without treating the tail as a prefix."""
    _,delta=parameters(m,q);G.require(type(d)is int and d>=m,'Exterior parameter too small')
    h=G.triangular(d)-delta
    if d==m and y>q:
        j=q-1-depth;L=y-3*q-m+1;kind='finite_tail'
    else:
        G.require(y<=h,'Original prefix not yet available')
        j=y-1-depth;L=1-2*y-G.block(y+delta);kind='stable_prefix'
    G.require(j>=0,'Negative receiving generator index')
    t=G.reflect_tile(G.rotate_tile(G.tile('H',L+3*j,y),p))
    return kind,j,t


def complete(d,m,q):
    _,delta=parameters(m,q);G.require(type(d)is int and d>=m,'Use d>=m')
    h=G.triangular(d)-delta;old=P.packing(d,h);A=set(source(m,q))
    G.require(A<=set(old),'Original source inclusion failed')
    return tuple(t for t in old if t not in A)+patch(m,q)
