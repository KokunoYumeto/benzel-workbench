from force_residue_corner import *
from local_residue_search import exact_cells
for k in [1,2,3,4,5,6]:
 m=30*k+10;data,info=setup_channel(k,1,m);rem,A,S,old=data;center=(0,1-m);rad=8*k+6
 dist=lambda z:max(abs(z[0]),abs(z[1]-center[1]),abs(sum(z)-center[1]))
 holes={z for z in rem if dist(z)<=rad};cap=[G.tile('H',3*k-2+j,2-j-m)for j in range(3)];cc=set(G.incidence(cap))
 take={t for t in old if(t[0]=='V'and any(dist(z)<=rad for z in t[1]))or set(t[1])&cc}
 target=(holes|set(G.incidence(take)))-cc
 F,left,ok=force(target)
 comps=components(left)
 print(k,len(left),'components',[(len(c),max(x for x,y in c)-min(x for x,y in c)+1,max(x+y for x,y in c)-min(x+y for x,y in c)+1)for c in comps],flush=True)
 D,stat=exact_cells(left,200000)
 print('exact',stat, len(D)if D else None,flush=True)
 if D:
  full=cap+F+list(D);G.check_partition(full,holes|set(G.incidence(take)))
  (ROOT/'exploration'/f'forced-all-r1p0-{k}.json').write_text(json.dumps({'k':k,'m':m,'remove':G.encode_anchors(take-set(full)),'add':G.encode_anchors(set(full)-take)}))
