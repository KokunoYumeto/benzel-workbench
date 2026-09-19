"""Small standard-library checker for the independently reconstructed identities."""
from pathlib import Path
from fractions import Fraction
import json,copy
ROOT=Path(__file__).resolve().parents[1]

def accept(row):
    A=row['constraints'];b=row['target'];lam=[Fraction(x) for x in row['multipliers']]
    if len(A)!=len(lam) or len(b)!=5 or any(len(a)!=5 for a in A):raise ValueError('dimension mismatch')
    if any(type(x)is not int for a in A for x in a) or any(type(x)is not int for x in b):raise ValueError('noninteger affine coefficient')
    if any(c<0 for c in lam):raise ValueError('negative coefficient')
    got=[sum(c*a[j] for c,a in zip(lam,A)) for j in range(5)]
    if got!=b:raise ValueError('false rational identity')

def main():
    rows=[json.loads(line) for line in (ROOT/'evidence/reconstructed-linear-identities.jsonl').read_text().splitlines()]
    names=set()
    for row in rows:
        key=(row['file'],row['name'])
        if key in names:raise ValueError('duplicated certificate association')
        names.add(key);accept(row)
    tests=[]
    bad=copy.deepcopy(rows[0]);bad['multipliers'][0]='-1';tests.append(bad)
    bad=copy.deepcopy(rows[0]);bad['target'][-1]+=1;tests.append(bad)
    bad=copy.deepcopy(rows[0]);bad['constraints'].pop();tests.append(bad)
    for bad in tests:
        try:accept(bad)
        except ValueError:pass
        else:raise RuntimeError('bad certificate accepted')
    result={'status':'PASS','exact_affine_identities':len(rows),'mutation_rejections':len(tests),'external_libraries':False}
    (ROOT/'evidence/linear-receipt-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
