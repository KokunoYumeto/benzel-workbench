import sys,json
from pathlib import Path
from regular2 import solve_cells,G
base=Path('/mnt/data/benzel-p7-turn8/turn8/exploration')
R={k:set(map(tuple,json.loads((base/f'forced-{k}.json').read_text())['residual']))for k in range(1,11)}
for step in [2,3]:
 possible=[]
 for dx in range(-step,4*step+1):
  for dy in range(-4*step,step+1):
   if all({(x+dx,y+dy)for x,y in R[k-step]}<=R[k]for k in range(step+1,11)):
    possible.append((dx,dy))
 print(step,'possible',possible,flush=True)
 for dx,dy in possible:
  sols=[]
  for k in range(step+1,11):
   patch=R[k]-{(x+dx,y+dy)for x,y in R[k-step]};B=solve_cells(patch,0.8)
   if B is None:break
   sols.append({'k':k,'tiles':G.encode_anchors(B)})
  if sols: print(step,(dx,dy),'solved',[s['k']for s in sols],flush=True)
  if len(sols)==10-step:
   (base/f'annulusR-{step}-{dx}-{dy}.json').write_text(json.dumps({'step':step,'shift':[dx,dy],'solutions':sols}));break
