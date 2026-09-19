#!/usr/bin/env python3
"""Fail-closed replay of the positive asymmetric continuation."""
from __future__ import annotations
from pathlib import Path
from collections import Counter
import argparse,json,time,sys,hashlib
import core,source_table,ownership,symbolic_certificate
G=core.G
ROOT=Path(__file__).resolve().parent

def ev(a,m,k,i=0):return a[0]*m+a[1]*k+a[2]*i+a[3]
def expanded_edits(k,m):
 old=[];new=[]
 for g in json.loads((ROOT/'edits.json').read_text()):
  num=g['count'][0]*m+g['count'][1]*k+g['count'][2]
  G.require(num>=0,'Negative indexed family')
  for i in range(num):
   old.extend(G.tile(c,ev(x,m,k,i),ev(y,m,k,i))for c,x,y in g['old'])
   new.extend(G.tile(c,ev(x,m,k,i),ev(y,m,k,i))for c,x,y in g['new'])
 return old,new

def run(max_k):
 t=time.monotonic();summary={'status':'RUNNING','python_optimized':not __debug__,'domain':'k>=4,m>=3k+3,d>=m; q=3k+1','symbolic':symbolic_certificate.verify(),'source_ownership':ownership.verify()}
 counts=Counter();cases=[]
 for k in range(4,max_k+1):
  for m in sorted({3*k+3,3*k+4,4*k+7}):
   old,new=expanded_edits(k,m);stages=list(core.stages(k,m))
   G.require(Counter(old)==Counter(t for _,_,a,b in stages for t in a),'Literal/ordered old tables disagree')
   G.require(Counter(new)==Counter(t for _,_,a,b in stages for t in b),'Literal/ordered new tables disagree')
   G.require(len(old)==2*m+6*k-2 and len(new)==2*m+6*k+4,'Exact transport counts')
   G.require(len(set(old))==len(old),'Repeated old generator')
   common,bones,stones=core.core(k,m)
   delta=G.triangular(m)-3*k-1
   G.require(len(stones)==delta,'Original right-stone count')
   counts['positive_cores']+=1;counts['old_generator_receivers']+=len(old)
   counts['edit_groups_expanded']+=len(stages)
   for d in[m,m+1]:
    tiles=core.complete(d,m,k);h=G.triangular(d)-delta
    G.require(sum(x[0]=='R'for x in tiles)==delta,'Full original stone count')
    G.require(sum(x[0]!='R'for x in tiles)==3*h*(h+d),'Full original bone count')
    refl=tuple(G.reflect_tile(x)for x in tiles);G.check_partition(refl,G.region_ab(2*d+3*h,d+3*h))
    counts['full_tilings_with_reflections']+=2;counts['full_tile_placements_with_reflections']+=2*len(tiles)
    cases.append({'k':k,'m':m,'d':d,'h':h,'a':d+3*h,'b':2*d+3*h,'right_stones':delta,'bones':3*h*(h+d)})
 # Original signed cochain identities for each local patch; no fitted parameters.
 A=lambda x,y:{(x,y),(x,y+1),(x+1,y-1)}
 B=lambda x,y:{(x,y),(x+1,y),(x+1,y+1)}
 R=lambda x,y:set(G.tile('R',x,y)[1])
 for x,y in[(0,0),(-7,11),(13,-9)]:
  for kind,holes,dx,dy in[('D',A,1,1),('U',A,0,3),('R',R,3,0),('B',B,0,3)]:
   old,new=map(core.as_tiles,core.move(kind,x,y));G.require(G.incidence(old)+Counter(holes(x,y))==G.incidence(new)+Counter(holes(x+dx,y+dy)),'Original local homotopy');counts['local_homotopy_identities']+=1
 # Deliberate invalid mathematical inputs and a false incidence equation.
 rejected=0
 for call in[lambda:core.core(3,20),lambda:core.core(4,14),lambda:core.complete(14,15,4),lambda:G.check_partition([G.tile('V',0,0)],{(0,0)})]:
  try:call()
  except (ValueError,AssertionError,RuntimeError):rejected+=1
  else:raise ValueError('Invalid input accepted')
 counts['rejection_tests']=rejected
 summary.update(status='PASS',seconds=round(time.monotonic()-t,3),counts=dict(counts),finite_k_range=[4,max_k],cases=cases,
  mathematical_scope='Unbounded Laurent and affine-certificate proof plus separately bounded original-cell replay. Not a full P7 resolution or an independent specialist/Lean certificate.',
  source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in sorted(ROOT.iterdir())if p.is_file()and p.suffix in('.py','.json')and p.name!='recorded-checks.json'})
 return summary
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--max-k',type=int,default=10);p.add_argument('--output',default='evidence/normal.json');a=p.parse_args()
 G.require(a.max_k>=4,'Empty replay scope')
 try:r=run(a.max_k)
 except Exception as e:
  out=ROOT/a.output;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps({'status':'FAIL','error':repr(e)},indent=2)+'\n');raise
 out=ROOT/a.output;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k not in('cases','source_sha256')},indent=2))
