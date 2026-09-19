# Benzel P7 — reimplementation audit, 18 September 2026

**Verdict: PASS in the reported scope.** No failed construction identity, source-bound certificate, canonical parameter case or original tiling was found. No mathematical modification to the frozen candidate source was needed.

Read `report/AUDIT_REPORT.pdf` or the editable `report/AUDIT_REPORT.tex` / `report/AUDIT_REPORT.md`. Machine-readable scope and results are in `AUDIT_SUMMARY.json`.

## What this verdict means

New checkers were written separately from the candidate's verification code. They check original barycentric cells, independently reconstructed formal identities, exact original-source inequalities, integral kernel coordinates and the full parameter exhaustion argument. The full original P7 assembly retains the exact published generalized-compression theorem for the residue-two class.

This is **verification by a separately implemented audit performed by the same assistant**, not an external specialist's endorsement or a Lean proof certificate. It does not audit the complete Sharma manuscript, determine novelty, or change repository status. The prior full-solution claim and older bone-homology attribution remain as recorded in the frozen provenance.

## Files

- `audit/`: newly written mathematical checkers and a packaging verifier.
- `evidence/`: new arithmetic, geometry, command and source-identity receipts. `normal/` and `optimized/` hold separate seven-script pipeline runs. The original-cell sweep was performed once; the fresh-copy replay was a smaller additional check.
- `frozen/benzel-p7-cumulative-through-turn10/current/`: unchanged mathematical source closure under audit, with its original manifest and original historical receipts. These historical receipts are not counted as new verification.
- `report/`: complete audit report and editable LaTeX.
- `SOURCES.json`: exact external dependency-reading scope.

This bundle contains the audited current source closure, not all historical ZIP handbacks. The previously supplied cumulative archive retains that history. No Sharma PDF, external source paper, or font file is included here.

## Reproduce

The recorded environment is Python 3.13.5 with SymPy 1.14.0. Install the dependency with `python -m pip install -r requirements.txt` in your own environment, then:

```sh
python audit/run_algebra_checks.py
python audit/run_algebra_checks.py --optimized
python audit/original_cell_check.py --max-d 20
```

The final command checks 3,372 full original/reflected tiling certificates in the recorded configuration and took approximately 12.4 minutes here. It also includes a specified larger-parameter sample and the residue-one cases, beyond the `--max-d` sweep. It does not sample the published compression construction.

The exported exact arithmetic can be replayed with the standard library alone:

```sh
python audit/check_polynomial_receipts.py
python audit/check_linear_receipts.py
```

A quick original-output test is `python audit/quick_output_check.py` (24 certificates). The two receipt-only scripts check the exported equations; the reconstruction scripts and report connect them to the original tile tables.

Generated test outputs may replace the corresponding `evidence/` files. The top-level manifest records the delivered snapshot; compare it before regenerating files. No command commits, uploads or otherwise modifies a remote repository.

To verify the delivered snapshot before running commands, use `python audit/verify_bundle.py`.
