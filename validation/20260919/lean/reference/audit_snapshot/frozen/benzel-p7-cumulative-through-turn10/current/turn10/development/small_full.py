from small_endpoints import *

def find_q1(k,m,rad):
 states,stones,holes=beforelower(k,m,1);c,b=m+2*k-4,1-k
 xlo=min(x for x,y in holes)-rad;xhi=max(x for x,y in holes)+rad
 ylo=min(y for x,y in holes)-rad;yhi=max(y for x,y in holes)+rad
 select={t for t in states if any(xlo<=x<=xhi and ylo<=y<=yhi for x,y in t[1])}
 out=cover(set(G.incidence(select))|holes,select,10)
 if not out:return
 rel=lambda ts:[[kind,G.anchor((kind,cs))[0]-c,G.anchor((kind,cs))[1]-b]for kind,cs in sorted(ts)]
 return {'k':k,'old':rel(select-set(out)),'new':rel(set(out)-select),'holes':[[x-c,y-b]for x,y in sorted(holes)]}

def find_q2(k,m,seconds=20):
 states,stones,holes,common,a0=initial(k,m,2)
 target=G.omega(G.triangular(m)-3*k-2)|set(G.incidence(common));target-=set(G.incidence(stones))
 out=cover(target,states,seconds)
 if not out:return None
 return {'k':k,'m':m,'old':G.encode_anchors(states-set(out)),'new':G.encode_anchors(set(out)-states),'bone_count':len(out)}
if __name__=='__main__':
 for k in [3,2]:
  for rad in [1,2,3,4]:
   ans=find_q1(k,3*k+3,rad);print('q1',k,rad, bool(ans),flush=True)
   if ans:
    (ROOT/f'small-q1-{k}.json').write_text(json.dumps(ans,indent=2));print(json.dumps(ans),flush=True);break
 for k in [2,3]:
  ans=find_q2(k,3*k+4,12);print('q2',k,bool(ans),flush=True)
  if ans:(ROOT/f'small-q2-full-{k}.json').write_text(json.dumps(ans,indent=2));print('edits',len(ans['old']),len(ans['new']),flush=True)
