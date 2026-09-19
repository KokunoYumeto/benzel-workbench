"""Replay only the explicitly selected supplied Benzel checks in one process.

Invoke through the existing Windows bounded_worker.py. No subprocess, Lean,
optimizer, full algebra pipeline, or full original-cell sweep is launched.
The intake is read-only; supplied checkers write solely into this copied bundle.
"""
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
import argparse
import hashlib
import io
import json
import os
import platform
import runpy
import sys
import time
import traceback


ROOT = Path(__file__).resolve().parent
BUNDLE = ROOT / "bundle"
RUNS = ROOT / "runs"
CHECKS = [
    ("manifest", "verify_bundle.py", None),
    ("polynomial", "check_polynomial_receipts.py", "evidence/polynomial-receipt-check.json"),
    ("affine", "check_linear_receipts.py", "evidence/linear-receipt-check.json"),
    ("quick-output", "quick_output_check.py", "evidence/fresh-copy-output.log"),
]
READ_CLOSURE = [
    "audit/verify_bundle.py", "audit/check_polynomial_receipts.py",
    "audit/check_linear_receipts.py", "audit/quick_output_check.py",
    "audit/original_cell_check.py",
    "frozen/benzel-p7-cumulative-through-turn10/current/turn10/complete_theorem.py",
    "frozen/benzel-p7-cumulative-through-turn10/current/turn10/source10.py",
    "frozen/benzel-p7-cumulative-through-turn10/current/turn9/source_table.py",
    "frozen/benzel-p7-cumulative-through-turn10/current/turn8/geometry.py",
    "frozen/benzel-p7-cumulative-through-turn10/current/turn8/packing.py",
    "frozen/benzel-p7-cumulative-through-turn10/current/turn8/construction.py",
    "frozen/benzel-p7-cumulative-through-turn10/current/turn8/bivariate_certificate.py",
    "frozen/benzel-p7-cumulative-through-turn10/current/turn8/families.py",
    "frozen/benzel-p7-cumulative-through-turn10/current/turn7/parent_construction.py",
    "frozen/benzel-p7-cumulative-through-turn10/current/turn7/construction.py",
]


def require(condition, description):
    if not condition:
        raise RuntimeError(description)


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            result.update(chunk)
    return result.hexdigest()


def snapshot(root):
    return {str(path.relative_to(root)).replace("\\", "/"): digest(path)
            for path in sorted(root.rglob("*")) if path.is_file()}


def store(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def without_seconds(receipt):
    return {key: value for key, value in receipt.items() if key != "seconds"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--intake", type=Path, default=ROOT.parent / "intake/benzel-audit-20260918")
    parser.add_argument("--limits", type=Path, default=ROOT / "kernel_limits.json")
    args = parser.parse_args()
    intake = args.intake.resolve()
    require(intake != BUNDLE.resolve(), "intake must differ from working copy")
    limits = json.loads(args.limits.read_text(encoding="utf-8"))
    require(limits["pid"] == os.getpid(), "limits must belong to this process")
    require(limits["active_process_limit"] == 1, "one-process kernel limit required")
    require(limits["logical_cores"] == 1, "one-core affinity required")
    require(limits["process_memory_limit_bytes"] == 2 * 1024**3, "2 GiB process limit required")
    require(limits["job_memory_limit_bytes"] == 2 * 1024**3, "2 GiB job limit required")
    require(sys.dont_write_bytecode, "invoke Python with -B")
    RUNS.mkdir(exist_ok=True)
    supplied_hashes = snapshot(intake)
    working_before = snapshot(BUNDLE)
    require(supplied_hashes == working_before, "fresh working copy differs from intake")
    store(RUNS / "supplied_file_hashes.json", supplied_hashes)
    baseline_receipts = {
        name: json.loads((intake / comparison).read_text(encoding="utf-8"))
        for name, _, comparison in CHECKS if comparison
    }
    audit = BUNDLE / "audit"
    sys.path.insert(0, str(audit))
    os.chdir(BUNDLE)
    runs = []
    for name, script_name, comparison in CHECKS:
        script = audit / script_name
        stdout, stderr = io.StringIO(), io.StringIO()
        sys.argv = [str(script)]
        started = time.monotonic()
        error = None
        try:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                runpy.run_path(str(script), run_name="__main__")
        except BaseException:
            error = traceback.format_exc()
        elapsed = round(time.monotonic() - started, 6)
        (RUNS / (name + ".stdout.json")).write_text(stdout.getvalue(), encoding="utf-8")
        (RUNS / (name + ".stderr.txt")).write_text(stderr.getvalue() + (error or ""), encoding="utf-8")
        require(error is None, "supplied checker failed: " + name)
        actual = json.loads(stdout.getvalue())
        require(actual["status"] == "PASS", "non-PASS receipt: " + name)
        entry = {
            "name": name, "script": "bundle/audit/" + script_name,
            "script_sha256": digest(script), "seconds_this_replay": elapsed,
            "exit_status": 0, "receipt": "runs/" + name + ".stdout.json",
            "receipt_sha256": digest(RUNS / (name + ".stdout.json")),
        }
        if comparison:
            require(without_seconds(actual) == without_seconds(baseline_receipts[name]),
                    "mathematical receipt differs from supplied: " + name)
            entry.update({
                "supplied_receipt": comparison,
                "supplied_receipt_sha256": digest(intake / comparison),
                "matches_supplied_except_seconds": True,
                "raw_bytes_match_supplied": (RUNS / (name + ".stdout.json")).read_bytes() == (intake / comparison).read_bytes(),
                "excluded_comparison_fields": ["seconds"] if "seconds" in actual else [],
            })
        runs.append(entry)
        print(name + ": PASS", flush=True)

    checker = sys.modules["original_cell_check"]
    require(Path(checker.__file__).resolve() == (audit / "original_cell_check.py").resolve(),
            "mutation checker must come from the working bundle")
    rejected = checker.mutation_checks()
    require(rejected == 8, "expected all eight original-cell mutations rejected")
    store(RUNS / "original-cell-mutations.json", {"status": "PASS", "mutations_rejected": rejected})
    print("original-cell mutations: 8 rejected", flush=True)

    final_working = snapshot(BUNDLE)
    intake_after = snapshot(intake)
    require(intake_after == supplied_hashes, "intake changed during replay")
    changed = [path for path in supplied_hashes if final_working.get(path) != supplied_hashes[path]]
    added = sorted(set(final_working) - set(supplied_hashes))
    allowed_changed = {"evidence/polynomial-receipt-check.json", "evidence/linear-receipt-check.json"}
    require(set(changed) <= allowed_changed, "unexpected working-copy mutation")
    require(set(added) <= {"evidence/quick-output.json"}, "unexpected working-copy file creation")
    manifest = json.loads((RUNS / "manifest.stdout.json").read_text(encoding="utf-8"))
    polynomial = json.loads((RUNS / "polynomial.stdout.json").read_text(encoding="utf-8"))
    affine = json.loads((RUNS / "affine.stdout.json").read_text(encoding="utf-8"))
    quick = json.loads((RUNS / "quick-output.stdout.json").read_text(encoding="utf-8"))
    guard = ROOT.parents[1] / "ym_quartic_20260917/replay_review/bounded_worker.py"
    result = {
        "schema": "benzel-selected-bounded-replay-v1", "status": "PASS", "date": "2026-09-19",
        "python_version": platform.python_version(), "python_optimization_level": sys.flags.optimize,
        "runner_sha256": digest(Path(__file__)), "guard_sha256": digest(guard),
        "resource_limits": limits, "final_resource_receipt": "kernel_limits.json",
        "source_manifest_sha256": supplied_hashes["MANIFEST.sha256"],
        "intake_files": len(supplied_hashes), "intake_unchanged": True,
        "working_copy_initially_byte_identical": True,
        "supplied_file_hashes": "runs/supplied_file_hashes.json",
        "read_code_closure_sha256": {path: supplied_hashes[path] for path in READ_CLOSURE},
        "runs": runs,
        "counts": {
            "manifest_entries": manifest["manifest_entries"],
            "polynomial_identities": polynomial["identities"],
            "polynomial_mutations_rejected": polynomial["mutations_rejected"],
            "exact_affine_identities": affine["exact_affine_identities"],
            "affine_mutations_rejected": affine["mutation_rejections"],
            "original_parameter_pairs": quick["original_parameter_pairs"],
            "tiling_certificates_with_reflections": quick["tiling_certificates_with_reflections"],
            "placements": quick["placements"],
            "original_cell_mutations_rejected": rejected,
        },
        "working_copy_changed_files": changed, "working_copy_added_files": added,
        "scope": "Supplied exported polynomial and affine equations replayed; 24 independently accepted original/reflected tiling certificates. The full reconstruction pipeline, full 3372-certificate sweep, unbounded-parameter theorem, external compression theorem, and Lean formalization were not replayed by this process.",
        "launch_from_workspace": "python -B private_review/ym_quartic_20260917/replay_review/bounded_worker.py private_review/benzel_validation_20260919/replay_audit/kernel_limits.json private_review/benzel_validation_20260919/replay_audit/run_replay.py",
        "reproduction_note": "Requires a fresh byte-identical bundle copy. For a second run, make a new review directory with this runner and a new bundle copied from intact intake; do not overwrite the original intake.",
    }
    store(ROOT / "REPLAY.json", result)
    print(json.dumps({"status": result["status"], "counts": result["counts"], "intake_unchanged": True}, indent=2))


if __name__ == "__main__":
    main()
