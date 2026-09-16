"""Optional certificate discovery. The final verifier uses only exact fractions.

Requires NumPy/SciPy; their feasibility statuses are never mathematical certificates.
"""
from fractions import Fraction
import json
import numpy as np
from scipy.optimize import linprog
import ownership
obs,summary=ownership.obligations();out=[]
for n,ob in enumerate(obs):
 A=np.asarray(ob['constraints'],dtype=float).T;b=np.asarray(ob['target'],dtype=float)
 r=linprog(np.ones(A.shape[1]),A_eq=A,b_eq=b,bounds=(0,None),method='highs')
 if r.x is None:raise RuntimeError('No exact certificate found for '+ob['name']+' '+str(ob))
 coeff=[Fraction(float(x)).limit_denominator(1000000)for x in r.x]
 if any(x<0 for x in coeff)or any(sum(c*row[j]for c,row in zip(coeff,ob['constraints']))!=ob['target'][j]for j in range(5)):raise RuntimeError('Rational reconstruction failed '+ob['name'])
 out.append({'name':ob['name'],'multipliers':[str(x)for x in coeff]})
path=ownership.Path(__file__).with_name('ownership-certificates.json');path.write_text(json.dumps(out,separators=(',',':'))+'\n');print(ownership.verify())
