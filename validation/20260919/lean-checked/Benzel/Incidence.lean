import Benzel.Tiles
import Mathlib.LinearAlgebra.Finsupp.LinearCombination
import Mathlib.Tactic.Abel

noncomputable section
namespace Benzel

abbrev TileChain := Tile →₀ ℤ
abbrev CellChain := Cell →₀ ℤ

def cellVector (p : Cell) : CellChain := Finsupp.single p 1

def tileVector (t : Tile) : CellChain := (t.cells.map cellVector).sum

/-- The original tile-to-cell incidence homomorphism. -/
def boundary : TileChain →ₗ[ℤ] CellChain :=
  Finsupp.linearCombination ℤ tileVector

def listChain (ts : List Tile) : TileChain :=
  (ts.map (fun t => Finsupp.single t 1)).sum

def cellsChain (cs : List Cell) : CellChain := (cs.map cellVector).sum

def Nonnegative (n : TileChain) : Prop := ∀ t, 0 ≤ n t

/-- Exact original-cell coverage; nonnegativity prevents signed cancellation. -/
def IsTiling (a b : ℤ) (n : TileChain) : Prop :=
  Nonnegative n ∧ ∀ c, boundary n c = if InBenzel a b c then 1 else 0

def IsTilingList (a b : ℤ) (ts : List Tile) : Prop := IsTiling a b (listChain ts)

def rightCount (ts : List Tile) : ℕ :=
  (ts.filter (fun t => decide (t.kind = Kind.right))).length

def boneCount (ts : List Tile) : ℕ :=
  (ts.filter (fun t => decide (t.kind ≠ Kind.right))).length

@[simp] theorem boundary_single (t : Tile) (a : ℤ) :
    boundary (Finsupp.single t a) = a • tileVector t := by
  simp [boundary]

@[simp] theorem boundary_listChain (ts : List Tile) :
    boundary (listChain ts) = cellsChain (occurrences ts) := by
  induction ts with
  | nil => simp [listChain,cellsChain,occurrences]
  | cons t ts ih =>
      simpa [listChain,cellsChain,occurrences,tileVector,map_add] using ih

/-- A permutation of actual cell occurrences gives the original vector equality. -/
theorem cellsChain_perm {xs ys : List Cell} (h : xs.Perm ys) :
    cellsChain xs = cellsChain ys := by
  exact (h.map cellVector).sum_eq

/-- The integral augmented differential uses the specified region vector. -/
def augmented (v : CellChain) : (ℤ × TileChain) →ₗ[ℤ] CellChain where
  toFun z := boundary z.2 - z.1 • v
  map_add' x y := by
    simp [map_add,add_smul]
    abel
  map_smul' r x := by
    simp [map_smul,smul_sub,smul_smul]

@[simp] theorem charge_one_cycle (v : CellChain) (n : TileChain) :
    augmented v (1,n) = 0 ↔ boundary n = v := by
  simp [augmented,sub_eq_zero]

end Benzel
