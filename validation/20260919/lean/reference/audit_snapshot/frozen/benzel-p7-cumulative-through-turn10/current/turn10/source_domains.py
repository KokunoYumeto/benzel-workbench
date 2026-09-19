"""Exact positivity of original index lengths, source bounds and distinctness.

The verifier uses only fractions. Optional discovery is a separate command.
"""
from pathlib import Path
import importlib.util,json,sys
from fractions import Fraction
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'turn8'))
import geometry as G
from ownership import M,K,I,J,v,add,sub,scale,neg
import source10

def source9():
    spec=importlib.util.spec_from_file_location('frozen_table9_domain',ROOT.parent/'turn9/source_table.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def observations():
    out=[];counts={}
    def bound(name,dom,t):out.append({'name':name,'constraints':dom+[v(1)],'target':t})
    def impossible(name,dom):out.append({'name':name,'constraints':dom,'target':v(-1)})
    for kfix,r in[(None,1),(None,2),(2,1),(2,2),(3,1),(3,2)]:
        tag=f'k{kfix}-r{r}';rows=(source9()if r==1 else source10).ROWS
        base=[sub(K,4),sub(sub(M,scale(K,3)),r+2)]if kfix is None else[sub(K,kfix),sub(kfix,K),sub(sub(M,scale(K,3)),r+2)]
        q=add(scale(K,3),r);domains=[]
        for j,(p,lo,hi,yl,yh,branch)in enumerate(rows):
            low=add(scale(K,lo[0]),lo[1]);high=add(scale(K,hi[0]),hi[1]);name=tag+'/'+str(j)
            def aff(a):return add(add(scale(M,a[0]),scale(K,a[1])),add(scale(I,a[2]),a[3]))
            lower,upper=aff(yl),aff(yh);dd=base+[sub(I,low),sub(high,I)]
            bound(name+'/depth-count',base,add(sub(high,low),1))
            bound(name+'/row-count',dd,add(sub(upper,lower),1))
            if branch=='cross':
                bound(name+'/prefix-length',dd,add(sub(q,lower),1));bound(name+'/tail-length',dd,sub(upper,q))
            else:bound(name+'/branch',dd,sub(q,upper)if branch=='prefix'else sub(lower,add(q,1)))
            dom=dd+[sub(J,lower),sub(upper,J)];domains.append((p,dom))
            for suffix,t in [('y0',sub(J,1)),('y1',sub(add(M,q),J)),('ell0',I),('ell-y',sub(sub(J,1),I)),('ell-q',sub(sub(q,1),I))]:bound(name+'/'+suffix,dom,t)
        for a,(p,da)in enumerate(domains):
            for b,(pp,db)in enumerate(domains[:a]):
                if p==pp:impossible(tag+f'/{a}!={b}',da+db)
        counts[tag]=len(rows)
    # The four fixed q templates used to finish all residues.
    templates=json.loads((ROOT.parent/'turn7/templates.json').read_text())
    for q0 in(1,2,4,5):
        s=templates[str(q0)];q=v(q0);base=[sub(M,q0+2)];doms=[]
        for j,(p,ell,ym,y0,nm,n0)in enumerate(s['source_families']):
            n=add(scale(M,nm),n0);y=add(add(scale(M,ym),y0),I);dom=base+[I,sub(sub(n,1),I)];name=f'legacy-q{q0}/source{j}'
            bound(name+'/length',base,n)
            for suffix,t in [('y0',sub(y,1)),('y1',sub(add(M,q),y)),('ell0',v(ell)),('ell-y',sub(sub(y,1),ell)),('ell-q',v(q0-1-ell))]:bound(name+'/'+suffix,dom,t)
            doms.append((p,ell,ym,y0,nm,n0))
        for a,A in enumerate(doms):
            for b,B in enumerate(doms[:a]):
                if A[:2]!=B[:2]:continue
                def interval(f,z):
                    p,l,ym,y0,nm,n0=f
                    return base+[z,sub(sub(add(scale(M,nm),n0),1),z)],add(add(scale(M,ym),y0),z)
                da,ya=interval(A,I);db,yb=interval(B,J);eq=sub(ya,yb)
                impossible(f'legacy-q{q0}/source{a}!={b}',da+db+[eq,neg(eq)])
        for j,(_,xm,xj,x0,ym,yj,y0,nm,n0)in enumerate(s['bone_families']):bound(f'legacy-q{q0}/bone{j}-count',base,add(scale(M,nm),n0))
        counts[f'legacy-q{q0}']=len(s['source_families'])
    return out,counts

def verify():
    obs,rows=observations();records=json.loads((ROOT/'source-domain-certificates.json').read_text());G.require(len(obs)==len(records),'Source-domain certificate count mismatch')
    for ob,rec in zip(obs,records):
        G.require(rec['name']==ob['name'],'Certificate source association changed');cs=[Fraction(x)for x in rec['multipliers']]
        G.require(len(cs)==len(ob['constraints'])and all(c>=0 for c in cs),'Invalid source-domain multipliers')
        got=tuple(sum(c*r[j]for c,r in zip(cs,ob['constraints']))for j in range(5))
        G.require(got==tuple(ob['target']),'Source-domain identity failed '+ob['name'])
    return {'status':'PASS','exact_affine_certificates':len(obs),'source_table_rows':rows,'optimizer_used_by_verifier':False}
if __name__=='__main__':
    if '--discover' in sys.argv:
        import numpy as np
        from scipy.optimize import linprog
        output=[]
        for ob in observations()[0]:
            A=np.array(ob['constraints'],float).T;b=np.array(ob['target'],float)
            r=linprog(np.ones(A.shape[1]),A_eq=A,b_eq=b,bounds=(0,None),method='highs')
            if r.x is None:raise ValueError('No discovery certificate for '+ob['name'])
            cs=[Fraction(float(x)).limit_denominator(1000000)for x in r.x]
            if any(c<0 for c in cs)or tuple(sum(c*t[j]for c,t in zip(cs,ob['constraints']))for j in range(5))!=tuple(ob['target']):raise ValueError('Discovery reconstruction failed '+ob['name'])
            output.append({'name':ob['name'],'multipliers':[str(x)for x in cs]})
        (ROOT/'source-domain-certificates.json').write_text(json.dumps(output,separators=(',',':'))+'\n')
    print(json.dumps(verify(),indent=2))
