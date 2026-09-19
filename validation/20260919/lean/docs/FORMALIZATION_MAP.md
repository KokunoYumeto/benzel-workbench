# Proof map: original mathematics -> Lean objects

| Original object / argument | Starter object | Remaining formal work |
|---|---|---|
| Axial cell and sum-one barycentric cell | `Cell`, `BaryCell`, `axialBaryEquiv` | Compile inverse proof scripts; relate the literal original bound equations. |
| Four original types of placed tiles | `Kind`, `Tile`, `Tile.cells` | Compile; prove rotation/reflection cell permutations and list-to-Fin-3 correspondence. |
| Original integer incidence map | `boundary : TileChain ->ₗ[Z] CellChain` | Compile `boundary_listChain`; establish positivity/occurrence equivalence once. |
| Region equation with nonnegative coefficients | `IsTiling`, `IsTilingList` | Prove the exact list/multiset equivalence and tile-count transport. |
| Canonical triangular inverse | `triangular`, `bandIndex`, `route` | Prove the square-root domain, unique m, original inverse parameters, and exhaustive route bounds. |
| One-stone shifted packing | `oneStoneCandidate` | Close `OneStoneGoal` via the actual band and residual proof; then the rotational-symmetry refinement. |
| Five fixed endpoint partitions | `Generated.LocalPatches` | Kernel-check the constant permutation/Nodup scripts and their translations. |
| Uniform q=3k families | `Generated.Threefold` | Full index/domain semantics, polynomial identity and positive source inclusion. |
| Both asymmetric edits and four exceptions | Six generated `EditGroup` lists | Reify scaffold/source rows, certify actual owners, nonnegative lengths, and all endpoints. |
| Exact affine certificates | `Certificate.dot`, `combination_nonnegative` | Compile soundness and generate coefficient equalities tied to reconstructed original constraints. |
| Six-variable Laurent specialization | `Certificate.specializeExponent` | Extend to the actual group algebras; finite-sum identities; denominators and injective localization. |
| Incoming finite-support bone differential | Optional `localBoundary`, `localWindow` | Compile against pinned upstream; all inclusion maps and coherence. |
| Full support reconstruction and internal quotient | Original upstream `LinearDiagram`, `ComplexDiagram` | Construct the concrete release diagram; invoke original D1--D8 interfaces without erasing a label. |
| Killed representatives / original boundaries | Optional `supportKernelEquiv` | Compile; relate the concrete matching and all-contained-bones maps; retain full kernel and integral duals. |
| Positive charge-one fibre | `augmented`, `charge_one_cycle` | Compile; construct its charge-dependent transitions and full positive-fibre equivalence. |
| All residue-zero d,h | `ConstructionCorrect` | Port `complete_W` and prove closed `construct_correct`. No mathematical premise can assume that conclusion. |
| Full original P7 | `FullP7Goal` | Direct residue one and formal proof of published residue-two input; never add an axiom for compression. |

## Original certificate locations

Relative to the frozen `current/` directory:

* `turn8/families.json`, `bivariate_certificate.py`, `PROOF.md` and
  `sources/turn6-PROOF.md` supply the stable packing and threefold family.
* `turn9/edits.json`, `source_table.py`, `ownership-certificates.json`,
  `symbolic_certificate.py`, `PROOF.md` supply q=3k+1.
* `turn10/edits.json`, four `edits-k*-r*.json`, `source10.py`,
  `source-domain-certificates.json`, ownership receipts, fixed endpoint JSON,
  `symbolic_certificate.py`, `small_symbolic.py`, `complete_theorem.py`, and
  `PROOF.{md,tex}` supply q=3k+2, exceptions, and exhaustive assembly.
* `turn7/templates.json` plus its original constructor supply q=1,2,4,5.

The separately written audit is under `reference/audit_snapshot/audit/`. Its
receipt files bind each polynomial and affine target to source bytes. Copying a
receipt or trusting its status is not a formal proof: the original expression
must elaborate into the equality being kernel-checked.

## Dependency pin and original source API

Lean: leanprover/lean4:v4.31.0.
Mathlib: fabf563a7c95a166b8d7b6efca11c8b4dc9d911f.
Original SplitZero: zeta-function-research-reader at
1c8ec52c85c173adc9f8403a8a26914955e2f5a9.

The following names were checked in that source:

* `SplitZero.Reconstruction.LinearDiagram`, `.Total`, and its reconstruction;
* `SplitZero.Homology.Window` and `ChainMap`;
* `Window.boundaryToCycles`, `.boundaries`, `.classOf`;
* `ChainMap.onHomology`, `.homologyKernelEquiv`;
* `SplitZero.InternalHomology.ComplexDiagram`, `.cycles`, `.boundaries`, `.homology`;
* `ComplexDiagram.differential_square`, `.cycle_condition`, `.homology_coequalizer`.

The upstream scalar core is separately pinned by its own original Git blob
ff991f7383922e71cdf0e4a3bc85e89e18f808ef; `fetch_splitzero.py` preserves that source.
The new adapter has not been compiled. A source API check is not proof of new
adapter elaboration or of the final benzel theorem.

## Natural/integer parameter transport

The program indexes d,h by natural numbers. The original nonnegative integer
parameters map to those by `(d.toNat,h.toNat)`, with inverse integer cast.
`Parameters.lean` supplies both inverse proof scripts. `twice_triangular` relates
the recursive natural triangular number to the original integer polynomial.
The final original-parameter assembly must transport the admissibility bounds
through these maps, rather than silently omit the integer formulation.
