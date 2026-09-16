from repair_residues import *
if __name__=='__main__':
 for k in [1,2,3,4]:
  for r in [1,2]:
   m=15*k+10;rem,A,S,B,info=setup(k,r,m)
   cells=set(rem)|set(G.incidence(B));new,inf=solve_patch(cells,set(B),25)
   print(k,r,m,inf,flush=True)
   if new is not None:
    G.check_partition(tuple(new)+tuple(S),set(G.omega(G.triangular(m)-3*k-r))|set(G.incidence(A)))
    (ROOT/'exploration'/f'global-r{r}-k{k}.json').write_text(json.dumps({'k':k,'r':r,'m':m,'info':inf,'remove':G.encode_anchors(set(B)-set(new)),'add':G.encode_anchors(set(new)-set(B)),'new':G.encode_anchors(new)}))
