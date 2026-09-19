"""Exact all-parameter incidence certificates over Z[X±,Y±,U±,V±].

U and V specialize to X^m and Y^m. Every denominator is a nonzero Laurent
polynomial in X,Y alone.  Expansion and cancellation are exact integer
operations.  No evaluation at finitely many m is used to accept an identity.
"""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
import json
from pathlib import Path
import geometry as G
from pathlib import Path
import json

def specification(q):
    data=json.loads((Path(__file__).resolve().parent/"templates.json").read_text())
    G.require(str(q) in data,"Uncertified deletion count")
    return data[str(q)]

ZERO=(0,0,0,0)
Poly=dict[tuple[int,int,int,int],int]

def clean(a): return {v:n for v,n in a.items() if n}
def add(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,0)+v
    return clean(out)
def scale(a,n):return clean({k:v*n for k,v in a.items()})
def mul(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():
            k=tuple(u+v for u,v in zip(i,j));out[k]=out.get(k,0)+x*y
    return clean(out)
def mono(x=0,y=0,u=0,v=0):return {(x,y,u,v):1}
def pow_mono(v,k):return mono(*(a*k for a in v))
def factor(v):
    G.require(len(v)==4 and all(type(z)is int for z in v) and v!=ZERO and v[2:]==(0,0),'Denominator must be a nonzero original X,Y Laurent factor')
    return add(mono(),scale({v:1},-1))
def conv(k):return k[0],k[1],k[2],k[3]

@dataclass(frozen=True)
class Term:
    numerator: Poly
    factors: tuple=()

class Expression:
    def __init__(self,terms=()):self.terms=tuple(terms)
    def __add__(self,b):return Expression(self.terms+b.terms)
    def __neg__(self):return Expression(Term(scale(t.numerator,-1),t.factors)for t in self.terms)
    def __sub__(self,b):return self+-b
    def __mul__(self,b):return Expression(Term(mul(a.numerator,c.numerator),a.factors+c.factors)
                                          for a in self.terms for c in b.terms)
    def verify_zero(self):
        common=Counter()
        for t in self.terms:
            for f,n in Counter(t.factors).items():common[f]=max(common[f],n)
        out={};expanded_counts=[]
        for t in self.terms:
            a=t.numerator
            for f,n in (common-Counter(t.factors)).items():
                for _ in range(n):a=mul(a,factor(f))
            expanded_counts.append(len(a));out=add(out,a)
        G.require(not out,'Nonzero exact incidence coefficient: '+str(next(iter(out.items()),None)))
        return {'rational_terms':len(self.terms),'common_denominator_factors':
                [[list(f),n]for f,n in sorted(common.items())],
                'expanded_numerator_term_count_before_sum':sum(expanded_counts),
                'residual_numerator_terms':len(out)}
    def evaluate(self,m):
        """Not used for proof acceptance. Sanity check support of numerator maps."""
        out=[]
        for t in self.terms:
            p={}
            for (a,b,c,d),n in t.numerator.items():
                key=(a+m*c,b+m*d);p[key]=p.get(key,0)+n
            out.append((clean(p),t.factors))
        return out

def E(p):return Expression((Term(p),))
def point(x0,y0,xm=0,ym=0):return E(mono(x0,y0,xm,ym))
def chars(k):return E({(x,y,0,0):1 for x,y in G.OFFSETS[k]})

def run(xm,xj,x0,ym,yj,y0,nm,n0):
    """Sum j=0..nm*m+n0-1 of X^(xm*m+xj*j+x0)Y^(...)."""
    start=mono(x0,y0,xm,ym)
    if nm==0:
        G.require(n0>=0,'Negative finite range')
        return E(dict(Counter((x0+xj*j,y0+yj*j,xm,ym) for j in range(n0))))
    G.require(nm==1 and (xj,yj)!=(0,0),'Unsupported or constant run')
    end=mono(xj*n0,yj*n0,xj*nm,yj*nm)
    num=mul(start,add(mono(),scale(end,-1)))
    return Expression((Term(num,((xj,yj,0,0),)),))

def base():
    # A=X^-2Y, B=X^-1Y^-1; n=m-2.
    a=(-2,1,0,0);b=(-1,-1,0,0);ab=(-1,2,0,0)
    an=mono(2,-1,-2,1)       # A^(m-1)
    bn=mono(1,1,-1,-1)       # B^(m-1)
    abn=mono(1,-2,-1,2)      # (A/B)^(m-1)
    t1=Term(add(mono(),scale(an,-1)),(a,b))
    t2=Term(scale(mul(bn,add(mono(),scale(abn,-1))),-1),(ab,b))
    return chars('R')*point(-2,0,1,0)*Expression((t1,t2))

def point_orbit(x0,y0,xm,ym):
    return point(x0,y0,xm,ym)+point(y0,1-x0-y0,ym,-xm-ym)+point(1-x0-y0,x0,-xm-ym,xm)

def first_source(q):
    out=Expression()
    # j=0..q-1 for y=j+1, r=m-1
    # j=0..m-q-1 for y=j+q+1, r=m
    for y0,nm,n0,e in ((1,0,q,1),(q+1,1,-q,0)):
        # x=y-m-2+e. F, F rho, F rho^2 of H(x,y).
        out += chars('D')*run(-1,1,y0-2+e,1,-2,3-2*y0-e,nm,n0)
        out += chars('V')*run(0,1,y0,-1,1,y0-2+e,nm,n0)
        out += chars('H')*run(1,-2,1-2*y0-e,0,1,y0,nm,n0)
    return out

def source(q):
    out=Expression()
    for p,depth,ym,start,nm,n0 in specification(q)['source_families']:
        intervals=[]
        if ym==1:
            G.require(nm==0,'Unsupported original affine band interval')
            intervals.append((ym,start,nm,n0,0))
        elif nm==0:
            for y in range(start,start+n0):intervals.append((0,y,0,1,int(y<=q)))
        else:
            first=max(0,q-start+1)
            if first:intervals.append((0,start,0,first,1))
            intervals.append((0,start+first,1,n0-first,0))
        for ym,y0,nm,n0,e in intervals:
            if p==0:
                out+=chars('D')*run(ym-1,1,y0-2-3*depth+e,1-2*ym,-2,3+3*depth-2*y0-e,nm,n0)
            elif p==1:
                out+=chars('V')*run(ym,1,y0,ym-1,1,y0-2-3*depth+e,nm,n0)
            else:
                out+=chars('H')*run(1-2*ym,-2,1+3*depth-2*y0-e,ym,1,y0,nm,n0)
    return out

def shift(q):return specification(q)['shift']

def removed(q):
    sx,sy=shift(q);out=Expression()
    for i in range(q):
        a,p=divmod(i,3)
        anchors=((-2-a,-a,1,0),(-a,2+2*a,0,-1),(2+2*a,-2-a,-1,1))
        x0,y0,xm,ym=anchors[p]
        out+=chars('R')*point(x0+sx,y0+sy,xm,ym)
    return out

def holes(q):
    out=Expression()
    for j in range(q):out+=point_orbit(q-j,q+1-j,0,-1)
    return out

def replacement_bones(q):
    out=Expression()
    for k,*row in specification(q)['bone_families']:
        out+=chars(k)*run(*row)
    return out

def identity(q):
    sx,sy=shift(q)
    return replacement_bones(q)-source(q)+(point(sx,sy)-point(0,0))*base()-removed(q)+holes(q)

def verify_all():
    results=[]
    for q in sorted(map(int,json.loads((Path(__file__).resolve().parent/"templates.json").read_text()))):
        r=identity(q).verify_zero();r.update(q=q,m_min=q+2,
          equality='boundary(B)+translated_base-deleted_corners = base-holes+boundary(A)')
        results.append(r)
    return results

if __name__=='__main__':
    out=verify_all();print(json.dumps(out,indent=2))
