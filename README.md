# Benzel tilings workbench

A PolyClank research workbench for James Propp's Benzel Problem 7: explicit
tilings, original-cell constructions, polynomial certificates, comparison maps,
and the history of approaches that led to them.

## Current construction

The [turn 8 proof](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn8/PROOF.md)
constructs a tiling for every integer triple k ≥ 1, m ≥ 3k + 2, d ≥ m, with
Δ = m(m−1)/2 − 3k and h = d(d−1)/2 − m(m−1)/2 + 3k. The original benzel
V(d+3h, 2d+3h) is tiled by Δ right stones and 3h(h+d) bones. Reflection supplies
the reversed-parameter family. This covers the positive deletion counts q = 3k;
it is not a resolution of the remaining two residue classes or of all Problem 7.

- [Read and reproduce turn 8](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn8/README.md).
- [Inspect the explicit constructors and comparison maps](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn8/).
- [Read the original-lattice morphism addendum](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn8/delivery/MORPHISM_ADDENDUM.md).
- [Follow the earlier constructions](workbenches/splitzero-nonzeta/sprints/benzel-p7/).
- [See the unfinished approaches and their outcomes](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn8/EXPLORATION.md).
- [Review the September 16 integration and checks](integration/20260916/README.md).

The core replay uses Python's standard library and exact arithmetic; it does not
require a tiling solver or Lean. The full supplied exploration is preserved
separately and is not promoted to a proved construction merely by inclusion.

## Provenance and collaboration

The work began in the [Mathematics Commons pilot](https://github.com/KokunoYumeto/mathematics-commons-pilot),
in PRs 23–26. This dedicated repository retains the original paths and complete
Benzel development, with the additional delivered checks and exploration. Its
[methodology](workbenches/splitzero-nonzeta/METHOD.md) records the relationship to
the [Split-Zero programme](https://github.com/KokunoYumeto/zeta-function-research-reader).
Original-cell maps, integer kernels, support complexes, and their exact source
versions are part of the proof; an analytic zeta conclusion is not imported.

This is human–LLM research under the public collaboration name Kokuno Yumeto.
Attribution inside the source records remains controlling. Existing proof,
computation and independent-review scopes are kept distinct. Source authors are
credited for their own work; no blanket third-party license is asserted.

Issues and pull requests are welcome. Identify the exact construction, retain
its original coordinates and hypotheses, and say what you checked. Corrections,
alternative proofs, exact counterexamples, and usable new tilings all count as
contributions. No raw private conversations or bulk copyrighted library are
included.
