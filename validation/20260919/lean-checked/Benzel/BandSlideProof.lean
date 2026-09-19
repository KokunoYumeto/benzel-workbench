import Benzel.OneStone
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring

noncomputable section
namespace Benzel

/-- A literal row of n consecutive horizontal bones, at their original anchors. -/
def rowBand (x y : ℤ) (n : ℕ) : List Tile :=
  (List.range n).map (fun j : ℕ => tile .horizontal (x+3*(j : ℤ)) y)

theorem horizontal_shift_boundary (x y : ℤ) :
    tileVector (tile .horizontal (x+1) y) - tileVector (tile .horizontal x y) =
      cellVector (x+3,y) - cellVector (x,y) := by
  have h2 : x+1+1 = x+2 := by ring
  have h3 : x+1+2 = x+3 := by ring
  simp only [tileVector, Tile.cells, offsets, tile, List.map_cons, List.map_nil,
    List.sum_cons, List.sum_nil, Prod.mk_add_mk, add_zero, h2, h3]
  abel

/-- An exact incidence identity for every finite band, including the empty one.
This theorem does not assume the bones are present in a surrounding packing. -/
theorem rowBand_boundary (x y : ℤ) (n : ℕ) :
    boundary (listChain (rowBand (x+1) y n) - listChain (rowBand x y n)) =
      cellVector (x+3*(n : ℤ),y) - cellVector (x,y) := by
  induction n with
  | zero => simp [rowBand, listChain]
  | succ n ih =>
      have ht : x+1+3*(n : ℤ) = (x+3*(n : ℤ))+1 := by ring
      have he : x+3*(n+1 : ℕ) = (x+3*(n : ℤ))+3 := by push_cast; ring
      simp only [rowBand, List.range_succ, List.map_append, List.map_cons,
        List.map_nil, listChain, List.sum_append, List.sum_cons, List.sum_nil,
        add_zero, map_sub, map_add, boundary_single, one_smul] at ih ⊢
      rw [ht]
      have hs := horizontal_shift_boundary (x+3*(n : ℤ)) y
      rw [he]
      have hh := congrArg₂ (fun a b : CellChain => a+b) ih hs
      convert hh using 1 <;> abel

/-- The endpoint equation used by the centered construction, uniformly in r. -/
theorem bandSlide_correct : BandSlideGoal := by
  intro r hr
  have hrow := rowBand_boundary (1-(r : ℤ)^2) (triangular (r+1)) (triangular (r+1))
  have hx : (1-(r : ℤ)^2)+1 = 2-(r : ℤ)^2 := by ring
  have hp : 1-(r : ℤ)^2+3*(triangular (r+1) : ℤ) = (triangular (r+2) : ℤ) := by
    have h1 := twice_triangular (r+1)
    have h2 := twice_triangular (r+2)
    push_cast at h1 h2
    nlinarith
  simpa only [rowBand, slideOld, slideNew, startEndpoint, endEndpoint, hx, hp] using hrow

end Benzel
