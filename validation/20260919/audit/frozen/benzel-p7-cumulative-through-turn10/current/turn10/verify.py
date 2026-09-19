"""Replay complete construction, exact parameter proofs and Split-Zero maps.

Only Python's standard library is used. This is not a Lean build or specialist
acceptance. All ranges below accompany, rather than replace, the written proof.
"""
from pathlib import Path
import argparse,json,sys,time,hashlib,subprocess,tempfile
from collections import Counter
import complete_theorem as T
import symbolic_certificate as SY,small_symbolic as SS,ownership as O,source_domains as SD
from split_complex import verify_repair
G=T.G;ROOT=Path(__file__).resolve().parent

def strip_metadata(obj):
    if isinstance(obj,dict):return {k:strip_metadata(v)for k,v in obj.items()if k!='proof_domain'}
    if isinstance(obj,list):return list(map(strip_metadata,obj))
    return obj

def independent_region(a,b):
    # Enumerate the two difference coordinates, with an exact inverse to cells.
    out=set()
    for u in range(1-a,b):
        lo=max(1-a,1-b-u);hi=min(b-1,a-1-u)
        for v in range(lo,hi+1):
            if (1-v-2*u)%3:continue
            x=(1-v-2*u)//3;y=x+u
            G.require(G.differences((x,y))==(u,v,-u-v),'Difference-coordinate inverse failed')
            out.add((x,y))
    return frozenset(out)

def prior_receipt(script,cwd):
    cmd=[sys.executable]+(['-O']if not __debug__ else[])+[script]
    p=subprocess.run(cmd,cwd=cwd,text=True,capture_output=True,timeout=45)
    G.require(p.returncode==0,'Retained proof checker failed: '+str(cwd)+'/'+script+' '+p.stderr)
    return json.loads(p.stdout)

def reject(f):
    try:f()
    except (ValueError,AssertionError,KeyError):return 1
    raise ValueError('Deliberately invalid input was accepted')

def main(dmax=12,kmax=9,full=True):
    started=time.time();counts=Counter();routes=Counter();records={};print('START parameter identities',flush=True)
    records['uniform_residue_two']=strip_metadata(SY.verify())
    O.configure();records['uniform_source_maps']=O.verify()
    records['exceptional_residues']=[]
    for k in(2,3):
        for r in(1,2):
            O.configure(k,r);rec=SS.verify(k,r);rec['source_maps']=O.verify();records['exceptional_residues'].append(rec)
    O.configure();records['source_domain_bounds']=SD.verify()
    fixed=T.load('fixed_polynomial_replay',ROOT.parent/'turn7/polynomial_check.py')
    records['fixed_residue_identities']={str(q):fixed.identity(q).verify_zero()for q in(1,2,4,5)}
    if full:
        records['retained_threefold']=strip_metadata(prior_receipt('bivariate_certificate.py',ROOT.parent/'turn8'))
        records['retained_residue_one']=strip_metadata(prior_receipt('symbolic_certificate.py',ROOT.parent/'turn9'))
        records['retained_residue_one_owners']=prior_receipt('ownership.py',ROOT.parent/'turn9')
    print('PARAMETER IDENTITIES PASS',flush=True)
    for d in range(2,dmax+1):
        for h in range(G.triangular(d)+1):
            m,q=T.canonical(G.triangular(d)-h);routes[T.route(q)]+=1
            ts=T.complete_W(d,h);counts['all_h_original_tilings']+=1;counts['all_h_placements']+=len(ts)
            reflected=tuple(G.reflect_tile(t)for t in ts);a,b=d+3*h,2*d+3*h
            G.check_partition(reflected,G.region_ab(b,a));counts['reflected_tilings']+=1;counts['reflected_placements']+=len(ts)
            if h in{0,1,G.triangular(d)//2,G.triangular(d)}:
                G.require(independent_region(a,b)==G.region_ab(a,b),'Independent original-region enumeration differs');counts['independent_regions']+=1
        print('ALL-H d',d,'passed',round(time.time()-started,1),flush=True)
    for k in range(4,kmax+1):
        for m in(3*k+4,3*k+7):
            print('NEW CORE',k,m,round(time.time()-started,1),flush=True)
            labels,bones,stones,old,new=T.core(m,k,2);counts['new_unbounded_core_samples']+=1;counts['core_placements']+=len(bones)+len(stones)
            G.require(len(old)==4*m+12*k+1 and len(new)==len(old)+9,'Uniform edit counts changed')
            for d in(m,m+1):
                ts=T.complete_from_core(d,m,3*k+2);a,b=G.parameters(d,G.triangular(d)-G.triangular(m)+3*k+2)
                G.check_partition(tuple(G.reflect_tile(t)for t in ts),G.region_ab(b,a));counts['unbounded_family_full_and_reflected']+=2;counts['unbounded_placements_with_reflection']+=2*len(ts)
                for p,y,ell,t in labels:G.require(T.receiving(d,m,3*k+2,p,y,ell)[2]==t,'Original receiving generator differs');counts['receiving_generators']+=1
            if k<=5:
                rec=verify_repair(old,new)
                for key,n in rec.items():counts['cohomology_'+key]+=n
                counts['cohomology_complete_comparisons']+=1
    for k in(2,3):
        for r in(1,2):
            q=3*k+r
            for m in(q+2,q+3,q+12):
                labels,bones,stones,old,new=T.core(m,k,r)
                counts['exception_core_samples']+=1
                if m==q+2:
                    rec=verify_repair(old,new)
                    for key,n in rec.items():counts['cohomology_'+key]+=n
                    counts['cohomology_complete_comparisons']+=1
                for d in(m,m+1):
                    ts=T.complete_from_core(d,m,q);counts['exception_full_tilings']+=1;counts['exception_placements']+=len(ts)
    for a in range(2,15):
        for b in range(2,15):
            if a<=2*b and b<=2*a and(a+b)%3==1:
                T.residue_one(a,b);counts['original_residue_one_controls']+=1
    counts['rejection_tests']+=reject(lambda:T.complete_W(3,-1))
    counts['rejection_tests']+=reject(lambda:T.complete_W(3,4))
    counts['rejection_tests']+=reject(lambda:T.complete_W(3.0,1))
    counts['rejection_tests']+=reject(lambda:T.core(15,4,2))
    counts['rejection_tests']+=reject(lambda:T.receiving(16,16,14,0,1,1))
    counts['rejection_tests']+=reject(lambda:T.canonical(-1))
    O.configure();original=json.loads((ROOT/'ownership-certificates.json').read_text());bad=json.loads(json.dumps(original));bad[0]['multipliers'][0]='-1'
    with tempfile.TemporaryDirectory()as td:
        p=Path(td)/'bad.json';p.write_text(json.dumps(bad));counts['rejection_tests']+=reject(lambda:O.verify(p))
        p.write_text(json.dumps(original[:-1]));counts['rejection_tests']+=reject(lambda:O.verify(p))
    labels,bones,stones,old,new=T.core(16,4,2)
    counts['rejection_tests']+=reject(lambda:verify_repair(old,new[:-1]))
    counts['rejection_tests']+=reject(lambda:G.check_partition(bones+stones+stones[:1],G.omega(G.triangular(16)-14)|set(G.incidence(t for *_,t in labels))))
    for delta in range(10000):
        m,q=T.canonical(delta);G.require(G.triangular(m)-q==delta and (delta==0 or 0<=q<=m-2),'Canonical integer inverse failed');T.route(q);counts['canonical_routing_checks']+=1
    files=[p for p in ROOT.rglob('*')if p.is_file()and p.suffix in('.py','.json')and'development'not in p.parts and'evidence'not in p.parts and'__pycache__'not in p.parts and p.name!='recorded-checks.json']
    return {'status':'PASS','date':'2026-09-18','python_optimized':not __debug__,'seconds':round(time.time()-started,3),
            'proved_construction_domain':'All integers d>=2 and 0<=h<=binom(d,2), on original W_h(d); parent residue-one construction also replayed.',
            'finite_window':{'all_h_d_min':2,'all_h_d_max':dmax,'new_k_min':4,'new_k_max':kmax},
            'counts':dict(counts),'routes_exercised':dict(routes),'exact_parameter_proofs':strip_metadata(records),
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in files},
            'scope':'Exact parameter identities and affine certificates plus bounded original-cell replay. Not independent specialist acceptance, a Lean build, a priority claim or an audit of Sharma.'}
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--max-d',type=int,default=12);a.add_argument('--max-k',type=int,default=9);a.add_argument('--skip-parent',action='store_true');a.add_argument('--output',default='evidence/normal.json');args=a.parse_args()
    rec=main(args.max_d,args.max_k,not args.skip_parent);p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps({'status':rec['status'],'seconds':rec['seconds'],'counts':rec['counts']},indent=2))
