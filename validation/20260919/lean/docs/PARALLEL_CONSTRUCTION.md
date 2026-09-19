# The parallel construction and a smaller formal target

## Three precise relationships

The audited full residual-and-repair construction is parallel to Sharma's
staircase/layer construction. They address the same original existence statement.
Our earlier positive band-slide proof is a standalone proof of a subfamily of our
construction, through the domain map d -> (d,C(d,2)-1). It is not presented as a
second finished proof for arbitrary h. Its explicit final tiles equal the
shift-one packing plus the centered right stone.

The earlier fixed-collar constructors are also retained in the cumulative work.
Their relationship to the full theorem is the inclusion d -> (d,h0) of their
proved parameter domains. Equality of their incidence images puts the difference
of two output tilings in the original integral incidence kernel. That identity
alone does not assert a sequence of positive local moves between arbitrary output
pairs. No such unconstructed connectivity statement is needed here.

## Concrete additional property

For every d >= 3 put s=h=C(d,2)-1. The positive band-slide construction tiles

    V((3d^2-d-6)/2, (3d^2+d-6)/2)

with the sole right stone R(0,0). It is invariant under the original rotation
rho(x,y)=(y,1-x-y). Its packing consists of all F rho^p images, p=0,1,2, of the
stated horizontal bands. On original cells rho F = F rho^2, so rotation merely
permutes those sectors. The central stone is fixed.

Sharma's supplied manuscript defines

    P(s,d;c,r)=(-d-2s+2+2c+r, d+s-2-c-2r, s-c+r),

with c,r>=0 and c+r<=d-2, then removes the first s positions in the order of
increasing r and, for each r, decreasing c. On the one-stone ray all but the last
position are removed. The last position is c=0,r=d-2, so its original barycentric
anchor is exactly

    P_last=(-2s, s-d+2, s+d-2).

The coordinate map from our axial cells is (x,y)->(x,y,1-x-y), with projection
onto the first two coordinates as inverse. Both constructions therefore refer to
the same original benzel. For d>=3, s>=2. Each cell of Sharma's prescribed stone
has first coordinate -2s or 1-2s, whereas the central stone has only 0 or 1.
Thus the actual prescribed stones are disjoint. No truth of the other manuscript's
final existence theorem is assumed in this comparison.

For d=3, s=2, the common region is V(9,12). Our barycentric stone is

    {(1,0,0),(0,1,0),(0,0,1)}.

The staircase anchor is (-4,1,3), giving the actual stone

    {(-3,1,3),(-4,2,3),(-4,1,4)}.

Translation by minus that anchor identifies the two three-cell tiles, with
inverse translation by that anchor, but also translates the ambient benzel.
That observation is not used to identify the two tilings inside a fixed region.
The same-region comparison above uses the identity on the original cells.

A right-stone anchor (x,y) rotates to (y,-x-y). The fixed-point equations force
x=y=0. Thus a rotationally invariant tiling with exactly one right stone has that
stone at the center. The centered construction records a genuine additional
placement/symmetry property. Its novelty is not determined by this comparison.

## The explicit band homotopy

For r=d-2,d-3,...,1 and j=0,...,C(r+1,2)-1, move

    H(1-r^2+3j, C(r+1,2))
      -> H(2-r^2+3j, C(r+1,2)),

together with the other two rotations. The old and new band differ only at

    P_r=(C(r+2,2), C(r+1,2)),
    Q_r=(1-r^2, C(r+1,2)).

The signed tile-chain difference has boundary [P_r]-[Q_r]. The actual positive
slides move a vacancy from the right to the left endpoint, one original bone at
a time, and their reverse is the inverse move. The endpoints satisfy
P_r=p_(r+2), Q_r=rho^2 p_(r+1), where p_d=(C(d,2),C(d,2)-d+1).
Their three orbits telescope to the central stone cells. The actual source
membership and nonintersection argument is preserved in the full turn-6 proof.

Exactly 3*C(d,3) old bones participate in this specified transport. No minimum
claim is made. The map on each three-path support is an original cochain homotopy;
its Split-Zero reconstruction preserves the support labels and the actual local
zero, while the positive partition establishes the required charge-one fibre.

## Sources and scope

Source for the standalone proof and tables:
`../reference/audit_snapshot/frozen/benzel-p7-cumulative-through-turn10/current/turn8/sources/turn6-PROOF.md`
and `turn8/packing.py` (`one_stone_bands`, `one_stone_transport`).

Source for the other placement: the supplied Akshat Sharma manuscript, Chapter 1,
equations (1.15)--(1.17) and Section 1.5, PDF pages 5--6. Its supplied SHA-256 is
3b2a36d9ce12d7e2caa7d4da5d0960af854c972763563330b78b487deae2a5c0.
That PDF is not copied into this handoff. This is a comparison of specified
constructions, not a full audit of Sharma's proof and not a priority determination.

The new finite comparison/transport checks are in
`../evidence/parallel-construction.json` and `../evidence/handoff-checks.json`.
The all-parameter statement is the earlier written proof, not an extrapolation
from those checks. The Lean candidate remains uncompiled at handoff.
