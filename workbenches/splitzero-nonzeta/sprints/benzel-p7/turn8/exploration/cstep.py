from regular2 import G,solve_cells
from regular3 import calc
from pathlib import Path
import json,time
ROOT=Path('/mnt/data/benzel-p7-turn8/turn8/exploration')
C={k:set(map(tuple,json.loads((ROOT/f'forced-{k}.json').read_text())['full']))for k in range(1,11)}
for step in [3,6]:
 for k in range(1,5):
  outer=C[k+step];inner={(x,y-3*step)for x,y in C[k]}
  if not inner<=outer:print('notnested',step,k);continue
  target=outer-inner;start=time.monotonic();B=solve_cells(target,6)
  print('STEP',step,'k',k,'size',len(target),'solved',B is not None,'time',time.monotonic()-start,flush=True)
  if B:(ROOT/f'Cstep-{step}-{k}.json').write_text(json.dumps({'k':k,'step':step,'shift':[0,-3*step],'tiles':G.encode_anchors(B)}))
