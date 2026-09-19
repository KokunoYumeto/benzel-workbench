"""Univariate-in-m identities for the four exceptional fixed deletion counts."""
from pathlib import Path
import importlib.util,json
import source10 as S
from symbolic_certificate import expr
L=S.L;ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('source9_symbolic',ROOT.parent/'turn9/source_table.py');S9=importlib.util.module_from_spec(spec);spec.loader.exec_module(S9)
def specialize(e,k):
 terms=[]
 for t in e.terms:
  num={}
  for(a,b,c,d,f,g),n in t.num.items():
   v=(a+k*f,b+k*g,c,d,0,0);num[v]=num.get(v,0)+n
  terms.append(L.Term({v:n for v,n in num.items()if n},t.den))
 return L.E(terms)
def verify(k,r):
 src=S9 if r==1 else S;raw=src.identity();raw=raw[0]if isinstance(raw,tuple)else raw
 a=specialize(raw,k).verify_zero();delta=L.E()
 groups=json.loads((ROOT/f'edits-k{k}-r{r}.json').read_text())
 for g in groups:
  for row in g['new']:delta+=expr(row,g['count'])
  for row in g['old']:delta-=expr(row,g['count'])
 residual=src.residual_expr();residual=residual[0]if isinstance(residual,tuple)else residual
 b=specialize(delta-residual,k).verify_zero()
 for x in(a,b):x.pop('proof_domain',None)
 return{'status':'PASS','q':3*k+r,'k':k,'m_min':3*k+r+2,'m_unbounded':True,'scaffold':a,'endpoint':b}
if __name__=='__main__':print(json.dumps([verify(k,r)for k in(2,3)for r in(1,2)],indent=2))
