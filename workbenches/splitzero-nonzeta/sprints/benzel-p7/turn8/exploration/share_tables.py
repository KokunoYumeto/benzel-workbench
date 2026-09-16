import sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import bivariate_certificate as B
orig=B.family
specs={}
for key,fn in [('source',B.source_sector),('corner',B.corner)]:
 rows=[]
 def capture(kind,x,y,I,J=None):
  rows.append({'kind':kind,'x':x,'y':y,'I':I,'J':J});return B.E()
 B.family=capture;fn();specs[key]=rows
B.family=orig
specs['long']=[{'kind':'H','x':[0,1,2,1,1],'y':[-1,1,-1,1,1],'I':[0,1,0],'J':[1,-3,0,1]}]
specs['deleted']=[{'kind':'R','x':[1,0,-1,0,-2],'y':[0,0,-1,0,0],'I':[0,1,0],'J':None}]
specs['schema']={'anchor_coefficients':['m','k','i','j','constant'],'I_coefficients':['m','k','constant'],'J_coefficients':['m','k','constant','i'],'domain':'integer k>=2, m>=3*k+2','kind':'literal placed R/H/V/D','k1':'Separate explicit four-tile corner; same actual source-label and long-strip formulas.'}
(ROOT/'families.json').write_text(json.dumps(specs,indent=2)+'\n')
