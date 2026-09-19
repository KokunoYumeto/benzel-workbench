# Turn 9: asymmetric positive endpoint completion

**Domain:** integers k >= 4, m >= 3k+3, d >= m, with q=3k+1, Delta=m(m-1)/2-q, and h=d(d-1)/2-Delta.

`PROOF.md` gives the full original-coordinate argument. `edits.json` is the shared literal parameter table. `ownership-certificates.json` gives exact nonnegative rational domain witnesses; `ownership.py` reconstructs and verifies their original source constraints. `symbolic_certificate.py` verifies the two integer Laurent identities before either parameter is chosen. The positive original-cell constructor calls no optimizer.

Run with Python's standard library:

```sh
python symbolic_certificate.py
python ownership.py
python verify.py --max-k 10 --output evidence/normal.json
python -O verify.py --max-k 10 --output evidence/optimized.json
```

The adjacent `turn8/` folder is the unchanged source dependency from the previously delivered handback. In the GitHub workbench the same sibling directory already exists at the base commit. The optional `generate_ownership_certificates.py` uses NumPy/SciPy to discover candidate multipliers; its statuses are not certificates. The final verifier uses exact fractions and does not need either package.

The written result is a constructive research claim pending independent mathematical review. It is not a full solution of Propp 7, a new Lean result, an optimality statement, or an assertion of historical priority. This continuation covers q=13,16,19,... without an upper cutoff; it does not promote the remaining q=3k+2 endpoint to a completed result.

No remote branch or pull request is represented as created by this handback. An additive patch and proposed PR description accompany the local source package.
