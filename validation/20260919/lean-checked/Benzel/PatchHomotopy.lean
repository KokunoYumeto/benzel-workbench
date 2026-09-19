import Benzel.Incidence
import Benzel.Generated.LocalPatches

noncomputable section
namespace Benzel

/-- Permutations concern cell occurrences, so overlapping copies cannot disappear. -/
theorem patch_homotopy {old new : List Tile} {before after : List Cell}
    (h : (patchCells old before).Perm (patchCells new after)) :
    boundary (listChain new-listChain old) = cellsChain before-cellsChain after := by
  have he := cellsChain_perm h
  have hv : cellsChain (occurrences old)+cellsChain before =
      cellsChain (occurrences new)+cellsChain after := by
    simpa [cellsChain,patchCells,List.map_append,List.sum_append] using he
  rw [map_sub,boundary_listChain,boundary_listChain]
  calc
    cellsChain (occurrences new)-cellsChain (occurrences old)
        = (cellsChain (occurrences new)+cellsChain after)
          -(cellsChain (occurrences old)+cellsChain after) := by abel
    _ = (cellsChain (occurrences old)+cellsChain before)
          -(cellsChain (occurrences old)+cellsChain after) := by rw [← hv]
    _ = cellsChain before-cellsChain after := by abel

/-- The original eight-bone bridge, not a generic zero-boundary assumption. -/
theorem bridgeSix_boundary :
    boundary (listChain Generated.bridgeSixNew-listChain Generated.bridgeSixOld) =
      cellsChain Generated.bridgeSixBefore-cellsChain Generated.bridgeSixAfter := by
  exact patch_homotopy Generated.bridgeSix_partition

end Benzel
