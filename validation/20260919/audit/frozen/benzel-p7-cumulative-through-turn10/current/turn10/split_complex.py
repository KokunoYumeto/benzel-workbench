"""Actual support-indexed augmented incidence complex of the new endpoint repairs."""
from dataclasses import dataclass
from collections import Counter
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'turn8'))
import geometry as G
from cohomology import Scalar,TAU,E,ONE,MatchingKernel,clean,add,scale,unit,join

class RepairSupports:
    def __init__(self,old,new):
        self.old=tuple(old);self.new=tuple(new)
        a,b=G.incidence(self.old),G.incidence(self.new)
        G.require(all(v==1 for v in a.values())and all(v==1 for v in b.values()),'Original endpoint inputs must be matchings')
        G.require(set(a)<=set(b),'Endpoint matching does not cover old support')
        self.holes=frozenset(set(b)-set(a));G.require(self.holes,'Original vacancy set is empty')
    def label(self,A):
        if A is None:return None
        A=frozenset(A);G.require(all(type(i)is int and 0<=i<len(self.old)for i in A),'Unknown original release index');return A
    def cells(self,A):
        A=self.label(A)
        return frozenset()if A is None else self.holes|frozenset(c for i in A for c in self.old[i][1])
    def validate(self,A,n):
        n=clean(n);support=self.cells(A)
        for t in n:G.anchor(t);G.require(t[0]!='R'and set(t[1])<=support,'Generator outside the original bone-support complex')
        return n
    def eta(self,A,B):
        A=self.label(A);B=self.label(B);G.require(A is not None and B is not None and A<=B,'Actual supported inclusion required')
        return unit(self.old[i]for i in B-A)
    def differential(self,A,r,n):
        G.require(type(r)is int and(A is not None or r==0),'Original charge at bottom');n=self.validate(A,n)
        return add(G.chain_boundary(n),scale(-r,unit(self.cells(A))))
    def transition(self,A,B,r,n):
        n=self.validate(A,n)
        if A is None:G.require(r==0 and not n,'Bottom module is zero');return 0,{}
        return r,add(n,scale(r,self.eta(A,B)))
    def positive(self,A,r,n):
        n=self.validate(A,n)
        return r==1 and all(c>=0 for c in n.values())and not self.differential(A,r,n)

@dataclass
class Total:
    support:RepairSupports
    degree:int
    label:object
    amplitude:dict
    def __post_init__(self):
        self.label=self.support.label(self.label);self.amplitude=clean(self.amplitude)
        if self.degree==0:self.support.validate(self.label,self.amplitude)
        elif self.degree==1:G.require(set(self.amplitude)<=self.support.cells(self.label),'Cell coefficient outside support')
        elif self.degree==2:G.require(not self.amplitude,'Following fibre is zero')
        else:raise ValueError('Original degree must be 0,1,2')
    def __add__(self,b):
        G.require(self.support is b.support and self.degree==b.degree,'Typed source/target mismatch')
        return Total(self.support,self.degree,join(self.label,b.label),add(self.amplitude,b.amplitude))
    def smul(self,s):return Total(self.support,self.degree,self.label if s.present else None,scale(s.amplitude,self.amplitude))
    def d(self):
        G.require(self.degree<2,'No following degree')
        return Total(self.support,self.degree+1,self.label,G.chain_boundary(self.amplitude)if self.degree==0 else{})


def verify_repair(old,new):
    S=RepairSupports(old,new);full=frozenset(range(len(old)));initial=frozenset();K=MatchingKernel(old,new)
    G.require(S.positive(full,1,unit(new)),'Positive charge-one endpoint cycle failed')
    G.require(G.chain_boundary(add(unit(new),scale(-1,unit(old))))==unit(S.holes),'Original signed cochain endpoint identity failed')
    A=frozenset(range(0,len(old),3));B=A|frozenset(range(1,len(old),3));n=unit(old[i]for i in A)
    d0=S.differential(A,2,n);r,n1=S.transition(A,B,2,n)
    G.require(S.differential(B,r,n1)==d0,'Augmented source square failed')
    r,n2=S.transition(B,full,r,n1);r3,n3=S.transition(A,full,2,n)
    G.require((r,n2)==(r3,n3),'Augmented composition lost original release terms')
    z=Total(S,0,full,unit(old));G.require(z.d().d().label==full and not z.d().d().amplitude,'Supported differential square failed')
    G.require(z.smul(E).label==full and z.smul(TAU).label is None,'Supported zero or absence was lost')
    G.require(z.smul(ONE).amplitude==z.amplitude,'Scalar identity failed')
    x=Total(S,0,A,n);y=Total(S,0,B,unit(old[i]for i in B));G.require((x+y).d().amplitude==(x.d()+y.d()).amplitude,'Actual inclusion differential not additive')
    q=tuple((i%7)-3 for i in range(len(K.B)));coords=K.coordinates(q)
    G.require(K.coordinates(K.inverse_coordinates(coords))==coords,'Integral kernel coordinate inverse failed')
    K.check_relations()
    for j in K.basis:K.check_dual(j)
    hole=min(S.holes);G.require(all(hole not in t[1]for t in old),'Distinguished evaluation does not annihilate old boundaries')
    return {'kernel_rank':len(K.basis),'closed_components':len(K.closed),'integer_duals':len(K.basis),
            'vacancy_cells':len(S.holes),'augmented_checks':4,'supported_zero_checks':3,'homotopy_identity':1}
