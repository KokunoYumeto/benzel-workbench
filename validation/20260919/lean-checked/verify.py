"""Serial kernel checks in an already prepared, pinned Lake environment.

Usage: lake env python verify.py
No builds or downloads are launched. Lean checks exactly one local file at a
time, with one thread, a 3000 MiB allocator limit and a 180-second timeout.
Windows additionally requires psutil and caps this controller plus Lean at
4 GiB with a kernel Job Object. The job allows only those two processes.
"""
from pathlib import Path
import ctypes
from ctypes import wintypes
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
MODULES=['Benzel.Geometry','Benzel.Tiles','Benzel.Incidence','Benzel.Parameters',
 'Benzel.Comparison','Benzel.Generated.LocalPatches','Benzel.PatchHomotopy',
 'Benzel.OneStone','Benzel.BandSlideProof','Benzel.SourceOwnershipExamples','BenzelChecked','Audit']
ALLOWED={'propext','Classical.choice','Quot.sound'}

def cap_windows():
    if os.name!='nt': return None
    import psutil
    for p in psutil.process_iter(['name']):
        if (p.info['name'] or '').lower()=='lean.exe':
            raise RuntimeError('Another Lean worker is active; no launch')
    class Basic(ctypes.Structure):
        _fields_=[('pt',ctypes.c_int64),('jt',ctypes.c_int64),('flags',wintypes.DWORD),
          ('minws',ctypes.c_size_t),('maxws',ctypes.c_size_t),('active',wintypes.DWORD),
          ('affinity',ctypes.c_size_t),('priority',wintypes.DWORD),('schedule',wintypes.DWORD)]
    class Extended(ctypes.Structure):
        _fields_=[('basic',Basic),('io',ctypes.c_uint64*6),('process',ctypes.c_size_t),
          ('job',ctypes.c_size_t),('peakprocess',ctypes.c_size_t),('peakjob',ctypes.c_size_t)]
    k=ctypes.WinDLL('kernel32',use_last_error=True)
    k.CreateJobObjectW.restype=wintypes.HANDLE
    k.GetCurrentProcess.restype=wintypes.HANDLE
    k.SetInformationJobObject.argtypes=[wintypes.HANDLE,ctypes.c_int,ctypes.c_void_p,wintypes.DWORD]
    k.AssignProcessToJobObject.argtypes=[wintypes.HANDLE,wintypes.HANDLE]
    job=k.CreateJobObjectW(None,None)
    info=Extended();info.basic.flags=0x100|0x200|0x2000|0x8;info.basic.active=2
    info.process=info.job=4*1024**3
    if not job or not k.SetInformationJobObject(job,9,ctypes.byref(info),ctypes.sizeof(info)):
        raise ctypes.WinError(ctypes.get_last_error())
    if not k.AssignProcessToJobObject(job,k.GetCurrentProcess()):
        raise ctypes.WinError(ctypes.get_last_error())
    process=psutil.Process();process.cpu_affinity([process.cpu_affinity()[0]])
    return job

def main():
    lean=shutil.which('lean')
    if lean is None: raise RuntimeError('Run inside the pinned Lake environment')
    version=subprocess.check_output([lean,'--version'],text=True)
    if not re.search(r'version\s+4\.32\.0\b',version): raise RuntimeError(version)
    mathlib=ROOT/'.lake/packages/mathlib'
    sha=subprocess.check_output(['git','-C',str(mathlib),'rev-parse','HEAD'],text=True).strip()
    if sha!='81a5d257c8e410db227a6665ed08f64fea08e997': raise RuntimeError('Mathlib pin differs')
    guard=cap_windows()
    env=os.environ.copy();env['LEAN_PATH']=str(ROOT)+os.pathsep+env.get('LEAN_PATH','')
    logs=ROOT/'replay';logs.mkdir(exist_ok=True)
    results=[]
    for name in MODULES:
        p=ROOT/Path(*name.split('.')).with_suffix('.lean')
        proc=subprocess.run([lean,'-j1','-M3000','--trust=0','-o',str(p.with_suffix('.olean')),str(p)],
           cwd=ROOT,env=env,text=True,encoding='utf-8',capture_output=True,timeout=180)
        text=proc.stdout+proc.stderr
        (logs/(name+'.log')).write_text(text,encoding='utf-8')
        if proc.returncode: raise RuntimeError(text)
        results.append({'module':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'exit_code':0})
    source=(ROOT/'Audit.lean').read_text(encoding='utf-8')
    targets=re.findall(r'^#print axioms (\S+)',source,re.M)
    axs={}
    for m in re.finditer(r"'([^']+)'\s+(?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)",text):
        if m[1] in axs: raise ValueError('Duplicate axiom report')
        axs[m[1]]=re.findall(r'[A-Za-z_][\w.]*',m[2] or '')
    if len(targets)!=len(axs) or set(targets)!=set(axs): raise ValueError('Incomplete axiom reports')
    if any(set(v)-ALLOWED for v in axs.values()): raise ValueError('Unapproved axiom')
    receipt={'status':'PASS','version':version.strip(),'mathlib':sha,'modules':results,'axioms':axs,
             'full_P7_formalized':False,'centered_tiling_formalized':False}
    (logs/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','modules':len(results),'axiom_reports':len(axs)}))

if __name__=='__main__': main()
