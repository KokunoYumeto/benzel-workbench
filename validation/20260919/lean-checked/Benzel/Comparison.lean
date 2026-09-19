import Benzel.Tiles

namespace Benzel

/-- Projection of Sharma's sum-zero candidate anchor to its first two coordinates.
Source manuscript equations (1.15)--(1.17), not a replacement tiling algorithm. -/
def staircaseAnchor (s d c r : ℤ) : Cell :=
  (-d-2*s+2+2*c+r, d+s-2-c-2*r)

/-- The last staircase index in the one-stone case is (c,r)=(0,d-2). -/
theorem last_staircase_anchor (s d : ℤ) :
    staircaseAnchor s d 0 (d-2) = (-2*s,s-d+2) := by
  apply Prod.ext <;> dsimp [staircaseAnchor] <;> ring

/-- On the same cell carrier the central cell is not in that off-center stone.
This is a concrete witness, not a claim that the methods have no relationship. -/
theorem center_not_last_staircase (s d : ℤ) (hs : 1 ≤ s) :
    (0,0) ∉ (tile .right (-2*s) (s-d+2)).cells := by
  simp only [Tile.cells,offsets,tile,List.map_cons,List.map_nil,
    List.mem_cons,List.not_mem_nil,or_false,Prod.mk_add_mk,Prod.mk.injEq]
  omega

theorem center_mem_our_stone : (0,0) ∈ (tile .right 0 0).cells := by
  decide

/-- The unique fixed right-stone anchor under the original order-three action. -/
theorem fixed_right_anchor (x y : ℤ) :
    rotateTile (tile .right x y) = tile .right x y ↔ x=0 ∧ y=0 := by
  constructor
  · intro h
    have ha := congrArg Tile.anchor h
    have hx := congrArg Prod.fst ha
    have hy := congrArg Prod.snd ha
    dsimp [rotateTile,tile] at hx hy
    omega
  · rintro ⟨rfl,rfl⟩
    rfl

end Benzel
