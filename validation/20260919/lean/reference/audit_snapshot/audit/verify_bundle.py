"""Check every delivered file against the self-excluding bundle manifest."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def main():
    manifest=ROOT/'MANIFEST.sha256';bad=[];seen=set()
    for line in manifest.read_text().splitlines():
        digest,relative=line.split('  ',1);p=ROOT/relative
        if relative in seen or p.resolve().is_relative_to(ROOT.resolve()) is False:raise ValueError('unsafe/duplicate manifest path')
        seen.add(relative)
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:bad.append(relative)
    receipt={'status':'PASS' if not bad else 'FAIL','manifest_entries':len(seen),'missing_or_changed':bad}
    print(json.dumps(receipt,indent=2))
    if bad:raise SystemExit(1)
if __name__=='__main__':main()
