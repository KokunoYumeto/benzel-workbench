from small_endpoints import *
import source10
sys.path.insert(0,str(ROOT.parent/'turn9'));import source_table as S9
for k in(2,3):
 for r in(1,2):
  groups=json.loads((ROOT/f'edits-k{k}-r{r}.json').read_text())
  for m in range(3*k+r+2,3*k+r+23):
   states,stones,holes,common,a0=initial(k,m,r)
   tab={t for *_,t in (S9 if r==1 else source10).labels(m,k)}
   assert tab==a0,('A0 mismatch',k,m,r,G.encode_anchors(tab-a0),G.encode_anchors(a0-tab))
   for g in groups:
    n=g['count'][0]*m+g['count'][1]*k+g['count'][2]
    for i in range(n):
     old=tuple(expand(row,m,k,i)for row in g['old']);new=tuple(expand(row,m,k,i)for row in g['new'])
     try:apply(states,holes,old,new)
     except AssertionError as e:raise AssertionError((k,m,r,g['name'],i,e))
   assert not holes,('remaining',k,m,r,holes)
   G.check_partition(tuple(states)+stones,G.omega(G.triangular(m)-3*k-r)|set(G.incidence(common)))
  print('PASS',k,r,'m',3*k+r+2,'..',3*k+r+22,flush=True)
