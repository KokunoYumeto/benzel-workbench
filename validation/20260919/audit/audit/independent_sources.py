"""Reconstruct original owner maps and replay nonnegative rational identities.

No producer verifier, affine arithmetic or obligation builder is imported.
SymPy expands newly constructed linear expressions; Fraction checks each
published multiplier against those freshly reconstructed inequalities.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction
import ast,json,itertools,time,hashlib
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'frozen/benzel-p7-cumulative-through-turn10/current'
m,k,i,j=sp.symbols('m k i j');VAR=(m,k,i,j)
OFF={'H':[(0,0),(1,0),(2,0)],'V':[(0,0),(0,1),(0,2)],'D':[(0,0),(1,-1),(2,-2)]}
SPECS=json.loads((SRC/'turn8/families.json').read_text())

def literal(path,name):
    for node in ast.parse(path.read_text()).body:
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in node.targets):return ast.literal_eval(node.value)
    raise ValueError('literal missing')
ROWS={1:literal(SRC/'turn9/source_table.py','ROWS'),2:literal(SRC/'turn10/source10.py','ROWS')}

def vec(e):
    e=sp.Poly(e,*VAR)
    if e.total_degree()>1:raise ValueError('nonlinear constraint')
    return tuple(int(e.coeff_monomial(v)) for v in VAR)+(int(e.coeff_monomial(1)),)

def a4(z,t=i):return z[0]*m+z[1]*k+z[2]*t+z[3]
def a3(z):return z[0]*m+z[1]*k+z[2]
def pairset(kind,x,y,fix=None):
    def val(e):return sp.expand(e if fix is None else sp.sympify(e).subs(k,fix))
    return {(val(x+u),val(y+v)) for u,v in OFF[kind]}
def rot(cs):return {(y,1-x-y) for x,y in cs}
def ref(cs):return {(x,1-x-y) for x,y in cs}
def parent_cells(owner,r,fix):
    if owner['type']=='common':
        row,depth=a4(owner['row']),a4(owner['depth']);off=1 if owner['branch']=='prefix' else 2
        cs=pairset('H',row-m-off-3*depth,row)
        for _ in range(owner['p']):cs=rot(cs)
        cs=ref(cs)
    else:
        part=owner.get('part','corner');f=SPECS[part][owner['family']]
        aa,bb=a4(owner['i']),a4(owner['j'])
        def lin(z):return z[0]*m+z[1]*k+z[2]*aa+z[3]*bb+z[4]
        x,y=lin(f['x']),lin(f['y'])
        if part=='corner':y-=m
        cs=pairset(f['kind'],x,y)
        for _ in range(owner['p']):cs=rot(cs)
        tx,ty=(-2,1) if r==1 else(-1,-1);cs={(x+tx,y+ty) for x,y in cs}
    def val(e):return sp.expand(e if fix is None else sp.sympify(e).subs(k,fix))
    return {(val(x),val(y)) for x,y in cs}

ALL=[]
def check_receipts(path,obs):
    records=json.loads(path.read_text())
    if len(records)!=len(obs):raise ValueError(f'Receipt count differs: {path.name}, {len(records)} vs {len(obs)}')
    for rec,(name,constraints,target) in zip(records,obs):
        if name!=rec['name']:raise ValueError(f'Association differs: {name} != {rec["name"]}')
        coeff=[Fraction(x) for x in rec['multipliers']]
        A=[vec(x) for x in constraints];b=vec(target)
        if len(coeff)!=len(A) or any(q<0 for q in coeff):raise ValueError('invalid multiplier')
        result=tuple(sum(q*row[c] for q,row in zip(coeff,A)) for c in range(5))
        if result!=b:raise ValueError('NONZERO affine residue at '+name)
        ALL.append({'file':str(path.relative_to(SRC)),'name':name,'constraints':A,'target':b,'multipliers':rec['multipliers']})
    return len(obs)

def owners(fix,r):
    legacy=fix is None and r==1
    folder='turn9' if legacy else 'turn10'
    suffix='' if fix is None else f'-k{fix}-r{r}'
    groups=json.loads((SRC/folder/f'edits{suffix}.json').read_text())
    base=[k-4,m-3*k-r-2] if fix is None else[k-fix,fix-k,m-3*k-r-2]
    obs=[];atoms=[];identities=0
    def bound(name,domain,target):obs.append((name,list(domain)+[1],target))
    def impossible(name,domain):obs.append((name,list(domain),-1))
    def domain(count,t=i):return base+[t,a3(count)-1-t]
    for g in groups:
        name=g['name'];cnt=g['count'];dom=domain(cnt)
        bound(name+('/nonnegative-count' if legacy else '/count'),base,a3(cnt))
        if len(g['old'])!=len(g['owners']):raise ValueError('Missing source owner')
        for n,(tile,o) in enumerate(zip(g['old'],g['owners'])):
            nm=f'{name}/{n}'
            if pairset(tile[0],a4(tile[1]),a4(tile[2]),fix)!=parent_cells(o,r,fix):raise ValueError('Original triple identity FAILED: '+nm)
            identities+=1;atoms.append((nm,cnt,o))
            if o['type']=='common':
                y,l=a4(o['row']),a4(o['depth']);q=3*k+r
                values=[y-1,m+q-y,l,y-1-l,q-1-l]
                suffixes=['row-low','row-high','depth-low','depth-below-row','depth-below-q'] if legacy else ['y0','y1','l0','ly','lq']
                for suf,val in zip(suffixes,values):bound(nm+'/'+suf,dom,val)
                bound(nm+'/branch',dom,q-y if o['branch']=='prefix' else y-q-1)
                for z,(p,elo,ehi,lo,hi,_) in enumerate(ROWS[r]):
                    if p!=o['p']:continue
                    def yy(a):return a[0]*m+a[1]*k+a[2]*l+a[3]
                    impossible(nm+'/outside-A0-'+str(z),dom+[l-elo[0]*k-elo[1],ehi[0]*k+ehi[1]-l,y-yy(lo),yy(hi)-y])
            else:
                f=SPECS[o.get('part','corner')][o['family']];aa,bb=a4(o['i']),a4(o['j']);outer=a3(f['I'])
                inner=1 if f['J'] is None else a3(f['J'][:3])+f['J'][3]*aa
                keys=['i-low','i-high','j-low','j-high'] if legacy else ['i0','i1','j0','j1']
                for key,val in zip(keys,[aa,outer-1-aa,bb,inner-1-bb]):bound(nm+'/'+key,dom,val)
    for nm,cnt,o in atoms:
        if cnt==[0,0,1]:continue
        keys=['row','depth'] if o['type']=='common' else ['i','j']
        if not any(o[key][2]!=0 for key in keys):raise ValueError('Noninjective original index map '+nm)
    for (na,ca,a),(nb,cb,b) in itertools.combinations(atoms,2):
        if a['type']!=b['type'] or a['p']!=b['p']:continue
        if a['type']!='common' and (a.get('part','corner'),a['family'])!=(b.get('part','corner'),b['family']):continue
        constraints=domain(ca)+domain(cb,j)
        for key in (('row','depth') if a['type']=='common' else ('i','j')):
            e=a4(a[key])-a4(b[key],j);constraints.extend([e,-e])
        impossible(na+('!= ' if legacy else ' != ')+nb,constraints)
    n=check_receipts(SRC/folder/f'ownership-certificates{suffix}.json',obs)
    return {'fixed_k':fix,'residue':r,'original_tile_map_identities':identities,'affine_certificates':n,'status':'PASS'}

def source_domains():
    obs=[]
    def bound(name,dom,t):obs.append((name,list(dom)+[1],t))
    def impossible(name,dom):obs.append((name,list(dom),-1))
    for fix,r in [(None,1),(None,2),(2,1),(2,2),(3,1),(3,2)]:
        tag=f'k{fix}-r{r}';base=[k-4,m-3*k-r-2] if fix is None else[k-fix,fix-k,m-3*k-r-2];q=3*k+r;domains=[]
        for n,(p,lo,hi,yl,yh,branch) in enumerate(ROWS[r]):
            low,high=lo[0]*k+lo[1],hi[0]*k+hi[1];nm=f'{tag}/{n}'
            def lin(z):return z[0]*m+z[1]*k+z[2]*i+z[3]
            lower,upper=lin(yl),lin(yh);dd=base+[i-low,high-i]
            bound(nm+'/depth-count',base,high-low+1);bound(nm+'/row-count',dd,upper-lower+1)
            if branch=='cross':bound(nm+'/prefix-length',dd,q-lower+1);bound(nm+'/tail-length',dd,upper-q)
            else:bound(nm+'/branch',dd,q-upper if branch=='prefix' else lower-q-1)
            dom=dd+[j-lower,upper-j];domains.append((p,dom))
            for key,e in [('y0',j-1),('y1',m+q-j),('ell0',i),('ell-y',j-1-i),('ell-q',q-1-i)]:bound(nm+'/'+key,dom,e)
        for a,(p,da) in enumerate(domains):
            for b,(pp,db) in enumerate(domains[:a]):
                if p==pp:impossible(tag+f'/{a}!={b}',da+db)
    templates=json.loads((SRC/'turn7/templates.json').read_text())
    for q in (1,2,4,5):
        spec=templates[str(q)];base=[m-q-2];doms=[]
        for n,(p,l,ym,y0,nm,n0) in enumerate(spec['source_families']):
            length=nm*m+n0;y=ym*m+y0+i;dom=base+[i,length-1-i];name=f'legacy-q{q}/source{n}'
            bound(name+'/length',base,length)
            for key,e in [('y0',y-1),('y1',m+q-y),('ell0',l),('ell-y',y-1-l),('ell-q',q-1-l)]:bound(name+'/'+key,dom,e)
            doms.append((p,l,ym,y0,nm,n0))
        for a,A in enumerate(doms):
            for b,B in enumerate(doms[:a]):
                if A[:2]!=B[:2]:continue
                def interval(f,t):return base+[t,f[4]*m+f[5]-1-t],f[2]*m+f[3]+t
                da,ya=interval(A,i);db,yb=interval(B,j)
                impossible(f'legacy-q{q}/source{a}!={b}',da+db+[ya-yb,yb-ya])
        for n,f in enumerate(spec['bone_families']):bound(f'legacy-q{q}/bone{n}-count',base,f[-2]*m+f[-1])
    n=check_receipts(SRC/'turn10/source-domain-certificates.json',obs)
    return {'status':'PASS','affine_certificates':n}

def parent_ranges():
    u,v=sp.symbols('u v')
    tested=[]
    for part in ('source','corner','long','deleted'):
        for n,f in enumerate(SPECS[part]):
            outer=a3(f['I'])
            tests=[outer]
            if f['J'] is not None:
                jm,jk,jc,ji=f['J'];inner=jm*m+jk*k+jc+ji*i
                tests.append(inner.subs(i,0 if ji>=0 else outer-1))
            for e in tests:
                transformed=sp.Poly(sp.expand(e.subs({m:u+3*v+8,k:v+2}, simultaneous=True)),u,v)
                if any(c<0 for c in transformed.coeffs()):raise ValueError('Nonnegative parameter-domain certificate failed')
                tested.append({'part':part,'family':n,'nonnegative_polynomial':str(transformed.as_expr())})
    return {'status':'PASS','bounds':len(tested),'coordinate_map':'k=v+2, m=u+3v+8; inverse v=k-2,u=m-3k-2','checks':tested}

def main():
    t=time.monotonic();results=[]
    for fix,r in [(None,1),(None,2),(2,1),(2,2),(3,1),(3,2)]:
        res=owners(fix,r);results.append(res);print(res,flush=True)
    domains=source_domains();ranges=parent_ranges()
    outfile=ROOT/'evidence/reconstructed-linear-identities.jsonl'
    with outfile.open('w') as out:
        for rec in ALL:out.write(json.dumps(rec,separators=(',',':'))+'\n')
    result={'status':'PASS','seconds':round(time.monotonic()-t,3),'owners':results,'source_domains':domains,'parent_index_ranges':ranges,
            'total_exact_affine_receipts':len(ALL),'all_constraints_reconstructed_without_producer_modules':True,
            'linear_receipts_sha256':hashlib.sha256(outfile.read_bytes()).hexdigest()}
    (ROOT/'evidence/independent-sources.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS total exact rational certificates',len(ALL))
if __name__=='__main__':main()
