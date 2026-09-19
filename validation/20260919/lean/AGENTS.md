# Working instructions for this formalization

Read CODEX_START_HERE.md and TASKS.json before editing. The expected theorem
statements are in formal/Benzel/Specification.lean and OneStone.lean. Preserve the
original cell, tile, invariant, parameter and positivity semantics.

Do not change reference/audit_snapshot. Add corrections and their proofs in new
files. The historical audit is evidence, not a Lean oracle or a novelty claim.

This handoff has no completed Lean build. First compile the starter, then close
the one-stone theorem and the full constructor in separate audited milestones.
Do not insert proof placeholders, theorem assumptions encoding the desired
conclusion, new axioms, native_decide, unsafe proof production, or trust options.
Do not weaken the specification to a finite range, a signed tiling, an arbitrary
constructor, a quotient with erased torsion, or an already assumed positive lift.

When an obstruction appears, save its actual original-generator equation and
change the next task accordingly. Preserve inverse maps and source-index bounds.
Mathematical refactoring needs an explicit equivalence and statement audit.

Keep remote writes additive and explicitly scoped. This handoff does not authorize
merges, publication announcements, paid computation, or downstream agent launch.
