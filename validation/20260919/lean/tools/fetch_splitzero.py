#!/usr/bin/env python3
"""Materialize only pinned original source files, without editing the user's repo.
Use --source-dir /path/to/formal/splitzero for an existing checkout, or --download.
Downloaded sources are not evaluated by this script. No credentials are requested.
"""
from __future__ import annotations
import argparse,hashlib,json,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
UP='https://raw.githubusercontent.com/KokunoYumeto/zeta-function-research-reader/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/formal/splitzero/'
CORE='https://raw.githubusercontent.com/KokunoYumeto/modern-latex-manuscripts/f7ff59b176c7dc3941babd4cb9272dffc653070d/formalization/lean/classical_candidates_20260626/split_support_sidecar/SplitZero.lean'
PINS={'SplitZero.lean':'ff991f7383922e71cdf0e4a3bc85e89e18f808ef',
'SplitZeroExtension.lean':'a5f9cb64355dfa5967ed9a0779843975cdea3449',
'SplitZeroFibres.lean':'6ec4d98ebc73387bffa8aa8a2f6ac58aaeb721aa',
'SplitZeroReconstruction.lean':'67501925618aad226644c4f67e15c7af7db9b4d7',
'SplitZeroHomology.lean':'7b9e5c49a494dd0c751133e0234b3e01048f7b67',
'SplitZeroInternalQuotient.lean':'908bd0e7d087864e4d004116fcbb4cd2751627be',
'SplitZeroComplex.lean':'34e7e69568a21e86d782ea4e98370f50762a8eab'}
def blob(raw):return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def main():
 ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True);g.add_argument('--source-dir',type=Path);g.add_argument('--download',action='store_true');args=ap.parse_args();staged={}
 for name,sha in PINS.items():
  dest=ROOT/'formal'/name
  if dest.exists():raw=dest.read_bytes()
  elif args.source_dir:raw=(args.source_dir/name).read_bytes()
  else:
   with urllib.request.urlopen(CORE if name=='SplitZero.lean'else UP+name,timeout=45)as r:raw=r.read()
  if blob(raw)!=sha:raise ValueError('Original upstream source identity changed: '+name)
  raw.decode('utf-8');staged[name]=raw
 for name,raw in staged.items():(ROOT/'formal'/name).write_bytes(raw)
 print(json.dumps({'status':'SOURCE_IDENTITIES_PASS','files':PINS,'lean_build':'NOT_RUN'},indent=2))
if __name__=='__main__':main()
