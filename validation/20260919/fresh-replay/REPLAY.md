# Selected Benzel audit replay — 19 September 2026

**PASS in the selected scope.** A fresh byte-identical copy of the supplied 18 September audit bundle passed its manifest check, all 18 exported polynomial identities, all 6,559 exported affine identities, and the 24-certificate quick original-cell check. Thirteen deliberate malformed inputs were rejected across the three checkers. The intact intake remained byte-for-byte unchanged.

The machine record is [REPLAY.json](REPLAY.json). The actual per-check outputs are in [runs/](runs/); [run_replay.py](run_replay.py) is the complete authored driver. No supplied checker or constructor was edited.

## Executed checks

| Supplied code / selected entry point | Fresh result | Comparison with supplied evidence |
|---|---:|---|
| `audit/verify_bundle.py` | 209 manifest entries, no missing or changed files | Fresh copied snapshot verified before any generated evidence was replaced |
| `audit/check_polynomial_receipts.py` | 18 integer Laurent identities; 2 mutations rejected | Every mathematical field matches supplied `evidence/polynomial-receipt-check.json`; only elapsed time excluded |
| `audit/check_linear_receipts.py` | 6,559 exact affine identities; 3 mutations rejected | Complete parsed JSON matches supplied `evidence/linear-receipt-check.json`; byte difference is CRLF versus LF only |
| `audit/quick_output_check.py` | 12 parameter pairs, 24 original/reflected tiling certificates, 269,470 tile placements | Every mathematical field matches supplied `evidence/fresh-copy-output.log`; only elapsed time excluded |
| `original_cell_check.mutation_checks()` | All 8 malformed certificates rejected | Invoked directly in the same process after the quick check; the full sweep entry point was not invoked |

The 12 tested `(d,h)` pairs were `(2,0)`, `(2,1)`, `(9,7)`, `(10,8)`, `(12,10)`, `(13,11)`, `(14,12)`, `(15,13)`, `(16,14)`, `(17,15)`, `(20,190)`, and `(21,40)`, together with their reflected tilings.

The polynomial checker clears the recorded products of nonzero factors `1-X^a Y^b`, retaining six independent integer exponent coordinates, and obtains a zero numerator for every exported identity. The affine checker validates exact nonnegative rational combinations of the supplied five-coordinate affine constraints and targets. These replays check the exported equations; they do not independently reconstruct their association with every original tile table.

The quick output check generates candidate tiles through the supplied constructor and accepts them through the separately supplied original-cell checker: allowed tile shapes, original barycentric inequalities, row intervals, collision-free coverage, and reflections. This is a fresh bounded output test of the supplied audit, not a claim that finite sampling proves the construction for all parameters.

## Process and source preservation

One Python 3.13.9 process ran the checks sequentially under the existing `private_review/ym_quartic_20260917/replay_review/bounded_worker.py` guard. Its Windows kernel Job Object verified a 2,147,483,648-byte process and job memory cap, active-process limit one, and affinity to one logical core before executing supplied code. The recorded peak committed memory was 118,894,592 bytes. The final kernel measurements are in [kernel_limits.json](kernel_limits.json).

The four main checks took approximately 16.6 seconds in total, excluding copy/hash preparation. No subprocesses, Lean workers, optimizers, full algebra pipeline, external packages, or full 3,372-certificate original-cell sweep were launched by this task. The root task's separate Lean work is outside this replay record.

All executed scripts and their constructor import closure were read for safety before launch. They use standard-library code and local data; supplied writes are restricted to the working copy's declared evidence files. All 210 intake files were hashed before and after the run. The new working copy initially matched those hashes exactly. Source and dependency hashes are retained in [runs/supplied_file_hashes.json](runs/supplied_file_hashes.json) and `REPLAY.json`.

Only the working copy's `evidence/polynomial-receipt-check.json` and `evidence/linear-receipt-check.json` were replaced, and `evidence/quick-output.json` was created. The original intake, candidate mathematical sources, repository/public files, and supplied historical evidence were preserved. Nothing was published.

The delivered top-level manifest SHA-256 is `70f80f98cd0f0e891c448b16cc4b7b343ebd0b588f1925e8234ba5df16b8517e`. The guard SHA-256 is `b6b2a0a176f7c34b7f06f0612573f555885601a293d681d71fcb8c629529042d`. The exact driver and each executed source hash are recorded in `REPLAY.json`.

## Reproduction

The recorded working directory was prepared by copying `private_review/benzel_validation_20260919/intake/benzel-audit-20260918` to `private_review/benzel_validation_20260919/replay_audit/bundle`. From the workspace, the guarded execution was equivalent to:

```text
python -B private_review/ym_quartic_20260917/replay_review/bounded_worker.py private_review/benzel_validation_20260919/replay_audit/kernel_limits.json private_review/benzel_validation_20260919/replay_audit/run_replay.py
```

The driver calls the four unmodified scripts using `runpy` in that same bounded process, captures each actual stdout/stderr, compares the result with the intact supplied receipt, invokes the eight cell mutations, and verifies that the intake did not change. It fails if the working bundle is not initially byte-identical to the intake.

For another replay, use a new sibling review directory containing a copy of this driver and a fresh `bundle` copied from the intact intake, then point the guard to that directory's limits file and driver. This preserves the present execution evidence and avoids treating regenerated evidence as the delivered manifest snapshot.

## Limits of the conclusion

This result supports the stated 18 polynomial identities, 6,559 affine receipt identities, 24 concrete tiling certificates, and 13 negative controls on the pinned supplied data. It does not independently replay the full reconstruction audit, certify the unbounded-parameter theorem, audit the external generalized-compression theorem, or constitute a Lean certificate or external specialist review. Those distinct claims require their own evidence and are not inferred from these passing checks.
