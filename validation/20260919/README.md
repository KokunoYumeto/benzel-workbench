# Benzel constructions: a readable proof and exact validation

This edition explains an explicit threefold-symmetric tiling with one central
right stone, preserves the complete residue-zero construction and its
AI-assisted audit, and supplies a modest kernel-checked formal contribution.

Start with **[A centered stone and three rotating bands](CENTERED_ONE_STONE.pdf)**
([online text](CENTERED_ONE_STONE.md), [editable LaTeX](CENTERED_ONE_STONE.tex)).
It defines the original region and tiles, constructs the bands, proves their
containment and disjointness, and identifies their three-cell complement.
The smallest example, V(9,12), has one central stone and 30 bones.

## Exact results

For every integer d >= 3, let h = d(d-1)/2 - 1. The displayed construction
tiles V(d+3h,2d+3h) with R(0,0) and 3h(h+d) bones, invariant under
rho(x,y) = (y,1-x-y). The reader gives a direct counting proof of the central
complement, avoiding the more general residual-ranking argument.

The [complete written construction](audit/frozen/benzel-p7-cumulative-through-turn10/current/turn10/PROOF.md)
covers d >= 2 and 0 <= h <= d(d-1)/2, using exactly d(d-1)/2-h right stones
and 3h(h+d) bones. Its exact source tables, preceding proofs and constructor
are preserved together. The full P7 assembly separately cites generalized
compression for the remaining residue-two class.

The [checked Lean edition](lean-checked/README.md) proves the five local positive
patch partitions, their translations and non-overlap, and the boundary equation
for every horizontal band length. In particular, `Benzel.bandSlide_correct`
proves the previously unproved band-slide target. These are kernel-checked
steps of the construction, not a formal proof of the complete tiling theorem.

## What was checked

- [18 September audit](audit/report/AUDIT_REPORT.pdf): separately written
  checking implementations, reconstructed unbounded identities and source
  bounds, and a recorded larger finite sweep. This was AI-assisted validation
  by the same assistant, not an audit of every lemma in Sharma's manuscript.
- [19 September fresh replay](fresh-replay/REPLAY.md): 18 polynomial identities,
  6,559 affine certificates, 24 complete tiling certificates and 13 rejected
  malformed inputs. All mathematical outputs matched the supplied records.
- [Lean receipt](lean-checked/receipts/KERNEL_CHECK.json): eleven source modules
  checked with Lean 4.32.0 and 39 named transitive axiom reports. The reproduced
  source and exact type assignment are included. The portable replay also
  checks the public entry-point module; its result is in `lean-checked/replay/`.

## Why this work exists

This project pursued Propp's Problem 7 before discovering Akshat Sharma's
earlier [8 September manuscript submission](https://mathdb.com/p/405267/existence-of-benzel-tilings-with-nonnegative-conway-lagarias).
The construction already in progress was then completed and examined. That
history motivates sharing a readable mathematical account and reusable checks,
not claiming first priority. The centered placement is explicitly compared
with Sharma's prescribed staircase placement on the same region. The current
MathDB record labels his manuscript a full-solution claim, not an independently
verified resolution.

## Preserved inputs and reproduction

`audit/` is the unchanged supplied audit, including the complete turn-10
source closure. `lean/` is the unchanged, originally uncompiled Lean 4.31.0
handoff. `lean-checked/` is the separate tested Lean 4.32.0 edition; its README
lists the exact changes and formal scope. None of those historical snapshots
is silently assigned the status of a later check.

To repeat the small Python checks, copy `audit/` to a disposable working
directory (the scripts write receipts), and run:

```text
python audit/verify_bundle.py
python audit/check_polynomial_receipts.py
python audit/check_linear_receipts.py
python audit/quick_output_check.py
```

For Lean, prepare the pinned dependencies and run `lake env python verify.py`
inside `lean-checked/`. It compiles serially, verifies the precise theorem type
and checks all axiom reports. The Windows checker enforces a 4 GiB cap.

This is part of **PolyClank**, an open human–LLM mathematics collaboration.
Fork this repository, work with the proofs yourself or with your model, and
submit a pull request. Alternatively, open an issue with a link or attachment.
Name the source commit and provide an argument others can follow; the direction
of your contribution is yours to choose. Raw private conversations and Sharma's
copyrighted manuscript are not republished here.
