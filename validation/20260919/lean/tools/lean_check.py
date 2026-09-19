#!/usr/bin/env python3
"""Run real Lean checking; refuse to promote a scaffold to a completed proof.
Exit 0 means only the requested stage passed. Exit 2 means a prerequisite is
missing; it is never reported as a mathematical success.
"""
from __future__ import annotations
import argparse,hashlib,json,re,shutil,subprocess,sys,tomllib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];FORMAL=ROOT/'formal'
EXPECTED_MATHLIB='fabf563a7c95a166b8d7b6efca11c8b4dc9d911f'
ALLOWED={'propext','Quot.sound','Classical.choice'}
BASE_TARGETS=['Benzel.from_toBary','Benzel.to_fromBary','Benzel.reflect_mem_iff',
 'Benzel.rotate_mem_iff','Benzel.twice_triangular','Benzel.boundary_listChain',
 'Benzel.last_staircase_anchor','Benzel.center_not_last_staircase',
 'Benzel.Generated.bridgeSix_partition','Benzel.Generated.bridgeSix_old_nodup',
 'Benzel.Generated.bridgeSix_new_nodup','Benzel.Generated.bridgeSix_translated',
 'Benzel.bridgeSix_boundary','Benzel.Certificate.combination_nonnegative',
 'Benzel.channel_low_original_owner','Benzel.channel_low_domain',
 'Benzel.fixed_right_anchor','Benzel.originalCL_numerator']

def strip_comments(s):
 # Preserve strings, support nested Lean block comments, do not trust a regex over comments.
 out=[];i=0;depth=0;string=False
 while i<len(s):
  if depth:
   if s.startswith('/-',i):depth+=1;i+=2
   elif s.startswith('-/',i):depth-=1;i+=2
   else:i+=1
  elif string:
   out.append(s[i])
   if s[i]=='\\' and i+1<len(s):out.append(s[i+1]);i+=2;continue
   if s[i]=='"':string=False
   i+=1
  elif s.startswith('/-',i):depth=1;out.append(' ');i+=2
  elif s.startswith('--',i):
   j=s.find('\n',i);i=len(s)if j<0 else j;out.append('\n')
  else:
   if s[i]=='"':string=True
   out.append(s[i]);i+=1
 if depth or string:raise ValueError('Unclosed comment/string')
 return ''.join(out)

def static_checks():
 lock=json.loads((ROOT/'SPEC_LOCK.json').read_text())
 for rel,digest in lock.items():
  if hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()!=digest:raise ValueError('Locked original specification changed: '+rel)
 for p in FORMAL.rglob('*.lean'):
  if '.lake' in p.parts or p.name in('Audit.Generated.lean','Release.Generated.lean'):continue
  if p.name.startswith('SplitZero'):continue  # separately byte-pinned upstream; audited transitively by Lean
  s=strip_comments(p.read_text())
  forbidden=[r'\bsorry\b',r'\badmit\b',r'\baxiom\b',r'\bunsafe\b',r'\bnative_decide\b',
    r'\bsorryAx\b',r'Lean\.ofReduceBool',r'Lean\.trustCompiler',r'debug\.skipKernelTC',
    r'\bimplemented_by\b',r'\bextern\b']
  for pat in forbidden:
   if re.search(pat,s):raise ValueError(f'Forbidden proof escape in {p.relative_to(ROOT)}: {pat}')
  if re.search(r'set_option\s+\S*(?:trust|kernel|Kernel)\S*',s):raise ValueError('Unexpected trust option')
 if (FORMAL/'lean-toolchain').read_text().strip()!='leanprover/lean4:v4.31.0':raise ValueError('Toolchain drift')
 cfg=tomllib.loads((FORMAL/'lakefile.toml').read_text())
 if not any(r.get('name')=='mathlib'and r.get('rev')==EXPECTED_MATHLIB for r in cfg.get('require',[])):
  raise ValueError('Mathlib source pin changed')
 return {'status':'PASS','meaning':'Specification hashes and source-policy scan only'}

def run(cmd,log):
 proc=subprocess.run(cmd,cwd=FORMAL,text=True,capture_output=True)
 log.write_text(proc.stdout+proc.stderr)
 if proc.returncode:raise RuntimeError('Command failed; see '+str(log.relative_to(ROOT)))
 return proc.stdout+proc.stderr

def audit_axioms(text,targets):
 found={}
 pattern=r"'([^']+)'\s+(?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)"
 for m in re.finditer(pattern,text,re.S):
  name=m.group(1)
  if name in found:raise ValueError('Duplicate axiom report: '+name)
  found[name]=set(re.findall(r'[A-Za-z_][\w.]*',m.group(2)or''))
 if set(found)!=set(targets):raise ValueError('Missing or unexpected axiom reports: '+str(set(found)^set(targets)))
 for name,axs in found.items():
  if axs-ALLOWED:raise ValueError(f'{name} uses unaccepted axioms {axs-ALLOWED}')
 return {k:sorted(v)for k,v in found.items()}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--stage',choices=['preflight','starter','one-stone','residue-zero','global'],default='starter');args=ap.parse_args()
 out=ROOT/'evidence'/('lean-'+args.stage);out.mkdir(parents=True,exist_ok=True)
 receipt={'stage':args.stage,'lean_checked':False,'full_p7_formalized':False}
 try:
  receipt['static']=static_checks()
  if args.stage=='preflight':
   receipt.update(status='PREFLIGHT_PASS_ONLY',reason='No Lean invocation requested; not a proof certificate')
  else:
   required={'one-stone':['Benzel/OneStoneProof.lean'],
     'residue-zero':['Benzel/Construction.lean','Benzel/Final.lean'],
     'global':['Benzel/Construction.lean','Benzel/Final.lean','Benzel/Global.lean']}.get(args.stage,[])
   missing=[p for p in required if not(FORMAL/p).exists()]
   if missing:raise FileNotFoundError('Unfinished formalization modules: '+', '.join(missing))
   if not shutil.which('lake') or not shutil.which('lean'):raise FileNotFoundError('Lean/lake executables are not installed in this runtime')
   version=run(['lean','--version'],out/'version.log')
   if not re.search(r'version\s+4\.31\.0\b',version):raise ValueError('Active Lean version is not pinned 4.31.0')
   lib=FORMAL/'.lake/packages/mathlib'
   if not lib.is_dir():raise FileNotFoundError('Run lake update and verify the pinned mathlib revision first')
   sha=subprocess.check_output(['git','-C',str(lib),'rev-parse','HEAD'],text=True).strip()
   if sha!=EXPECTED_MATHLIB:raise ValueError('Downloaded Mathlib revision differs from pin')
   imports=['Benzel'];targets=list(BASE_TARGETS);typechecks=[]
   if args.stage=='one-stone':
    imports+=['Benzel.OneStoneProof'];targets+=['Benzel.oneStone_correct']
    typechecks+=['example : Benzel.OneStoneGoal := Benzel.oneStone_correct']
   elif args.stage in('residue-zero','global'):
    imports+=['Benzel.Construction','Benzel.Final'];targets+=['Benzel.construct_correct']
    typechecks+=['example : Benzel.ConstructionCorrect Benzel.construct := Benzel.construct_correct']
   if args.stage=='global':
    imports+=['Benzel.Global'];targets+=['Benzel.fullP7']
    typechecks+=['example : Benzel.FullP7Goal := Benzel.fullP7']
   run(['lake','build']+imports,out/'build.log')
   audit='\n'.join('import '+x for x in imports)+'\n\n'+'\n'.join(typechecks)+'\n\n'+'\n'.join('#print axioms '+t for t in targets)+'\n'
   (FORMAL/'Audit.Generated.lean').write_text(audit)
   output=run(['lake','env','lean','--trust=0','-DwarningAsError=true','Audit.Generated.lean'],out/'axioms.log')
   axs=audit_axioms(output,targets)
   receipt.update(status='PASS',lean_checked=True,axioms=axs,full_p7_formalized=args.stage=='global')
 except FileNotFoundError as e:receipt.update(status='NOT_RUN',reason=str(e))
 except Exception as e:receipt.update(status='FAIL',reason=str(e))
 (out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
 return 0 if receipt['status']in('PASS','PREFLIGHT_PASS_ONLY')else 2
if __name__=='__main__':raise SystemExit(main())
