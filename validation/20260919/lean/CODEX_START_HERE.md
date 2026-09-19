# Codex: build an actual kernel-checked benzel formalization

## Mandate and immutable mathematical inputs

Work on the audited residual-packing/corner-repair proof. Do not swap to a proof
of a different tiling model, an existence theorem with an extra unproved premise,
or an audit of Sharma's proof. The original objects are in
`formal/Benzel/{Geometry,Tiles,Incidence,Specification}.lean`.

The source snapshot is
`reference/audit_snapshot/frozen/benzel-p7-cumulative-through-turn10/current/`.
All mathematical references in the task graph are relative to that directory.
The audit is at `reference/audit_snapshot/audit/`; it is a source of exact
certificates, not a Lean oracle. Its Python `PASS` values cannot be imported as
proofs. Preserve the original input manifest and keep every correction visible.

The supplied Lean source has NOT been elaborated. The first task is real
compilation and correction of any API/elaboration mistakes, without changing
mathematical definitions or quantifiers. No source-provided proof script is to be
marked complete merely because it contains no unfinished-proof keyword.

## First commands

1. Run the package's Python preflight/export checks.
2. In `formal/`, use `leanprover/lean4:v4.31.0` and the exact Mathlib commit
   `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. Run `lake update`, verify the resolved
   commit, and obtain its cache. Save the resolved Lake lock file.
3. Run `python tools/lean_check.py --stage starter` from the package root.
4. Repair and compile the handwritten modules before scaling up generated proofs.
   A compilation repair to a locked specification must preserve its displayed
   source equation, be recorded in a separate semantic-change report, and receive
   a deliberate lock update. Do not silently regenerate SPEC_LOCK.json.

## First complete mathematical target

Prove `Benzel.oneStone_correct : Benzel.OneStoneGoal` in
`Benzel/OneStoneProof.lean`.

The candidate is defined in `OneStone.lean`. For every d >= 3 it must tile the
original V(d+3h,2d+3h), h=C(d,2)-1, with the unique right stone at (0,0) and exactly
3h(h+d) bones, together with invariance under the original threefold rotation. The proof route is the written band-packing argument and positive
hole transport in `turn8/sources/turn6-PROOF.md`, sections on shifted sectors and
the one-stone path. Do not use any of the full q=3k+1 or q=3k+2 endpoint theorems
as a premise; this is a genuinely smaller independently inspectable subproof.

Formalize the inverse for `bandIndex`, prefix/tail containment, cross-sector
nonintersection, and the exact residual. The cell-difference minimum provides
the original rank-orbit inverse. The triangular rows are precisely where the
unshifted and shift-one constructions differ. Formalize that equality of actual
placed generators and the telescoping band homotopy. The coordinate transform
must act on the original tile lists, not only on their areas.

Run `python tools/lean_check.py --stage one-stone`. That command requires a
closed theorem, not a term of type `OneStoneGoal -> OneStoneGoal`.

## Full constructive residue-zero target

Port the deterministic constructor as `Benzel.construct : Nat -> Nat -> List Tile`
in `Benzel/Construction.lean`, and prove

```
Benzel.construct_correct : Benzel.ConstructionCorrect Benzel.construct
```

in `Benzel/Final.lean`. The target quantifies over ALL d >= 2 and h <= C(d,2),
requires original-cell incidence one, and retains both exact tile counts.
Invalid-input behavior may be totalized separately; it cannot shrink the proved
admissible domain. Do not make an arbitrary classical-choice constructor and
then call it the audited algorithm. Port each original generator/index formula
and prove the list/multiplicity correspondence.

Port every literal branch:
q=0; q=1,2,4,5; q=3k (k>=1); q=3k+1 and q=3k+2 (k>=4);
and q=7,8,10,11. The source-to-tail index maps include d=m. Retain the released
old bone when the intercorner channel has zero length. Keep empty index sets
empty, with separate proofs of every nonnegative count; do not silently truncate
an invalid negative count to Nat zero.

Run `python tools/lean_check.py --stage residue-zero` only after the closed theorem
exists. A successful source generator or a finite tiling sweep cannot replace it.

## Certificate route: required semantic chain

For every polynomial certificate, complete all of these links:

* original placed tiles and index domains -> finite Laurent sum;
* typed six-variable expression -> sparse integer coefficient map;
* a kernel-checked coefficient equality -> equality of that SAME expression;
* explicit parameter specialization and its original coefficient-ring map;
* injective localization at the stated nonzero cell-variable denominators;
* original cell incidence equality;
* source ownership, distinct removal, and nonnegative output -> exact positive tiling.

For every affine certificate, reconstruct the row constraints from the typed
original tile/owner data. Verify nonnegative rational multipliers and their exact
weighted coefficient equality inside Lean. An external optimizer may propose
multipliers, but its status contributes no assumption. `Certificate/Affine.lean`
contains a soundness proof script for the arithmetic combination; that still needs
compilation and application to the reified original constraints.

The generated Lean tables retain all 274 owner records. They must not be dropped
from the formal source construction. `check_generated_data.py` parses the emitted
Lean syntax back into the original arrays, including the inverse permutation of
the double-family inner-count coefficients.

## Split-Zero integration

Use the actual original library, pinned at
`zeta-function-research-reader@1c8ec52c85c173adc9f8403a8a26914955e2f5a9`.
`tools/fetch_splitzero.py` accepts either an existing source directory or an
explicit download. It checks every Git blob, including the original scalar core
materialized by upstream prepare.py. It never edits the user's original checkout.

After materialization, copy `lakefile.with-splitzero.toml` over the local
`lakefile.toml` and build `BenzelWithSplitZero`. Check the Mathlib pin again.
`Optional/SplitZeroAdapter.lean` starts the actual finite-support Window and
inclusion ChainMap. Finish their coherence and the complete release
ComplexDiagram, then use the upstream reconstruction and universal properties.

Keep the extra bottom distinct from the nonbottom empty release set. For a
residual Z, the latter has physical support Z; bottom has empty physical support.
The supported differential and its source/target degree must stay typed.
Retain the whole quotient-kernel equivalence, the all-contained-bones receiving
map, the integer matching kernel coordinates, and the nonnegative charge-one
fibre. Do not equate integral solvability with positive tileability.

## Global theorem and published input

The full target is `Benzel.FullP7Goal`. Its original invariant has the explicitly
recorded factor-of-two numerator relation. The residue-one construction must be
formalized. The generalized-compression input for residue two is still a separate
formalization task; it must not be introduced as an axiom. A completed residue-zero
formalization is a real stopping milestone even before that larger literature
formalization is finished. Only `--stage global` may report a full P7 Lean theorem.

## Acceptance and handback

Use ordinary proof-producing tactics (`omega`, `ring`, `norm_num`, exact proof
terms, and small `decide`). Do not use unfinished-proof terms, new axioms,
compiler-trust/native-decision escapes, opaque external Boolean certificates,
or a changed theorem statement. Keep coefficient rings, all quantifiers, source
indices and positivity visible.

The gate compiles the exact requested module and an additional type-ascription
file, then checks every `#print axioms` report for missing or unexpected entries.
Only propext, Quot.sound and Classical.choice are allowed in the selected closure.
The policy scan is only an extra control; it is not a replacement for kernel
checking. A build with the final theorem absent cannot pass the final gate.

Return the source diff, pinned dependencies, exact commands, build/axiom logs,
statement comparison, and manifest. Report the strongest CLOSED theorem actually
checked. Keep all uncompleted task IDs open. Do not claim a whole-library audit
from a small selected declaration list.
