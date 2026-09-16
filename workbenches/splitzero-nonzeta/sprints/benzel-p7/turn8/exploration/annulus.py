import sys,json
from pathlib import Path
from regular2 import solve_cells,G
base=Path('/mnt/data/benzel-p7-turn8/turn8/exploration')
C={k:set(map(tuple,json.loads((base/f'corner3-{k}.json').read_text())['cells']))for k in range(1,6)}
R={k:set(map(tuple,json.loads((base/f'forced-{k}.json').read_text())['residual']))for k in range(1,7)}
for kind,regions in [('C',C),('R',R)]:
 possible=[]
 for dx in range(-3,6):
  for dy in range(-7,4):
   if all({(x+dx,y+dy)for x,y in regions[k-1]}<=regions[k]for k in range(2,max(regions)+1)):
    possible.append((dx,dy))
 print(kind,'possible',possible,flush=True)
 for dx,dy in possible:
  sols=[]
  for k in range(2,max(regions)+1):
   patch=regions[k]-{(x+dx,y+dy)for x,y in regions[k-1]};B=solve_cells(patch,2)
   if B is None:break
   sols.append({'k':k,'tiles':G.encode_anchors(B)})
  print(kind,(dx,dy),'solved ks',[s['k']for s in sols],flush=True)
  if len(sols)==max(regions)-1:
   (base/f'annulus-{kind}-{dx}-{dy}.json').write_text(json.dumps({'shift':[dx,dy],'solutions':sols}))
