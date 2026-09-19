"""Optional rational certificate discovery; verification is exact and separate."""
from fractions import Fraction
import json,numpy as np
from scipy.optimize import linprog
import ownership
import argparse
a=argparse.ArgumentParser();a.add_argument("--k",type=int);a.add_argument("--r",type=int,default=2);arg=a.parse_args();ownership.configure(arg.k,arg.r)
obs,summary=ownership.obligations();out=[]
for n,ob in enumerate(obs):
 r=linprog(np.zeros(len(ob['constraints'])),A_eq=np.array(ob['constraints'],dtype=float).T,b_eq=np.array(ob['target'],dtype=float),bounds=(0,None),method='highs')
 if r.x is None:raise RuntimeError('No certificate for '+ob['name'])
 co=[Fraction(float(x)).limit_denominator(1000000)for x in r.x]
 if min(co)<0 or any(sum(q*row[j]for q,row in zip(co,ob['constraints']))!=ob['target'][j]for j in range(5)):raise RuntimeError('Exact rational reconstruction failed '+ob['name'])
 out.append({'name':ob['name'],'multipliers':list(map(str,co))})
path=ownership.ROOT/f'ownership-certificates{ownership.SUFFIX}.json';path.write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps(ownership.verify(),indent=2))
