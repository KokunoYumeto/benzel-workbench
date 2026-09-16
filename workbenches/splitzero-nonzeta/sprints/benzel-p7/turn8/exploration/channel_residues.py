from remainder_residues import *

def channels(k,r,m):
 old=[];new=[]
 if r==1:
  for i in range(m-3*k-3):
   x=3*k+3+i;y=1-m+i
   old += [G.tile('V',x,y),G.tile('V',x,y+3)]
   new += [G.tile('D',x-2,y+2),G.tile('D',x-2,y+3)]
 else:
  for i in range(m-3*k-1):
   x=3*k+3+i;y=1-m+i
   old.append(G.tile('V',x,y));new.append(G.tile('H',x-1,y+1))
  for i in range(m-3*k-3):
   x=3*k-m+2*i;y=m-1-i
   old.append(G.tile('H',x,y));new.append(G.tile('D',x,y+1))
 return old,new

def setup_channel(k,r,m):
 rem,A,S,B,info=setup(k,r,m)
 R=rem|set(G.incidence(B));old,new=channels(k,r,m)
 if not set(old)<=set(B):return None,{'missing_old':G.encode_anchors(set(old)-set(B))}
 if not set(G.incidence(new))<=R:return None,{'outside_new':sorted(set(G.incidence(new))-R)}
 G.require(max(G.incidence(new).values(),default=0)<=1,'Channels overlap')
 keep=[t for t in B if not set(t[1])&set(G.incidence(new))]
 fixed=keep+new;rem=R-set(G.incidence(fixed))
 centers=[(0,1-m),(1-m,m),(m,0)]
 parts=[{z for z in rem if max(abs(z[0]-c[0]),abs(z[1]-c[1]),abs(sum(z)-sum(c)))<10*k+10}for c in centers]
 inf={'k':k,'r':r,'m':m,'components':[len(c)for c in components(rem)],'residual':len(rem),'cornerjets':[(len(p)%3,sum(x for x,y in p)%3,sum(y for x,y in p)%3)for p in parts]}
 return(rem,A,S,fixed),inf

if __name__=='__main__':
 for k in range(1,7):
  for r in [1,2]:
   for m in [3*k+r+2,8*k+10,30*k+10]:
    data,info=setup_channel(k,r,m)
    if data is None:info={z:len(v) for z,v in info.items()}
    print(k,r,m,info,flush=True)
