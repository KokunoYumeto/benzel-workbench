# Benzel tilings workbench

A PolyClank research workbench for James Propp's Benzel Problem 7: explicit
tilings, original-cell constructions, polynomial certificates, comparison maps,
and the history of approaches that led to them.

## Read the current work

- [Cumulative reader through turn 9 (100-page PDF)](readers/20260917/Cumulative_Research_Record.pdf) and [editable LaTeX](readers/20260917/latex/).
- [New turn-9 proof](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn9/PROOF.md), [constructor, source tables and exact certificates](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn9/), and [reproduction instructions](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn9/README.md).
- [Complete supplied cumulative archive](archives/20260917/benzel-p7-cumulative-through-turn9.zip), including the nine original ZIP handbacks, historical source variants and earlier proof editions.
- [September 17 edition and provenance](integration/20260917/README.md), including the distinction between recorded checks and independent mathematical review.

The new turn-9 manuscript is a **research construction pending independent
review**. The full original Problem 7 is not declared solved.

## The two unbounded construction families

Write $t_n=n(n-1)/2$, choose a positive deletion count $q$, and put

$$
\Delta=t_m-q,\qquad h=t_d-\Delta.
$$

The target is the original benzel

$$
W_h(d)=V(d+3h,2d+3h),
$$

tiled by exactly $\Delta$ right stones and $3h(h+d)$ bones. In axial cell
coordinates, a right stone has offsets $(0,0),(1,0),(0,1)$; the three bone
orientations have offsets $(0,0),(1,0),(2,0)$, $(0,0),(0,1),(0,2)$, and
$(0,0),(1,-1),(2,-2)$. All constructions use these original placed tiles.

| Manuscript | Deletion count | Complete stated parameter range | Review status |
|---|---|---|---|
| [Turn 8](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn8/PROOF.md) | $q=3k$ | $k\ge1$, $m\ge3k+2$, $d\ge m$ | Prior scoped proof/computation review and full replay retained in the [September 16 record](integration/20260916/README.md). |
| [Turn 9](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn9/PROOF.md) | $q=3k+1$ | $k\ge4$, $m\ge3k+3$, $d\ge m$ | Written research proof, symbolic/source certificates and recorded finite replays; independent review pending. |

Reflection supplies the reversed parameter pairs. The turn-9 family includes
$q=13,16,19,22,\ldots$ without an upper cutoff. Its smaller $k$ values keep
their earlier individual statuses. The remaining unbounded $q=3k+2$ positive
endpoint is not supplied by this continuation.

### What changes in turn 9

The earlier symmetric $q=3k$ replacement is translated and one additional
original corner stone is removed. This produces an explicit scaffold with
18 uncovered cells. Two connected endpoint repairs transport and fill those
vacancies using positive partitions of the original cells. Every released
bone has an explicit source index in the scaffold; the exact affine
certificates check those indices, their ranges and their distinctness.

If $A$ is the common source-bone family, $B'$ the repaired bone family, $S$
the retained stones and $\partial$ the original tile-to-cell incidence map,
the construction's central identity is

$$
\partial(B'+S)=\mathbf1_{\Omega_\Delta}+\partial A.
$$

Here $\Omega_\Delta$ is the original uncovered core. Adjoining the frozen
outer bones gives the full positive tiling

$$
\bigl(\Gamma_\Delta(d,h)\setminus A\bigr)\cup B'\cup S.
$$

The proof includes the endpoint $m=3k+3$: the channel has length zero there,
but one old vertical bone still has to be released. It also calculates the
receiving indices at $d=m$, so the construction includes the smallest
exterior parameter rather than only an eventual range. These endpoint and
source calculations are in [proof Sections 2–7](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn9/PROOF.md).

The exact Laurent identities retain both parameters before specialization.
The supplied normal and optimized finite replays cover $k=4,\ldots,10$,
21 positive cores and 84 full/reflected tilings. Those are additional checks,
not the source of the unbounded quantifiers; see the [recorded scope](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn9/recorded-checks.json).
The standard-library constructor and final certificate verifiers require
neither a tiling solver nor Lean. The optional multiplier-discovery script
uses NumPy/SciPy; its numerical solver statuses are not the final certificates.

## Source history and collaboration

The work began in the [Mathematics Commons pilot](https://github.com/KokunoYumeto/mathematics-commons-pilot),
in PRs 23–26. This dedicated repository preserves its original paths and prior
editions. Turn 9 is additive; the turn-8 dependency files and earlier review
have not been overwritten. The cumulative archive also preserves material
that was recovered separately from the original ZIPs. It is a conversation
delivery archive, not a complete Git clone; its source-recovery gaps remain
documented in the [supplied README](integration/20260917/SUPPLIED_README.md).

The [methodology](workbenches/splitzero-nonzeta/METHOD.md) records the
relationship to the [Split-Zero programme](https://github.com/KokunoYumeto/zeta-function-research-reader).
Turn 9 makes the local vacancy moves into explicit cochain homotopies on
marked cells and placed bones, retaining support labels and the positive
tiling fibre; see [Section 8](workbenches/splitzero-nonzeta/sprints/benzel-p7/turn9/PROOF.md).
This is a concrete use of that algebraic machinery, not an analytic zeta claim.

PolyClank is an open human–LLM collaboration under the public name Kokuno
Yumeto. To participate, download or fork this repository, give the relevant
proof and source files to your own model or work on them yourself, and submit
your results as a pull request. An issue with an attached argument, code or a
link to your own repository works too. Include the source commit you started
from and distinguish what you proved, computed or conjectured. Contributions
need not follow a prescribed direction; their mathematical content can be
read and developed in its own right.

Attribution inside the source records remains controlling. Proof, computation
and independent-review scopes stay distinct. Source authors are credited for
their own work; no blanket third-party license is asserted. No raw private
conversations or bulk copyrighted library are included.
