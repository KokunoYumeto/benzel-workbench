# Benzel P7 — completed residue-zero construction

Start with `turn10/PROOF.pdf` or the editable `turn10/PROOF.tex` / `turn10/PROOF.md`.

The constructor now covers **every integer d>=2 and 0<=h<=binom(d,2)** on the original regions `W_h(d)=V(d+3h,2d+3h)`, with exactly `binom(d,2)-h` right stones and `3h(h+d)` bones. All canonical q residue classes and the exceptional q=7,8,10,11 cases are handled. The new uniform second-residue repair uses the original first and third corner stones and an eight-bone vacancy bridge.

The full original P7 assembly also uses the previously established residue-two generalized-compression theorem; its exact parameter map and tile-set inclusion are explicitly retained. This is not a self-contained reproof of that published result or a line-by-line audit of the earlier full claim reported by the owner. Read `turn10/PROVENANCE.md`.

## Run

From `turn10`:

```sh
python verify.py --max-d 12 --max-k 9 --output evidence/normal.json
python -O verify.py --max-d 12 --max-k 9 --output evidence/optimized.json
```

These commands use the Python standard library only. They replay unbounded-parameter polynomial identities, exact rational source certificates, original-generator ownership, complete bounded tilings, integral comparison-kernel duals and deliberate rejection tests. They do not invoke a solver or network service.

For one original tiling:

```python
from complete_theorem import complete_W, G
placements = complete_W(d=16, h=14)
G.check_partition(placements, G.region_ab(58, 74))
```

The literal original kinds are R,H,V,D, and each placement retains its three integer cells. `complete_from_core` gives the explicit `(d,m,q)` interface. `residue_one(a,b)` constructs the established sum-one-modulo-three family directly.

## Layout

`turn10/` is the new proof, code, tables and exact certificates. `turn7/`, `turn8/`, and `turn9/` preserve the mathematical dependencies used by the proof. Recorded outcomes are in `turn10/evidence/`; `MANIFEST.sha256` identifies the delivered bytes. The optional development directory records searches and corrections; it is not a proof premise.

The canonical scope is complete, but the work remains a research proof pending independent mathematical review. No first-priority claim, new Lean certificate or remote integration is asserted. The user's report of prior literature overlap is explicitly preserved.
