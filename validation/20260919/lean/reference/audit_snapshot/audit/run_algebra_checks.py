"""Replay the independently written algebra/source audit in separate processes."""
from pathlib import Path
import subprocess,sys,json,time,hashlib,shutil,argparse,platform
ROOT=Path(__file__).resolve().parents[1]
JOBS=[('independent_symbolic.py','independent-symbolic.json'),
      ('check_polynomial_receipts.py','polynomial-receipt-check.json'),
      ('table_semantics.py','table-semantics.json'),
      ('independent_sources.py','independent-sources.json'),
      ('check_linear_receipts.py','linear-receipt-check.json'),
      ('independent_kernel.py','independent-kernel.json'),
      ('local_and_parameters.py','local-and-parameters.json')]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--optimized',action='store_true');args=ap.parse_args()
    mode='optimized' if args.optimized else 'normal';out=ROOT/'evidence'/mode;out.mkdir(parents=True,exist_ok=True)
    runs=[]
    for script,receipt in JOBS:
        command=[sys.executable]+(['-O'] if args.optimized else [])+[str(ROOT/'audit'/script)]
        t=time.monotonic();proc=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,timeout=180)
        (out/(script+'.log')).write_text(proc.stdout+proc.stderr)
        if proc.returncode:raise RuntimeError(f'{script} failed; inspect its {mode} log')
        raw=(ROOT/'evidence'/receipt).read_bytes();data=json.loads(raw)
        if data.get('status')!='PASS':raise RuntimeError(f'{script} did not return a passing receipt')
        (out/receipt).write_bytes(raw)
        runs.append({'script':script,'optimized':args.optimized,'returncode':0,'seconds':round(time.monotonic()-t,3),
                    'script_sha256':hashlib.sha256((ROOT/'audit'/script).read_bytes()).hexdigest(),
                    'receipt':str((out/receipt).relative_to(ROOT)), 'receipt_sha256':hashlib.sha256(raw).hexdigest()})
        print(mode,script,'PASS',flush=True)
    (out/'run-ledger.json').write_text(json.dumps({'status':'PASS','mode':mode,'python':platform.python_version(),'runs':runs},indent=2)+'\n')
if __name__=='__main__':main()
