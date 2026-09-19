#!/usr/bin/env python3
"""Validate this source handoff without interpreting any proof status."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 manifest=ROOT/'MANIFEST.sha256';seen=set();bad=[]
 for line in manifest.read_text().splitlines():
  expected,rel=line.split('  ',1);p=ROOT/rel
  if rel in seen or not p.resolve().is_relative_to(ROOT.resolve()):raise ValueError('Unsafe manifest entry')
  seen.add(rel)
  if not p.is_file()or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:bad.append(rel)
 actual={str(p.relative_to(ROOT))for p in ROOT.rglob('*')if p.is_file()and p!=manifest and '__pycache__'not in p.parts and '.lake'not in p.parts}
 extras=sorted(actual-seen)
 out={'status':'PASS'if not bad and not extras else'FAIL','files':len(seen),'changed_or_missing':bad,'unexpected':extras,'scope':'File identity only'}
 print(json.dumps(out,indent=2))
 if out['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':main()
