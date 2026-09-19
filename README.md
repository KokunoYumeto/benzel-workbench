# Benzel tilings workbench

This PolyClank project studies James Propp's Problem 7 through explicit
tilings, geometric proofs and exact verification. It includes the complete
written residue-zero construction, an AI-assisted audit, and kernel-checked
local steps.

## Start with the mathematics

**[A centered stone and three rotating bands — six-page PDF](validation/20260919/CENTERED_ONE_STONE.pdf)**
([online exposition](validation/20260919/CENTERED_ONE_STONE.md),
[editable LaTeX](validation/20260919/CENTERED_ONE_STONE.tex)).

For every integer $d\ge3$, put $h=d(d-1)/2-1$. The original benzel
$V(d+3h,2d+3h)$ has an explicitly constructed tiling with the single central
stone $R(0,0)$ and $3h(h+d)$ straight bones, invariant under
$\rho(x,y)=(y,1-x-y)$. The reader defines these objects and proves containment,
non-overlap and coverage. For $d=3$ it constructs one stone and 30 bones in
$V(9,12)$.

![One central stone and 30 bones](validation/20260919/centered-example.png)

## Complete construction and exact validation

The [turn-10 proof and constructor](validation/20260919/audit/frozen/benzel-p7-cumulative-through-turn10/current/turn10/PROOF.md)
cover every $d\ge2$ and $0\le h\le\binom d2$, returning exactly
$\binom d2-h$ right stones and $3h(h+d)$ bones. All deletion residues and
small exceptions are included. The full Problem 7 assembly also uses the
published generalized-compression theorem for the residue-two class.

The [AI-assisted audit](validation/20260919/audit/report/AUDIT_REPORT.pdf)
uses separately implemented original-cell checks, parameter-preserving
identities and source-membership bounds. A [fresh replay](validation/20260919/fresh-replay/REPLAY.md)
passed 18 exported polynomial identities, 6,559 affine certificates and
24 complete tiling checks; 13 deliberately malformed inputs were rejected.
The unbounded argument is in the mathematical sources, not inferred from
the size of a finite test.

The [Lean contribution](validation/20260919/lean-checked/README.md) checks the
five positive local patches, their translations and non-overlap, and the
band-slide boundary equation **for every band length**. It includes 39 named
transitive axiom reports. The complete centered tiling and full P7 theorem
are not yet formalized.

## Why this work exists

The construction was pursued before the project learned of Akshat Sharma's
earlier *A Constructive Proof of Propp's Problem 7*, submitted on 8 September
2026. The construction already in progress was then completed and examined.
This is not a first-priority claim or a line-by-line validation of Sharma's
manuscript. His [MathDB submission](https://mathdb.com/p/405267/existence-of-benzel-tilings-with-nonnegative-conway-lagarias)
is currently marked claimed solved, independently unverified.

The centered theorem supplies a placement and symmetry property compared
with his prescribed staircase output; the reader checks both placements
in the same original region. The original AI audit used different checking
implementations but the same assistant. It is AI-assisted validation, not
independent human peer review.

Primary references: [Propp's problem paper](https://arxiv.org/abs/2206.06472),
[Kim–Propp on tribone tilings](https://arxiv.org/abs/2206.04223), and
[Defant–Foster–Li–Propp–Young on generalized compression](https://doi.org/10.1137/24M1648247).
The [September 19 edition](validation/20260919/README.md) links the complete
proof sources, original audit, unmodified handoff, checked Lean edition
and reproduction instructions.

## PolyClank: how to contribute

PolyClank is an open human–LLM collaboration under the public name Kokuno
Yumeto. Fork or download this repository, work with the relevant files
yourself or with your model, and submit a pull request. Alternatively, open
an issue with an attached argument or a link to your repository. Include
the source commit and provide an explanation another mathematician can
follow. The direction of your contribution is yours to choose.

The project began in the [Mathematics Commons pilot](https://github.com/KokunoYumeto/mathematics-commons-pilot).
[Section 10 of the complete construction](validation/20260919/audit/frozen/benzel-p7-cumulative-through-turn10/current/turn10/PROOF.md)
records the incidence maps, support changes, comparison kernels and positive
filling fibres associated with the [Split-Zero programme](https://github.com/KokunoYumeto/zeta-function-research-reader).
No analytic zeta connection is inferred merely from that use.

Earlier editions remain available: [turn-9 cumulative reader](readers/20260917/Cumulative_Research_Record.pdf),
[September 17 source record](integration/20260917/README.md), and
[original cumulative archive](archives/20260917/benzel-p7-cumulative-through-turn9.zip).
Their incomplete-case descriptions are historical. Source attribution remains
controlling; no blanket third-party license, raw private transcript, or
copyrighted literature PDF is added by this edition.
