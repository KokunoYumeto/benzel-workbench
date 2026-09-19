import Benzel.Tiles

namespace Benzel

/-- The literal sector-one tail generator before and after the original maps. -/
def commonOneTail (m row depth : ℤ) : Tile :=
  reflectTile (rotateTile (tile .horizontal (row-m-2-3*depth) row))

/-- First `channel-low` source in turn10/edits.json.
Its original coordinates are matched, not inferred from an incidence class. -/
theorem channel_low_original_owner (m k i : ℤ) :
    commonOneTail m (3*k+i+3) (k+1) =
      tile .vertical (3*k+i+3) (i-m-2) := by
  dsimp [commonOneTail,reflectTile,rotateTile,tile]
  apply congrArg (fun p : Cell => (⟨Kind.vertical,p⟩ : Tile))
  apply Prod.ext <;> dsimp <;> ring

/-- Actual integer bounds on that original source index. -/
theorem channel_low_domain (m k i : ℤ)
    (hk : 4 ≤ k) (hm : 3*k+4 ≤ m)
    (hi : 0 ≤ i) (hin : i < m-3*k-2) :
    3*k+2 < 3*k+i+3 ∧ 3*k+i+3 ≤ m ∧
    0 ≤ k+1 ∧ k+1 < 3*k+2 ∧ k+1 < 3*k+i+3 := by
  omega

/-- Finite-tail and stable bone indices, with the original affine inverse. -/
theorem receiving_index_inverse (q y j : ℤ) :
    (j+q-y)+y-q = j := by ring

end Benzel
