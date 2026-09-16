# Benzel turn8 integration review — 16 September 2026

## Claim and primary verdict

**Proved as written at the stated construction scope**, with the exact coefficient certificate checked by executable integer arithmetic and the matching-to-all-bones distinction made explicit in `MORPHISM_ADDENDUM.md`. This is a bounded integration review by a separate model agent, not specialist acceptance or novelty certification.

For all integers k>=1, m>=3k+2, d>=m, set Delta=m(m-1)/2-3k and h=d(d-1)/2-Delta. The supplied constructor gives a tiling of V(d+3h,2d+3h), and its reflected region, with exactly Delta right stones and 3h(h+d) bones. It does **not** resolve the full Propp Problem7 or uniformly treat the other two deletion residues.

Reviewed revision: `KokunoYumeto/mathematics-commons-pilot@20cb022dcfda7f37b3adec13b5619be8f13be3e8`, PR26, all16 added files under `workbenches/splitzero-nonzeta/sprints/benzel-p7/turn8/`. Local reviewed bytes match all16 live PR Git blob identities (`independent-checks.json`). No source changes or remote mutations were made by this reviewer.

## Dependency graph and exact checks

1. Original axial inequalities and R/H/V/D tiles agree with the corpus-routed `benzels_full_reconstruction.tex`, section “Axial coordinates and exact covers,” read in full for this dependency.
2. Retained `sources/turn6-PROOF.md` sections1–3 prove the actual parent matching and exact residual rank map. The proof supplies containment, pairwise sector disjointness, count, infinite residual inverse, and passage back to finite regions. These were read; the rest of the retained proof was also read but its ancillary fixed-q results are not prerequisites of turn8.
3. Turn8 section2 gives genuine source indices in both d=m finite tails and d>=m+1 prefixes. The tail inverse preserves original cells rather than enlarging a band.
4. The deleted stones are distinct source members. Every new coefficient is +1. The literal corner formulas in section3 independently expand to the JSON table for k=1,...,15, including k=1 and k=2 empty-range boundaries.
5. The six-variable Laurent certificate retains m and k independently; denominators involve only X,Y and remain nonzero under parameter specialization. Integer-domain localization is injective. Thus zero formal numerator implies the exact all-parameter original-cell identity, not an inference from sampled m,k.
6. Original source matching plus its disjoint residual makes the right side of the cell identity an indicator. Positive coefficients on the left then force containment and multiplicity one; adding frozen bones proves the full tiling.
7. The integral matching-kernel proof is the coefficient propagation argument on a bipartite cell graph. Closed-component sums are primitive disjoint-support relations; removing one pivot per closed component gives an integral basis. Forest-path cell duals have the required signs. Synthetic empty, shared-tile closed, old-only, new-only, and partially overlapping cases pass independently.
8. The support reconstruction and internal quotient match exact pinned source `zeta-function-research-reader@1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/tex/support_diagrams.tex`, D1–D8, read through its proofs. The augmented charge-one positive fibre is distinguished from signed boundary vanishing.
9. The matching quotient is not the all-contained-bone quotient. The attached addendum gives the actual maps and additional kernel `im(partial_U)/(B_A+B_B)` without assigning it zero. This clarification belongs in the repository with the proof, rather than only in the PR comment.

No failed mathematical step was found in this reviewed dependency chain. Original research status and nonclaims should remain visible. The exact matching-kernel rank is not a rank assertion about the full contained-bone quotient.

## Fresh computation

`run-review.ps1` runs the reviewed standard-library verifier serially in normal and optimized Python3.13.9, with bytecode disabled, a5,000,000,000-byte sampled physical-memory stop and180-second wall cap. Reviewed source launches no children. Actual peaks: normal97,169,408 bytes; optimized96,653,312 bytes. Actual elapsed times:20.032s and29.061s. Eleven input code/data/proof hashes were unchanged before and after.

Both full `--max-k 15` runs passed:

- 60 positive core partitions;
- 120 full/reflected tilings, 1,047,540 full tile placements;
- 314,460 source-to-receiving-generator checks;
- 24 independent region enumerations;
- 1,935 integer kernel duals across 10 comparisons;
- 80 augmented transition and 80 scalar/cochain checks;
- 279 exact band homotopies;
- 10 deliberate invalid-input/mutation rejections.

The formal main certificate contains222 rational terms and28,128 expanded numerator terms, with zero surviving coefficients. The separate k=1 certificate contains39 rational terms and510 expanded terms, also zero. All23 affine index-bound rows pass. These formal checks have their algebraic reduction in the proof; the listed finite windows are separate.

`independent_checks.py` additionally verifies all15 printed corner expansions, five synthetic kernel cases, and the16 remote blob identities. Raw receipts, result JSON, manifests and standard output are retained here.

## Live stack and integration recommendation

At inspection the stack is:

| PR | Head | Base | Added scope |
|---|---|---|---|
|23|038ed02bb524e60e9c2bd20c3a0aa02365f4001d|main|34 files: broad Split-Zero non-zeta portfolio plus Benzel turns1/2|
|24|d7cd069031536bea677ed31f7729ebdd4e9f97f6|PR23 branch|12 turn3 files|
|25|6fe012fd1facd564e07e1fa052ad219debdd8278|PR24 branch|10 turn4 files|
|26|20cb022dcfda7f37b3adec13b5619be8f13be3e8|PR25 branch|16 turn8 files|

All four were open drafts and mergeable. `main` did not contain `workbenches/splitzero-nonzeta/` at inspection. Merging only PR26 into its current base does not place it on main. Preserve ancestry and merge/rebase the reviewed stack in dependency order with explicit head pins and readback.

**Approve turn8 for research-workbench integration**, adding its morphism clarification and retaining exact scope. This reviewer inspected PR23–25 metadata/change scope, not every earlier proof: those ancestor mathematical claims are not newly certified by this review. PR23's portfolio extends far beyond Benzel; it can retain its research/draft labels in Commons, but should not become an unqualified Benzel theorem index or a claim of completed251-job execution.

For a dedicated Benzel mirror, preserve the whole relative prefix `workbenches/splitzero-nonzeta/sprints/benzel-p7/` so imports and historical source links still resolve. Include relevant `METHOD.md`, source provenance and the bounded review alongside navigation, without presenting unrelated portfolio research as a Benzel result. The attached turn8 `sources/`, `evidence/`, `exploration/` and all constructor files can be placed under the same turn8 directory after root's publication-safety check. The required retained turn6 proof already makes turn8 self-contained; missing historical turns5–7 must not be described as remotely archived in full. No third-party paper/PDF corpus or private transcript needs publication for this replay.

## Additional ancestor integration smoke

After the main review, root requested a short PR23–25 source-safety/import-closure pass. The exact staged historical Benzel sprint files were copied into this review directory; no staged source was modified. AST inspection rejected process/network imports and dynamic eval/exec in the copied Python sources. The diff metadata adds no workflows. The portfolio dispatcher was separately read: it writes local job-description files, has no network/agent launcher, and was not executed. Instructions contained in those job descriptions were treated as data.

The serial smoke completed in 3.135 seconds at a sampled 30,703,616-byte working-set peak, under the same 5 GB / 120-second stop. `check.py`, `check_turn2.py`, `turn2/check.py`, `turn3/fixtures.py`, `turn3/check.py`, and `turn4/verify.py` all passed; finite d was restricted to at most 8. Turn3 also regenerated its 8,919 exact all-parameter collision certificates and passed seven negative controls. Turn4 passed 21,545 finite bone-dual evaluations, 17,928 finite algebra identities, its parameter-interval checks and six negative controls. This strengthens integration evidence but does not independently re-audit every earlier written proof.

**Runtime closure:** the full Benzel sprint prefix is enough. The root checker is self-contained; both turn2 checkers depend only on that root checker and their sprint fixtures; turn3 imports only its own construction/certify/affine/polygons and tables; turn4 imports the sibling turn3 construction/tables. No sprint checker imports an external `review/tools/benzel.py`. `turn3/fixtures.py` must be run before the turn3 check when generated fixture JSON is absent; it recreates exact hash-pinned fixtures and refuses to overwrite different bytes. The smoke generated these only in the review copy.

Evidence: `ancestor-smoke.json`, `ancestor.run.json`, `ancestor.stdout.txt`, the six `smoke_*` result folders, and copied source hashes. These are separate smoke receipts, not replacements for historical records or the main turn8 proof audit.
