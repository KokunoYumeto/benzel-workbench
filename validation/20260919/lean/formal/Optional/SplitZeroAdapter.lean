import Benzel.Incidence
import SplitZeroComplex

/-!
Optional source adapter to the byte-pinned original SplitZero library.
Run tools/fetch_splitzero.py, then use lakefile.with-splitzero.toml.
This file is NOT part of the starter's default target and has NOT been compiled.
It constructs actual finite-support windows and maps. The complete release
ComplexDiagram and positive augmented diagram remain named Codex tasks.
-/
noncomputable section
namespace Benzel.SplitAdapter
open scoped BigOperators
open SplitZero.Homology

abbrev CellAt (S : Finset Cell) := {c : Cell // c ∈ S}
abbrev BoneAt (S : Finset Cell) :=
  {t : Tile // t.kind ≠ Kind.right ∧ ∀ i : Fin 3, t.cell i ∈ S}

abbrev CellModule (S : Finset Cell) := CellAt S →₀ ℤ
abbrev BoneModule (S : Finset Cell) := BoneAt S →₀ ℤ

/-- Every coefficient refers to an original cell, with its support proof. -/
def localBoundary (S : Finset Cell) : BoneModule S →ₗ[ℤ] CellModule S :=
  Finsupp.linearCombination ℤ (fun t =>
    ∑ i : Fin 3, Finsupp.single (⟨t.val.cell i,t.property.2 i⟩ : CellAt S) 1)

/-- Genuine zero outgoing differential; the original incoming map is retained. -/
def localWindow (S : Finset Cell) : SplitZero.Homology.Window ℤ where
  Mprev := BoneModule S
  M := CellModule S
  Mnext := ↥(⊥ : Submodule ℤ (CellModule S))
  prev := localBoundary S
  next := 0
  square_zero := by simp

def cellInclusion {S T : Finset Cell} (h : S ⊆ T) : CellAt S → CellAt T :=
  fun c => ⟨c.val,h c.property⟩

def boneInclusion {S T : Finset Cell} (h : S ⊆ T) : BoneAt S → BoneAt T :=
  fun t => ⟨t.val,t.property.1,fun i => h (t.property.2 i)⟩

def cellMap {S T : Finset Cell} (h : S ⊆ T) : CellModule S →ₗ[ℤ] CellModule T :=
  Finsupp.lmapDomain ℤ ℤ (cellInclusion h)

def boneMap {S T : Finset Cell} (h : S ⊆ T) : BoneModule S →ₗ[ℤ] BoneModule T :=
  Finsupp.lmapDomain ℤ ℤ (boneInclusion h)

theorem inclusion_square {S T : Finset Cell} (h : S ⊆ T) :
    (cellMap h).comp (localBoundary S) = (localBoundary T).comp (boneMap h) := by
  apply Finsupp.lhom_ext
  intro t a
  simp [cellMap,boneMap,localBoundary,cellInclusion,boneInclusion,
    Finsupp.lmapDomain,Finsupp.mapDomain_single,map_sum,map_smul]

def inclusionChain {S T : Finset Cell} (h : S ⊆ T) :
    ChainMap (localWindow S) (localWindow T) where
  left := boneMap h
  mid := cellMap h
  right := 0
  prev_comm := inclusion_square h
  next_comm := by simp [localWindow]

/-- These use the upstream *constructed* induced map and kernel equivalence. -/
def supportHomologyMap {S T : Finset Cell} (h : S ⊆ T) :=
  (inclusionChain h).onHomology

def supportKernelEquiv {S T : Finset Cell} (h : S ⊆ T) :=
  (inclusionChain h).homologyKernelEquiv

/-- The new bottom is absence. `some ∅` retains the actual residual. -/
def releaseSupport (Z : Finset Cell) : WithBot (Finset Tile) → Finset Cell
  | none => ∅
  | some A => Z ∪ A.biUnion (fun t => t.cells.toFinset)

theorem release_empty_label (Z : Finset Cell) :
    releaseSupport Z (some ∅) = Z := by
  simp [releaseSupport]

theorem release_bottom (Z : Finset Cell) :
    releaseSupport Z none = ∅ := rfl

end Benzel.SplitAdapter
