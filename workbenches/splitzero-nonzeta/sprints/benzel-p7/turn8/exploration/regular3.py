from regular2 import *
import json,sys

def calc(k,margin=8):
 q=3*k;K=2*k-1;m=60*k+5
 A=body(m,q,K)
 removed={G.rotate_tile(G.tile('R',m-2-a,-a),p)for a in range(k)for p in range(3)}
 count=G.incidence(A);count.update(G.incidence(removed))
 M={p for j in range(q)for p in G.orbit((q-j,q+1-m-j))}
 for p in M:count[p]-=1
 G.require(all(v in (0,1)for v in count.values()),'Original signed cell coefficients are not a support')
 R={p for p,v in count.items()if v}
 B=[G.rotate_tile(G.tile('H',y+m+3*ell,y),p)for ell in range(k)for y in range(2-m+k-1-ell,1-2*k)for p in range(3)]
 cov=G.incidence(B);G.require(max(cov.values())==1 and set(cov)<=R,'Bad long strips')
 centers=G.orbit((0,1-m))
 def near(t):return any(max(abs(x-cx),abs(y-cy),abs(x+y-cx-cy))<=margin*k for x,y in t[1]for cx,cy in centers)
 covset=set(cov)
 keep=[t for t in A if not near(t) and not(set(t[1])&covset)]
 cov.update(G.incidence(keep));G.require(max(cov.values())==1,'Keep overlapping')
 remain=R-set(cov);C={(x,y+m)for x,y in remain if y<-m//2}
 G.require(len(remain)==3*len(C),'Not corner separated')
 return C,{'k':k,'K':K,'margin':margin,'C':len(C),'kept':len(keep),'long':len(B)}
if __name__=='__main__':
 k=int(sys.argv[1]);C,inf=calc(k);print(inf,flush=True);B=solve_cells(C,20);print('SOLVE',B is not None)
 if B:open(f'/mnt/data/benzel-p7-turn8/turn8/exploration/corner3-{k}.json','w').write(json.dumps({**inf,'cells':sorted(C),'tiles':G.encode_anchors(B)}))
