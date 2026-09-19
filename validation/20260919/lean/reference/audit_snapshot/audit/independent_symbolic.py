"""A separate symbolic verifier, using SymPy's integer polynomial arithmetic.

It imports no producer symbolic implementation. All generating functions are
rebuilt from frozen literal tables, original tile offsets and the geometric-sum
identity derived in the audit report. The two size parameters remain formal.
"""
from __future__ import annotations
import ast,json,time,hashlib
from pathlib import Path
from collections import Counter
from sympy.polys.rings import ring
from sympy import ZZ
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'frozen/benzel-p7-cumulative-through-turn10/current'
P,*_ = ring('X,Y,Mx,My,Kx,Ky',ZZ)
ZERO=(0,)*6
EXPORTED_IDENTITIES=[]

def literal(path,name):
    for node in ast.parse(path.read_text()).body:
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in node.targets):
            return ast.literal_eval(node.value)
    raise ValueError('Missing literal '+name)

def mon(v=ZERO):return P.from_dict({tuple(v):ZZ.one})

class Sum:
    def __init__(self,terms=()):self.terms=tuple((n,tuple(ds)) for n,ds in terms if n)
    def __add__(self,b):return Sum(self.terms+b.terms)
    def __neg__(self):return Sum((-n,ds) for n,ds in self.terms)
    def __sub__(self,b):return self+(-b)
    def __mul__(self,b):return Sum((n*m,ds+es) for n,ds in self.terms for m,es in b.terms)
    def shift(self,v):return Sum((n*mon(v),ds) for n,ds in self.terms)
    def move(self,A,o=(0,0)):
        def image(e):
            out=[]
            for x,y in zip(e[::2],e[1::2]):out.extend((A[0][0]*x+A[0][1]*y,A[1][0]*x+A[1][1]*y))
            out[0]+=o[0];out[1]+=o[1];return tuple(out)
        ans=[]
        for n,ds in self.terms:
            d={}
            for v,c in n.items():
                u=image(v);d[u]=d.get(u,0)+c
            den=[(A[0][0]*x+A[0][1]*y,A[1][0]*x+A[1][1]*y) for x,y in ds]
            ans.append((P.from_dict(d),den))
        return Sum(ans)
    def fixk(self,k):
        ans=[]
        for n,ds in self.terms:
            d={}
            for(a,b,c,e,f,g),v in n.items():
                u=(a+k*f,b+k*g,c,e,0,0);d[u]=d.get(u,0)+v
            ans.append((P.from_dict(d),ds))
        return Sum(ans)
    def verify(self,name):
        canonical=[];common=Counter()
        for num,den in self.terms:
            ds=[]
            for x,y in den:
                if (x,y)==(0,0):raise ValueError('Attempted zero denominator')
                if x<0 or (x==0 and y<0):
                    # EXACT equality of fractions: 1/(1-z^-1)=-z/(1-z).
                    x,y=-x,-y;num=-num*mon((x,y,0,0,0,0))
                ds.append((x,y))
            dc=Counter(ds);common|=dc;canonical.append((num,dc))
        total=P.zero;expanded=0
        for num,dc in canonical:
            for(x,y),count in (common-dc).items():num*= (P.one-mon((x,y,0,0,0,0)))**count
            expanded+=len(num);total+=num
        if total:raise ValueError(name+': NONZERO '+str(total)[:1000])
        result={'identity':name,'status':'PASS','summands':len(self.terms),'expanded_monomials':expanded,
                'nonzero_result_coefficients':len(total),'denominator_factors':[[list(v),n] for v,n in sorted(common.items())]}
        EXPORTED_IDENTITIES.append({'identity':name,'terms':[{'numerator':[[list(v),int(c)] for v,c in sorted(n.items())],'denominator':[list(d) for d in ds]} for n,ds in self.terms]})
        print(name,': PASS',expanded,'expanded integer monomials',flush=True)
        return result

def pt(a=0,b=0,am=0,bm=0,ak=0,bk=0):return Sum(((mon((a,b,am,bm,ak,bk)),()),))
def rotate(s):return s.move(((0,1),(-1,-1)),(0,1))
def reflect(s):return s.move(((1,0),(-1,-1)),(0,1))
def orbit(s):return s+rotate(s)+rotate(rotate(s))
def orient(s,p):
    for _ in range(p):s=rotate(s)
    return reflect(s)
OFF={'R':((0,0),(1,0),(0,1)),'H':((0,0),(1,0),(2,0)),'V':((0,0),(0,1),(0,2)),'D':((0,0),(1,-1),(2,-2))}
def shape(kind):return Sum(((sum((mon((x,y,0,0,0,0)) for x,y in OFF[kind]),P.zero),()),))
def geom(direction,length):
    x,y=direction;am,ak,c=length
    if direction==(0,0):
        if am or ak:raise ValueError('Unrepresented variable multiplicity')
        return Sum(((P.ground_new(c),()),))
    return Sum((((P.one-mon((x*c,y*c,x*am,y*am,x*ak,y*ak))),((x,y),)),))
def power(v,n):
    x,y=v;am,ak,c=n;return pt(x*c,y*c,x*am,y*am,x*ak,y*ak)
def fam(kind,x,y,outer,inner=None):
    xm,xk,xi,xj,xc=x;ym,yk,yi,yj,yc=y
    offset=pt(xc,yc,xm,ym,xk,yk)*shape(kind)
    if inner is None:return offset*geom((xi,yi),tuple(outer))
    jm,jk,jc,ji=inner;s=(xj,yj)
    body=geom((xi,yi),tuple(outer))-power(s,(jm,jk,jc))*geom((xi+ji*xj,yi+ji*yj),tuple(outer))
    if s==(0,0):raise ValueError('Inner multiplicity requires explicit handling')
    return offset*Sum((n,ds+(s,)) for n,ds in body.terms)
SPECS=json.loads((SRC/'turn8/families.json').read_text())
def group(name):
    s=Sum()
    for f in SPECS[name]:s+=fam(f['kind'],f['x'],f['y'],f['I'],f['J'])
    return s
BASE=fam('R',(1,0,-2,-1,-2),(0,0,1,-1,0),(1,0,-1),(1,0,-1,-1))
B8=orbit(group('long')+pt(bm=-1)*group('corner'))
D8=orbit(group('deleted'))
def missing(r):return orbit(pt(r,r+1,0,-1,3,3)*geom((-1,-1),(0,3,r)))

def source_rows(r):return literal(SRC/('turn9/source_table.py' if r==1 else 'turn10/source10.py'),'ROWS')
def source_part(p,elo,ehi,lo,hi,branch):
    ek,ec=elo
    ly_m,ly_k,ly_i,ly_c=lo
    y=[ly_m,ly_k+ly_i*ek,ly_i,1,ly_c+ly_i*ec]
    off=1 if branch=='prefix' else 2
    x=[y[0]-1,y[1]-3*ek,y[2]-3,1,y[4]-off-3*ec]
    dm,dk,di,dc=[h-l for h,l in zip(hi,lo)]
    outer=(0,ehi[0]-ek,ehi[1]-ec+1);inner=(dm,dk+di*ek,dc+di*ec+1,di)
    return orient(fam('H',x,y,outer,inner),p)
def scaffold_source(r):
    s=Sum()
    for p,elo,ehi,lo,hi,branch in source_rows(r):
        if branch=='cross':
            s+=source_part(p,elo,ehi,lo,(0,3,0,r),'prefix')
            s+=source_part(p,elo,ehi,(0,3,0,r+1),hi,'tail')
        else:s+=source_part(p,elo,ehi,lo,hi,branch)
    return s
Z9=literal(SRC/'turn10/source10.py','Z9')
def zpoly(r):
    points=[pt(*v) for v in Z9]
    if r==1:return sum(points,Sum())
    return sum((p.shift((1,-2,0,0,0,0)) for p in points[:12]),Sum())+sum((rotate(rotate(p)).shift((-2,1,0,0,0,0)) for p in points[3:]),Sum())
def scaffold(r):
    extra=pt(-2,0,1,0,-1,-1)*shape('R')
    deleted=D8+extra
    if r==2:deleted+=rotate(rotate(extra))
    trans=(-2,1,0,0,0,0) if r==1 else (-1,-1,0,0,0,0)
    return (B8+BASE-deleted).shift(trans)+zpoly(r)-BASE+missing(r)-scaffold_source(r)
def edits(path):
    s=Sum()
    for g in json.loads(path.read_text()):
        for side,sgn in (('new',1),('old',-1)):
            for kind,x,y in g[side]:
                start=pt(x[3],y[3],x[0],y[0],x[1],y[1])*shape(kind)
                length=tuple(g['count'])
                term=start*geom((x[2],y[2]),length)
                s+=term if sgn==1 else -term
    return s

def fixed_identity(q):
    spec=json.loads((SRC/'turn7/templates.json').read_text())[str(q)]
    A=Sum();B=Sum()
    for p,depth,ym,y0,nm,n0 in spec['source_families']:
        segments=[]
        if ym!=0:raise ValueError('Fixed-source family with parameter-dependent start needs additional cut')
        if nm==0:
            for y in range(y0,y0+n0):segments.append((y,(0,0,1),y<=q))
        else:
            early=max(0,q-y0+1)
            if early:segments.append((y0,(0,0,early),True))
            segments.append((y0+early,(nm,0,n0-early),False))
        for first,length,prefix in segments:
            off=1 if prefix else 2
            s=pt(first-off-3*depth,first,-1,0)*shape('H')*geom((1,1),length)
            A+=orient(s,p)
    for kind,xm,xj,x0,ym,yj,y0,nm,n0 in spec['bone_families']:
        B+=pt(x0,y0,xm,ym)*shape(kind)*geom((xj,yj),(nm,0,n0))
    deleted=Sum()
    for i in range(q):
        a,p=divmod(i,3);s=pt(-2-a,-a,1,0)*shape('R')
        for _ in range(p):s=rotate(s)
        deleted+=s
    sx,sy=spec['shift'];shifted=(BASE-deleted).shift((sx,sy,0,0,0,0))
    M=orbit(pt(q,q+1,0,-1)*geom((-1,-1),(0,0,q)))
    return B-A+shifted-BASE+M

def main():
    t=time.monotonic();results=[]
    results.append((B8-orbit(reflect(group('source')))-D8+missing(0)).verify('threefold k>=2,m>=3k+2'))
    # The complete k=1 source is a separate legitimate family; no negative loops.
    A=orient(pt(0,1,-1,0)*shape('H')*geom((1,1),(0,0,3)),0)
    A+=orient(pt(2,4,-1,0)*shape('H')*geom((1,1),(1,0,-2)),0)
    B=pt(2,2,0,-1)*shape('H')*geom((1,1),(1,0,-3))
    for kind,x,y in [('V',-1,1),('V',0,0),('V',1,-1),('D',0,3)]:B+=pt(x,y,0,-1)*shape(kind)
    one=orbit(B-A-pt(-2,0,1,0)*shape('R')+pt(3,4,0,-1)*geom((-1,-1),(0,0,3)))
    results.append(one.verify('threefold k=1,m>=5'))
    for q in (1,2,4,5):results.append(fixed_identity(q).verify(f'fixed q={q},m>={q+2}'))
    for r in (1,2):
        sc=scaffold(r);path=SRC/('turn9/edits.json' if r==1 else 'turn10/edits.json');ep=edits(path)-zpoly(r)
        results.append(sc.verify(f'scaffold r={r},k>=4'))
        results.append(ep.verify(f'endpoint r={r},k>=4'))
        for k in (2,3):
            results.append(sc.fixk(k).verify(f'scaffold k={k},r={r},m>={3*k+r+2}'))
            p=SRC/f'turn10/edits-k{k}-r{r}.json'
            results.append((edits(p)-zpoly(r)).fixk(k).verify(f'endpoint k={k},r={r},m>={3*k+r+2}'))
    # Altering one actual cell coefficient must be rejected by this independent engine.
    try:(one+pt(17,-19)).verify('deliberately mutated expression')
    except ValueError:mutation='PASS: nonzero original cell rejected'
    else:raise RuntimeError('symbolic engine accepted nonzero cell')
    result={'status':'PASS','engine':'independently assembled finite-sum rational expressions, SymPy integer PolyElement arithmetic',
            'seconds':round(time.monotonic()-t,3),'identities':results,'mutation':mutation,
            'producer_symbolic_modules_imported':False}
    path=ROOT/'evidence/independent-symbolic.json';path.write_text(json.dumps(result,indent=2)+'\n')
    with (ROOT/'evidence/reconstructed-polynomial-identities.jsonl').open('w') as out:
        for item in EXPORTED_IDENTITIES:out.write(json.dumps(item,separators=(',',':'))+'\n')
if __name__=='__main__':main()
