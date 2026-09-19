"""Separate checker for outputs of the frozen benzel constructor.

No producer geometry, area, incidence, shape or checking routine is used here.
The only producer API called is complete_W (or residue_one) to obtain tiles.
Coordinates are reinterpreted as triples of sum one, and coverage is compared
against independently derived integer row intervals of the six original bounds.
"""
from __future__ import annotations
from collections import defaultdict, Counter
from pathlib import Path
import argparse, hashlib, importlib.util, json, sys, time

ROOT = Path(__file__).resolve().parents[1]
FROZEN = ROOT/'frozen/benzel-p7-cumulative-through-turn10/current'
class InvalidCertificate(Exception): pass

def need(condition, message):
    if not condition: raise InvalidCertificate(message)

def ceildiv(a,b): return -((-a)//b)

def independent_rows(a:int,b:int):
    """The original row at first barycentric coordinate i, without area formula."""
    need(type(a) is int and type(b) is int and min(a,b)>=2 and a<=2*b and b<=2*a,'admissible original benzel')
    low,high=1-a,b-1
    # i=(1-(j-i)+(i-k))/3 follows from i+j+k=1.
    for i in range(ceildiv(1+low-high,3),(1+high-low)//3+1):
        lower=max(i+low,ceildiv(1-i-high,2),low+1-2*i)
        upper=min(i+high,(1-i-low)//2,high+1-2*i)
        if lower<=upper: yield i,lower,upper

DIRECTIONS={'H':(-1,0,1),'V':(0,1,-1),'D':(1,-1,0)}

def verify_tiles(tiles,a,b):
    rows=defaultdict(list);counts=Counter();ntiles=0
    for label, raw in tiles:
        need(label in ('R','H','V','D'),'unpermitted tile label')
        need(len(raw)==3,'tile must contain exactly three cells')
        need(all(len(c)==2 and all(type(v) is int for v in c) for c in raw),'literal integer cell pairs required')
        triples=tuple((i,j,1-i-j) for i,j in raw)
        need(len(set(triples))==3,'three distinct original cells required')
        if label=='R':
            anchor=tuple(min(c[t] for c in triples) for t in range(3))
            expected={tuple(anchor[t]+(t==s) for t in range(3)) for s in range(3)}
            need(sum(anchor)==0 and set(triples)==expected,'not an original right-pointing stone')
        else:
            total=tuple(sum(c[t] for c in triples) for t in range(3))
            need(all(v%3==0 for v in total),'bone center is not an original cell')
            center=tuple(v//3 for v in total); direction=DIRECTIONS[label]
            expected={tuple(center[t]+u*direction[t] for t in range(3)) for u in (-1,0,1)}
            need(set(triples)==expected,'not an allowed centered original bone')
        counts[label]+=1;ntiles+=1
        for i,j,k in triples:
            need(all(1-a<=v<=b-1 for v in (j-i,k-j,i-k)),f'outside original region: {(i,j,k)}')
            rows[i].append(j)
    actual_area=0
    expected_keys=set()
    for i,lo,hi in independent_rows(a,b):
        expected_keys.add(i);values=sorted(rows.get(i,()))
        need(len(values)==hi-lo+1,f'row cardinality mismatch at i={i}')
        # This comparison detects both holes and collisions, not just cardinality.
        need(all(j==lo+r for r,j in enumerate(values)),f'cell multiplicity mismatch at i={i}')
        actual_area+=hi-lo+1
    need(set(rows)==expected_keys,'extra or absent original rows')
    need(actual_area==3*ntiles,'independent row count not equal tile area')
    return {'tiles':ntiles,'cells':actual_area,'stones':counts['R'],'bones':ntiles-counts['R']}

def reflect_output(tiles):
    # Exact coordinate transposition (i,j,k)->(i,k,j), independently applied.
    swap={'R':'R','H':'D','V':'V','D':'H'}
    return tuple((swap[t],tuple((i,1-i-j) for i,j in cs)) for t,cs in tiles)

def mutation_checks():
    base=(('R',((0,0),(1,0),(0,1))),)
    verify_tiles(base,2,4)
    invalid=[(),base+base,(('R',((0,0),(0,0),(0,1))),),
             (('H',base[0][1]),),(('R',((1,0),(0,1),(1,1))),),
             (('R',((0,0),(1.0,0),(0,1))),),
             (('X',base[0][1]),),(('R',((10,10),(11,10),(10,11))),)]
    for item in invalid:
        try: verify_tiles(item,2,4)
        except InvalidCertificate: pass
        else: raise RuntimeError('A deliberately bad certificate was accepted')
    return len(invalid)

def load_producer():
    sys.path.insert(0,str(FROZEN/'turn10'))
    spec=importlib.util.spec_from_file_location('producer_under_audit',FROZEN/'turn10/complete_theorem.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-d',type=int,default=20);ap.add_argument('--output',type=Path,default=ROOT/'evidence/original-cells.json');args=ap.parse_args()
    start=time.monotonic();producer=load_producer();records=[];counts=Counter();counts['checker_mutations_rejected']=mutation_checks()
    cases=[]
    for d in range(2,args.max_d+1):
        for h in range(d*(d-1)//2+1):cases.append((d,h,'all-h'))
    # Independently generate canonical (m,q) edge cases and exterior-tail cases.
    for k in (4,5,6,9,13,20,31):
        for r in (0,1,2):
            q=3*k+r
            for mo in (0,3):
                m=q+2+mo
                for do in (0,1):
                    d=m+do;h=d*(d-1)//2-m*(m-1)//2+q
                    cases.append((d,h,'large-canonical'))
    seen=set()
    for d,h,group in cases:
        if (d,h) in seen:continue
        seen.add((d,h));tiles=producer.complete_W(d,h,check=False)
        a,b=d+3*h,2*d+3*h;stats=verify_tiles(tiles,a,b)
        need(stats['stones']==d*(d-1)//2-h,'original invariant count')
        need(stats['bones']==3*h*(h+d),'original bone count')
        reflected=verify_tiles(reflect_output(tiles),b,a)
        need(stats==reflected,'reflection did not preserve actual tiling counts')
        counts[group+'_original']+=1;counts[group+'_with_reflections']+=2
        counts['placements']+=2*stats['tiles'];counts['cell_incidences']+=2*stats['cells']
        records.append({'d':d,'h':h,'a':a,'b':b,'group':group,**stats})
        if len(records)%50==0:print('checked',len(records),'last',d,h,'seconds',round(time.monotonic()-start,1),flush=True)
    # The nonzero congruence-class constructor has its own direct original check.
    for a in range(2,41):
        for b in range(a,2*a+1):
            if (a+b)%3!=1:continue
            tiles=producer.residue_one(a,b);stats=verify_tiles(tiles,a,b)
            need(stats['bones']==0,'residue-one contains a bone')
            verify_tiles(reflect_output(tiles),b,a)
            counts['residue_one_with_reflections']+=2;counts['placements']+=2*stats['tiles'];counts['cell_incidences']+=2*stats['cells']
    result={'status':'PASS','audit_date':'2026-09-18','seconds':round(time.monotonic()-start,3),
            'counts':dict(counts),'records':records,
            'independence':'Output validity checker independently written; producer used only to generate candidate tile lists. No producer geometry/incidence/coverage routine used for acceptance.',
            'scope':'Exact finite certificate checks; no finite test is represented as a proof for unbounded parameters.'}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
if __name__=='__main__':main()
