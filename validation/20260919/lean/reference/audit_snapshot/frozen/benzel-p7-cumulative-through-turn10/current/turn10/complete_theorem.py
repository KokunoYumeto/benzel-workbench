"""Complete residue-zero benzel construction on the original cells.

Uses the exact retained q=0,3k,+1 sources and new +2/exception tables.
No search or optimizer is called by any constructor.
"""
from pathlib import Path
from collections import Counter
import importlib.util,json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'turn8'))
import geometry as G,packing as P,construction as C8
import source10

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj;spec.loader.exec_module(obj);return obj
SOURCE9=load('frozen_source9',ROOT.parent/'turn9/source_table.py')
# This legacy import has no conflicting module names; its data stay unchanged.
P7=load('parent_construction',ROOT.parent/'turn7/parent_construction.py')
C7=load('frozen_templates7',ROOT.parent/'turn7/construction.py')

def canonical(delta:int):
    G.require(type(delta)is int and delta>=0,'Nonnegative integral invariant required')
    if delta==0:return 1,0
    m=G.block(delta)+1;q=G.triangular(m)-delta
    G.require(0<=q<=m-2,'Triangular inverse left its canonical domain')
    return m,q

def route(q:int):
    if q==0:return 'triangular'
    if q in(1,2,4,5):return 'fixed-'+str(q)
    k,r=divmod(q,3)
    if r==0:return 'threefold'
    if k in(2,3):return f'exception-k{k}-r{r}'
    G.require(k>=4,'An actual canonical residue was left uncovered')
    return 'residue-'+str(r)

def shift(t,s):return t[0],tuple(sorted((x+s[0],y+s[1])for x,y in t[1]))

def receiving(d,m,q,p,y,ell):
    G.require(d>=m>=q+2 and 0<=p<3 and 1<=y<=m+q and 0<=ell<min(y,q),'Original receiving domain')
    h=G.triangular(d)-G.triangular(m)+q
    if y<=h:
        j=y-1-ell;L=1-2*y-G.block(y+G.triangular(m)-q);role='prefix'
    else:
        G.require(d==m,'Unexpected exterior tail');j=q-1-ell;L=y-3*q-m+1;role='tail'
    out=G.reflect_tile(G.rotate_tile(G.tile('H',L+3*j,y),p))
    return role,j,out

def common_labels(m,q):
    for p in range(3):
        for y in range(1,m+q+1):
            rr=m-1 if y<=q else m
            for ell in range(min(y,q)):
                yield p,y,ell,G.reflect_tile(G.rotate_tile(G.tile('H',y-rr-2-3*ell,y),p))

def edit_data(k,r):
    if k in(2,3):path=ROOT/f'edits-k{k}-r{r}.json'
    elif r==1:path=ROOT.parent/'turn9/edits.json'
    else:path=ROOT/'edits.json'
    return json.loads(path.read_text())

def expand_row(row,m,k,i):
    kind,x,y=row
    def value(a):return a[0]*m+a[1]*k+a[2]*i+a[3]
    return G.tile(kind,value(x),value(y))

def core(m,k,r,check=True):
    q=3*k+r;G.require(r in(1,2) and k>=2 and m>=q+2,'Original nonzero residue core domain')
    source=SOURCE9 if r==1 else source10;s=(-2,1)if r==1 else(-1,-1)
    labels=tuple(common_labels(m,q));common=tuple(z[3]for z in labels);a0=tuple(z[3]for z in source.labels(m,k))
    G.require(len(set(a0))==len(a0) and set(a0)<=set(common),'Original scaffold source invalid')
    base=set(C8.retained_stones(m,k));extra={G.rotate_tile(G.tile('R',m-2-k,-k),p)for p in((0,)if r==1 else(0,2))}
    G.require(len(extra)==r and extra<=base,'Original extra stone missing')
    stones=tuple(shift(t,s)for t in sorted(base-extra));bb=tuple(shift(t,s)for t in C8.new_bones(m,k))
    initial=tuple(sorted(set(common)-set(a0)))+bb;states=Counter(initial);allold=[];allnew=[]
    G.require(all(v==1 for v in states.values()),'Duplicate scaffold tile')
    for g in edit_data(k,r):
        am,ak,c=g['count'];n=am*m+ak*k+c;G.require(n>=0,'Negative original index range')
        for i in range(n):
            old=tuple(expand_row(row,m,k,i)for row in g['old']);new=tuple(expand_row(row,m,k,i)for row in g['new'])
            allold.extend(old);allnew.extend(new)
            for t in old:
                G.require(states[t]==1,f'Missing original source at {g["name"]}/{i}')
                states[t]-=1
            states.update(new)
            G.require(all(v in(0,1)for v in states.values()),'A positive edit duplicated an original tile')
    G.require(len(set(allold))==len(allold) and set(allold)<=set(initial),'Original sources were borrowed or repeated')
    bones=tuple(states.elements());omega=G.omega(G.triangular(m)-q)
    if check:G.check_partition(bones+stones,omega|set(G.incidence(common)))
    return labels,bones,stones,tuple(allold),tuple(allnew)

def complete_from_core(d,m,q,check=True):
    G.require(type(d)is int and type(m)is int and type(q)is int and d>=m>=q+2 and q>=1,'Original core and receiving domain')
    branch=route(q);k,r=divmod(q,3);h=G.triangular(d)-G.triangular(m)+q
    if branch.startswith('fixed-'):out=C7.complete(d,m,q)
    elif r==0:out=C8.complete(d,m,k)
    else:
        labels,bones,stones,_,_=core(m,k,r,check);common={t for *_,t in labels};old=set(P.packing(d,h))
        for p,y,ell,t in labels:
            G.require(receiving(d,m,q,p,y,ell)[2]==t,'Original generator receiving square failed')
        G.require(common<=old,'Original common body is not in finite packing')
        out=tuple(sorted(old-common))+bones+stones
    if check:
        G.check_partition(out,G.region(d,h));counts=Counter(t[0]for t in out)
        G.require(counts['R']==G.triangular(m)-q and len(out)-counts['R']==3*h*(h+d),'Wrong original tile counts')
    return out

def complete_W(d:int,h:int,check=True):
    G.require(type(d)is int and type(h)is int and d>=2 and 0<=h<=G.triangular(d),'Use d>=2,0<=h<=C(d,2)')
    delta=G.triangular(d)-h;m,q=canonical(delta);G.require(m<=d,'Canonical core exceeds exterior parameter')
    if d==2:
        # Same original band formula; the parent API deliberately begins at d=3.
        if h==0:out=(G.tile('R',0,0),)
        else:
            out=[]
            for y in range(1,2*h+d+1):
                L,c=((1-2*y-G.block(y+delta),y) if y<=h else(y-3*h-d+1,min(h,2*h+d-y)))
                for j in range(c):out.extend(G.reflect_tile(G.rotate_tile(G.tile('H',L+3*j,y),p))for p in range(3))
            out=tuple(out)
    elif q==0:out=P.triangular_family(d,m)
    else:out=complete_from_core(d,m,q,check)
    if check:G.check_partition(out,G.region_ab(d+3*h,2*d+3*h))
    return out

def residue_one(a:int,b:int):
    G.require(a>=2 and b>=2 and a<=2*b and b<=2*a and (a+b)%3==1,'Original residue-one domain')
    target=G.region_ab(a,b);out=set();r=(2-a)%3
    # Barycentric anchor u has sum zero; the original R-anchor is (u0,u1).
    for x,y in target:
        for dx,dy in((0,0),(1,0),(0,1)):
            ux,uy=x-dx,y-dy
            if (uy-ux)%3==r:
                out.add(G.tile('R',ux,uy));break
        else:raise ValueError('No original anchor residue')
    G.check_partition(tuple(out),target);return tuple(sorted(out))

if __name__=='__main__':
    for d in range(2,10):
        for h in range(G.triangular(d)+1):complete_W(d,h)
        print('d',d,'complete',flush=True)
