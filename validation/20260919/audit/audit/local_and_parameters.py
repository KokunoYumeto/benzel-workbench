"""Independent literal endpoint partitions and integer parameter controls."""
from collections import Counter
from pathlib import Path
import json,sys
from original_cell_check import load_producer,InvalidCertificate
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'frozen/benzel-p7-cumulative-through-turn10/current'
OFF={'R':((0,0),(1,0),(0,1)),'H':((0,0),(1,0),(2,0)),
     'V':((0,0),(0,1),(0,2)),'D':((0,0),(1,-1),(2,-2))}
def tilecells(rows):
    ans=Counter()
    for kind,x,y in rows:
        if kind not in OFF:raise ValueError('unpermitted shape')
        for dx,dy in OFF[kind]:ans[x+dx,y+dy]+=1
    return ans

def alpha(x,y):return [(x,y),(x,y+1),(x+1,y-1)]
def beta(x,y):return [(x,y),(x+1,y),(x+1,y+1)]
def validate_partition(old,new,holes1,holes2):
    lhs=tilecells(old)+Counter(map(tuple,holes1));rhs=tilecells(new)+Counter(map(tuple,holes2))
    if lhs!=rhs or not all(c==1 for c in lhs.values()):raise ValueError('not the same two positive cell partitions')
    return len(lhs)

def canonical_binary(delta):
    if type(delta)is not int or delta<0:raise ValueError('not a nonnegative integer')
    if delta==0:return 1,0
    lo,hi=1,2
    while hi*(hi-1)//2<delta:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid*(mid-1)//2<delta:lo=mid
        else:hi=mid
    return hi,hi*(hi-1)//2-delta

def intended_route(q):
    if q==0:return 'triangular'
    if q in (1,2,4,5):return f'fixed-{q}'
    k,r=divmod(q,3)
    if r==0:return 'threefold'
    if q in (7,8,10,11):return f'exception-k{k}-r{r}'
    if k<4:raise ValueError('uncovered positive deletion count')
    return f'residue-{r}'

def main():
    controls=[]
    old=[('H',0,4),('H',0,5),('H',0,6),('H',1,2),('H',1,3),('H',1,7),('V',0,1),('V',3,4)]
    new=[('V',0,0),('V',0,3),('V',1,0),('V',1,3),('V',2,2),('V',2,5),('V',3,2),('V',3,5)]
    controls.append({'patch':'eight-bone bridge','cells':validate_partition(old,new,beta(0,0),beta(0,6))})
    for k in (2,3):
        a=json.loads((SRC/f'turn10/small-q1-{k}.json').read_text())
        expected=alpha(0,-3)+[(x,y) for kind,x0,y0 in [('R',-3,0),('V',-1,3*k-5)] for dx,dy in OFF[kind] for x,y in [(x0+dx,y0+dy)]]+[(2,3*k-2),(2,3*k-1),(3,3*k-1)]
        if Counter(expected)!=Counter(map(tuple,a['holes'])):raise ValueError('q1 exceptional holes mismatch')
        controls.append({'patch':f'q1, k={k}','cells':validate_partition(a['old'],a['new'],expected,[])})
        b=json.loads((SRC/f'turn10/small-direct-{k}.json').read_text())
        before=alpha(0,-3)+[(-3+dx,dy) for dx,dy in OFF['R']];after=beta(-1,3*k)
        if Counter(before)!=Counter(map(tuple,b['oldholes'])) or Counter(after)!=Counter(map(tuple,b['newholes'])):raise ValueError('q2 exceptional hole description mismatch')
        controls.append({'patch':f'q2, k={k}','cells':validate_partition(b['old'],b['new'],before,after)})
    producer=load_producer();values=set(range(100001))
    for m in (2,3,5,10,10**6,10**12,10**30,10**100):
        for offset in (-2,-1,0,1,2):
            n=m*(m-1)//2+offset
            if n>=0:values.add(n)
    for n in sorted(values):
        if producer.canonical(n)!=canonical_binary(n):raise ValueError('canonical inverse disagreement')
    for q in range(100001):
        if producer.route(q)!=intended_route(q):raise ValueError('dispatcher disagreement')
    rejected=0
    for value in (-1,0.5,True,'1',None):
        try:producer.canonical(value)
        except (ValueError,TypeError):rejected+=1
        else:raise ValueError('producer accepted invalid invariant')
    for d,h in [(1,0),(2,-1),(2,2),(2.0,0),(2,False)]:
        try:producer.complete_W(d,h,check=False)
        except (ValueError,TypeError):rejected+=1
        else:raise ValueError('producer accepted invalid region parameter')
    out={'status':'PASS','original_positive_patch_identities':controls,'integer_inverse_controls':len(values),
         'dispatcher_controls':100001,'invalid_inputs_rejected':rejected,
         'independence':'Partition and inverse checker written independently; literal patch tables are frozen source data. The producer is only the object of comparison.',
         'scope':'Exact local identities and finite implementation controls; general exhaustion is proved in the audit report.'}
    (ROOT/'evidence/local-and-parameters.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
