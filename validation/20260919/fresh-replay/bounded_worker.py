"""Apply Windows kernel memory/CPU-affinity caps before loading the supplied code."""
import ctypes
from ctypes import wintypes
import json
import os
from pathlib import Path
import runpy
import sys


class BasicLimit(ctypes.Structure):
    _fields_ = [
        ("PerProcessUserTimeLimit", ctypes.c_int64),
        ("PerJobUserTimeLimit", ctypes.c_int64),
        ("LimitFlags", wintypes.DWORD),
        ("MinimumWorkingSetSize", ctypes.c_size_t),
        ("MaximumWorkingSetSize", ctypes.c_size_t),
        ("ActiveProcessLimit", wintypes.DWORD),
        ("Affinity", ctypes.c_size_t),
        ("PriorityClass", wintypes.DWORD),
        ("SchedulingClass", wintypes.DWORD),
    ]


class IOCounters(ctypes.Structure):
    _fields_ = [(name, ctypes.c_uint64) for name in (
        "ReadOperationCount", "WriteOperationCount", "OtherOperationCount",
        "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]


class ExtendedLimit(ctypes.Structure):
    _fields_ = [
        ("BasicLimitInformation", BasicLimit), ("IoInfo", IOCounters),
        ("ProcessMemoryLimit", ctypes.c_size_t),
        ("JobMemoryLimit", ctypes.c_size_t),
        ("PeakProcessMemoryUsed", ctypes.c_size_t),
        ("PeakJobMemoryUsed", ctypes.c_size_t),
    ]


def main():
    limits_path = Path(sys.argv[1]).resolve()
    script = Path(sys.argv[2]).resolve()
    args = sys.argv[3:]
    if os.name != "nt":
        raise RuntimeError("This runner requires Windows kernel Job Objects")
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
    kernel.CreateJobObjectW.restype = wintypes.HANDLE
    kernel.SetInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
    kernel.QueryInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD, ctypes.c_void_p]
    kernel.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
    kernel.GetCurrentProcess.restype = wintypes.HANDLE
    kernel.GetProcessAffinityMask.argtypes = [wintypes.HANDLE, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_size_t)]
    kernel.SetProcessAffinityMask.argtypes = [wintypes.HANDLE, ctypes.c_size_t]
    process = kernel.GetCurrentProcess()
    job = kernel.CreateJobObjectW(None, None)
    if not job:
        raise ctypes.WinError(ctypes.get_last_error())
    info = ExtendedLimit()
    # PROCESS_MEMORY | JOB_MEMORY | KILL_ON_JOB_CLOSE | ACTIVE_PROCESS
    info.BasicLimitInformation.LimitFlags = 0x100 | 0x200 | 0x2000 | 0x8
    info.BasicLimitInformation.ActiveProcessLimit = 1
    info.ProcessMemoryLimit = info.JobMemoryLimit = 2 * 1024**3
    for ok in (
        kernel.SetInformationJobObject(job, 9, ctypes.byref(info), ctypes.sizeof(info)),
        kernel.AssignProcessToJobObject(job, process),
    ):
        if not ok:
            raise ctypes.WinError(ctypes.get_last_error())
    mask = ctypes.c_size_t()
    system_mask = ctypes.c_size_t()
    if not kernel.GetProcessAffinityMask(process, ctypes.byref(mask), ctypes.byref(system_mask)):
        raise ctypes.WinError(ctypes.get_last_error())
    selected = mask.value & -mask.value
    if not selected or not kernel.SetProcessAffinityMask(process, selected):
        raise ctypes.WinError(ctypes.get_last_error())
    actual = ExtendedLimit()
    if not kernel.QueryInformationJobObject(job, 9, ctypes.byref(actual), ctypes.sizeof(actual), None):
        raise ctypes.WinError(ctypes.get_last_error())
    record = {
        "mechanism": "Windows kernel Job Object, verified before executing supplied code",
        "process_memory_limit_bytes": actual.ProcessMemoryLimit,
        "job_memory_limit_bytes": actual.JobMemoryLimit,
        "active_process_limit": actual.BasicLimitInformation.ActiveProcessLimit,
        "limit_flags": actual.BasicLimitInformation.LimitFlags,
        "cpu_affinity_mask": selected,
        "logical_cores": selected.bit_count(),
        "python_optimization_level": sys.flags.optimize,
        "pid": os.getpid(),
    }
    if record["process_memory_limit_bytes"] != 2 * 1024**3 or record["job_memory_limit_bytes"] != 2 * 1024**3:
        raise RuntimeError("Kernel limit readback mismatch")
    limits_path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    os.chdir(script.parent)
    sys.path.insert(0, str(script.parent))
    sys.argv = [str(script), *args]
    try:
        runpy.run_path(str(script), run_name="__main__")
    finally:
        if kernel.QueryInformationJobObject(job, 9, ctypes.byref(actual), ctypes.sizeof(actual), None):
            record["peak_process_commit_bytes"] = actual.PeakProcessMemoryUsed
            record["peak_job_commit_bytes"] = actual.PeakJobMemoryUsed
            limits_path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    # Do not close a kill-on-close job while the process is still executing.


if __name__ == "__main__":
    main()
