"""Standard-library replay of original integer Laurent coefficient identities.

Each receipt is a finite sum of numerators over products (1-X^a Y^b).
Exponents in the numerator retain all six independent variables. No parameter
values are chosen, and no floating-point arithmetic or CAS is called.
"""
from collections import Counter
from pathlib import Path
from copy import deepcopy
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[1]

def shift(p,v,scale=1):return {tuple(a+b for a,b in zip(e,v)):scale*c for e,c in p.items()}
def add(a,b):
    z=dict(a)
    for e,c in b.items():
        z[e]=z.get(e,0)+c
        if z[e]==0:del z[e]
    return z

def check(row):
    normalized=[];denominator=Counter()
    for term in row['terms']:
        p={}
        for ee,c in term['numerator']:
            if len(ee)!=6 or any(type(x)is not int for x in ee) or type(c)is not int:raise ValueError('integer Laurent term required')
            e=tuple(ee);p[e]=p.get(e,0)+c
            if p[e]==0:del p[e]
        dd=Counter()
        for raw in term['denominator']:
            if len(raw)!=2 or any(type(x)is not int for x in raw):raise ValueError('original-cell direction required')
            x,y=raw
            if (x,y)==(0,0):raise ValueError('zero denominator')
            if x<0 or (x==0 and y<0):
                x,y=-x,-y
                # 1/(1-z^-1) = -z/(1-z), with the actual monomial z.
                p=shift(p,(x,y,0,0,0,0),-1)
            dd[x,y]+=1
        normalized.append((p,dd));denominator|=dd
    total={};expanded=0
    for p,dd in normalized:
        for (x,y),count in (denominator-dd).items():
            for _ in range(count):p=add(p,shift(p,(x,y,0,0,0,0),-1))
        expanded+=len(p);total=add(total,p)
    if total:raise ValueError('nonzero cleared numerator')
    return {'identity':row['identity'],'integer_terms_after_expansion':expanded,'remaining_coefficients':0}

def main():
    t=time.monotonic();path=ROOT/'evidence/reconstructed-polynomial-identities.jsonl'
    items=[json.loads(x) for x in path.read_text().splitlines()]
    if len({r['identity'] for r in items})!=len(items):raise ValueError('duplicate identity')
    output=[check(row) for row in items]
    broken=deepcopy(items[0]);broken['terms'].append({'numerator':[[[0,0,0,0,0,0],1]],'denominator':[]})
    zero=deepcopy(items[0]);zero['terms'][0]['denominator'].append([0,0])
    for item in (broken,zero):
        try:check(item)
        except ValueError:pass
        else:raise RuntimeError('malformed/nonzero identity accepted')
    receipt={'status':'PASS','identities':len(items),'mutations_rejected':2,'engine':'Python integer exponent dictionaries only',
             'seconds':round(time.monotonic()-t,3),'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'results':output}
    (ROOT/'evidence/polynomial-receipt-check.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
