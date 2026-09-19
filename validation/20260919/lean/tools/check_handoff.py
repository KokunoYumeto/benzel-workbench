#!/usr/bin/env python3
"""Check export fidelity and new finite controls. This cannot mark Lean proved."""
from __future__ import annotations
import argparse,ast,collections,hashlib,importlib.util,json,math,subprocess,sys,tempfile
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'reference/audit_snapshot/frozen/benzel-p7-cumulative-through-turn10/current'
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_generated_data import check as roundtrip
OFF={'R':((0,0),(1,0),(0,1)),'H':((0,0),(1,0),(2,0)),
     'V':((0,0),(0,1),(0,2)),'D':((0,0),(1,-1),(2,-2))}
def req(p,s):
 if not p:raise ValueError(s)
def expanded(rows):
 return collections.Counter((x+u,y+v)for kind,x,y in rows for u,v in OFF[kind])
def evaluate_patch(p):
 a=expanded(p['old']);a.update(map(tuple,p['oldholes']))
 b=expanded(p['new']);b.update(map(tuple,p['newholes']))
 req(a==b and all(n==1 for n in a.values()),'Invalid positive cell partition')
 return len(a)
def producer():
 sys.path.insert(0,str(SRC/'turn10'))
 spec=importlib.util.spec_from_file_location('frozen_complete',SRC/'turn10/complete_theorem.py')
 mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
 return mod

def explicit_tiles(rows):
 return tuple((kind,tuple(sorted((x+u,y+v)for u,v in OFF[kind])))for kind,x,y in rows)


def port_rotate(row):
 kind,x,y=row
 return {'R':('R',y,-x-y),'H':('V',y,-1-x-y),
         'V':('D',y,1-x-y),'D':('H',y-2,1-x-y)}[kind]

def port_reflect(row):
 kind,x,y=row
 return {'R':('R',x,-x-y),'H':('D',x,1-x-y),
         'V':('V',x,-1-x-y),'D':('H',x,1-x-y)}[kind]

def port_one_stone(d):
 h=d*(d-1)//2-1;rows=[]
 for y in range(1,2*h+d+1):
  n=y+1;r=(math.isqrt(8*n+1)-1)//2
  block=r+1 if r*(r+1)//2<n else r
  left=1-2*y-block if y<=h else y-3*h-d+1
  count=y if y<=h else min(h,2*h+d-y)
  for j in range(count):
   for power in range(3):
    t=('H',left+3*j,y)
    for _ in range(power):t=port_rotate(t)
    rows.append(port_reflect(t))
 return explicit_tiles(rows+[('R',0,0)])

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',default='evidence/handoff-checks.json');args=ap.parse_args()
 rt=roundtrip();patches=json.loads((ROOT/'evidence/local-patches.json').read_text())
 patch_records=[{'name':p['name'],'cells':evaluate_patch(p)}for p in patches]
 mod=producer();G=mod.G;P=mod.P
 centered=[];placement_total=0;band_steps=0;coordinate_checks=0
 for kind in OFF:
  for x in range(-5,6):
   for y in range(-5,6):
    t=G.tile(kind,x,y)
    req(G.rotate_tile(t)==explicit_tiles([port_rotate((kind,x,y))])[0],'Lean rotation formula differs from original cells')
    req(G.reflect_tile(t)==explicit_tiles([port_reflect((kind,x,y))])[0],'Lean reflection formula differs from original cells')
    coordinate_checks+=2
 for d in range(3,13):
  h=d*(d-1)//2-1
  t=P.one_stone_transport(d)
  canonical=mod.complete_W(d,h,check=True)
  req(collections.Counter(t)==collections.Counter(canonical),'Two one-stone constructors differ')
  req(collections.Counter(port_one_stone(d))==collections.Counter(canonical),'Handwritten Lean candidate formulas differ from frozen construction')
  rs=[x for x in t if x[0]=='R'];req(rs==[G.tile('R',0,0)],'Not the original central stone')
  req(set(map(G.rotate_tile,t))==set(t),'Original rotation did not preserve tiling')
  # Independently expand the stated Sharma last candidate. No use of his proof's conclusions.
  s=h;r=d-2;c=0
  a=(-d-2*s+2+2*c+r,d+s-2-c-2*r,s-c+r)
  req(a==(-2*s,s-d+2,s+d-2) and sum(a)==0,'Incorrect source-parameter map')
  sharma=[(a[0]+1,a[1],a[2]),(a[0],a[1]+1,a[2]),(a[0],a[1],a[2]+1)]
  central={(1,0,0),(0,1,0),(0,0,1)}
  req(set(sharma)!=central,'Distinctness witness failed')
  for rr,p,old,new in P.one_stone_bands(d):
   # Signed Counter subtraction by .subtract retains the negative old coefficients.
   ch=collections.Counter(new);ch.subtract(old)
   actual=G.chain_boundary(ch)
   y=rr*(rr+1)//2
   start=((rr+1)*(rr+2)//2,y);end=(1-rr*rr,y)
   for _ in range(p):start=G.rho(start);end=G.rho(end)
   expected=collections.Counter({start:1});expected[end]-=1
   req(actual=={x:n for x,n in expected.items()if n},'Band endpoint identity failed')
   band_steps+=1
  placement_total+=len(t)
  centered.append({'d':d,'h':h,'a':d+3*h,'b':2*d+3*h,'our_stone_anchor_barycentric':[0,0,0],
    'sharma_last_stone_anchor_barycentric':list(a),'sharma_stone_cells_barycentric':sharma,
    'same_original_region':True,'our_rotational_symmetry_checked':True,'tile_count':len(t)})
 # Recompute the right endpoint code's small literal d=2 certificate.
 seed=G.encode_anchors(mod.complete_W(2,1,check=True))
 req(len(seed)==9 and all(x[0]!='R'for x in seed),'d=2 seed mismatch')
 # Rejection controls are real failing inputs, not unconditional flags.
 rejected=0
 for changed in ['drop_old','duplicate_new','left_shape','move_hole']:
  bad=json.loads(json.dumps(patches[0]))
  if changed=='drop_old':bad['old']=bad['old'][1:]
  if changed=='duplicate_new':bad['new'].append(bad['new'][0])
  if changed=='left_shape':bad['new'][0][0]='L'
  if changed=='move_hole':bad['oldholes'][0][0]+=9
  try:evaluate_patch(bad)
  except (ValueError,KeyError):rejected+=1
  else:raise ValueError('Invalid patch accepted')
 # Confirm main Python tools parse; external reference files are untouched.
 for p in (ROOT/'tools').glob('*.py'):ast.parse(p.read_text(),str(p))
 details={'status':'PASS','scope':'Local export tests and bounded mathematical controls only; not Lean elaboration',
  'lean_compilation':'NOT_RUN','python_optimized':not __debug__,'roundtrip':rt,
  'patches':patch_records,'one_stone_parameter_values':len(centered),'one_stone_placements':placement_total,
  'band_homotopies':band_steps,'rejected_bad_patches':rejected,
  'handwritten_coordinate_formula_checks':coordinate_checks,
  'candidate_formula_comparison':'Evaluated independently in Python, not by Lean'}
 out=ROOT/args.output;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(details,indent=2)+'\n')
 (ROOT/'evidence/parallel-construction.json').write_text(json.dumps({'scope':'Formula comparison and finite replay; no audit of the other author\'s full proof','cases':centered},indent=2)+'\n')
 (ROOT/'evidence/d2-nine-bone-seed.json').write_text(json.dumps(seed,indent=2)+'\n')
 print(json.dumps(details,indent=2))
if __name__=='__main__':main()
