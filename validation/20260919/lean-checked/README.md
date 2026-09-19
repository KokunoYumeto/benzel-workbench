# Kernel-checked local moves and band transport

This is the checked, modest formalization of concrete steps in the Benzel
construction. The full supplied scaffold is preserved separately in `../lean/`.
The complete centered tiling and full Propp Problem 7 are not claimed formalized.

## Mathematical content

`Benzel.rowBand_boundary` proves, for **every** integer anchor `(x,y)` and every
natural band length `n`, that replacing the horizontal bones at
`(x+3j,y)` by those at `(x+1+3j,y)`, `0 <= j < n`, changes the cell vector by

```text
[x+3n,y] - [x,y].
```

The empty band is included. `Benzel.bandSlide_correct : Benzel.BandSlideGoal`
specializes this equation to the triangular-length bands in the centered
construction. It is a new completed proof of the exact specification in the
handoff. This boundary identity alone does not assert that the old bones are
present in an arbitrary surrounding tiling.

The five constant patches have kernel-checked equal cell-occurrence lists up
to permutation, no duplicate cells on either side, and valid translations at
every integer anchor. `Benzel.bridgeSix_boundary` derives the eight-bone
bridge's boundary equation from that positive partition. The coordinate maps
have checked inverse laws and region transport. The checked staircase
comparison and fixed-anchor equations make the central placement precise.
One original channel-owner formula and its full integer domain are also checked.

## Toolchain and changes to the handoff

The immutable handoff used Lean 4.31.0 and was uncompiled. This small checked
edition uses **Lean 4.32.0**, Mathlib
`81a5d257c8e410db227a6665ed08f64fea08e997`, reusing the existing local cache.
It did not build or mutate Mathlib. Imports were narrowed to avoid loading all
of Mathlib. Two proof scripts needed elaboration repairs: simplifying tuple
projections before `omega`, and simplifying the induction hypothesis together
with the list-incidence goal. The band definitions make the natural-number
map binder explicit; they retain the same integer anchors and index range.

The original source archive is unchanged. No definition of the region, tile,
positive tiling, or target theorem was weakened to make a proof pass.

The [receipt](receipts/KERNEL_CHECK.json) records eleven checked source modules
and 39 named transitive axiom reports. Only `propext`, `Classical.choice`, and
`Quot.sound` occur. No `sorryAx`, added theorem axiom, or native compiler-trust
proof occurs. The full construction targets remain definitions, not theorems.

## Reproduction

Prepare the pinned dependencies using Lake and the official Mathlib cache.
With that environment available, run `lake env python verify.py`. It compiles
the local modules serially and verifies the exact `BandSlideGoal` assignment
and all 39 axiom reports. It never launches a dependency build. On Windows,
install `psutil`; the checker enforces a 4 GiB whole-process-tree cap, one
logical CPU and one Lean worker, with a 180-second timeout per module.

The original local run additionally watched process memory; its successful
module peaks were about 0.9–1.1 GB resident. Larger proof targets were not
attempted. This is a deliberately bounded formal contribution.
