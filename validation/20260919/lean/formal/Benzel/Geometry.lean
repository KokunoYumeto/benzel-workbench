import Mathlib

/-!
Original axial and barycentric cells, not a replacement grid.
Status: proof scripts supplied; this handoff has NOT run Lean.
-/
namespace Benzel

abbrev Cell := ℤ × ℤ
abbrev BaryCell := {p : ℤ × ℤ × ℤ // p.1 + p.2.1 + p.2.2 = 1}

def toBary (c : Cell) : BaryCell :=
  ⟨(c.1, c.2, 1 - c.1 - c.2), by omega⟩

def fromBary (c : BaryCell) : Cell := (c.1.1, c.1.2.1)

@[simp] theorem from_toBary (c : Cell) : fromBary (toBary c) = c := by
  cases c
  rfl

@[simp] theorem to_fromBary (c : BaryCell) : toBary (fromBary c) = c := by
  rcases c with ⟨⟨x, y, z⟩, h⟩
  apply Subtype.ext
  apply Prod.ext
  · rfl
  · apply Prod.ext
    · rfl
    · dsimp [toBary, fromBary] at *
      omega

def axialBaryEquiv : Cell ≃ BaryCell where
  toFun := toBary
  invFun := fromBary
  left_inv := from_toBary
  right_inv := to_fromBary

def u (c : Cell) : ℤ := c.2 - c.1
def v (c : Cell) : ℤ := 1 - c.1 - 2*c.2
def w (c : Cell) : ℤ := 2*c.1 + c.2 - 1

def InBenzel (a b : ℤ) (c : Cell) : Prop :=
  1-a ≤ u c ∧ u c ≤ b-1 ∧
  1-a ≤ v c ∧ v c ≤ b-1 ∧
  1-a ≤ w c ∧ w c ≤ b-1

instance (a b : ℤ) (c : Cell) : Decidable (InBenzel a b c) :=
  inferInstanceAs (Decidable (1-a ≤ u c ∧ u c ≤ b-1 ∧
    1-a ≤ v c ∧ v c ≤ b-1 ∧ 1-a ≤ w c ∧ w c ≤ b-1))

def Admissible (a b : ℤ) : Prop :=
  2 ≤ a ∧ a ≤ 2*b ∧ 2 ≤ b ∧ b ≤ 2*a

def rotateCell (c : Cell) : Cell := (c.2, 1-c.1-c.2)
def reflectCell (c : Cell) : Cell := (c.1, 1-c.1-c.2)
def shiftCell (s c : Cell) : Cell := s+c

@[simp] theorem difference_sum (c : Cell) : u c + v c + w c = 0 := by
  dsimp [u,v,w]
  ring

@[simp] theorem rotateCell_three (c : Cell) :
    rotateCell (rotateCell (rotateCell c)) = c := by
  apply Prod.ext <;> dsimp [rotateCell] <;> ring

@[simp] theorem reflectCell_two (c : Cell) :
    reflectCell (reflectCell c) = c := by
  apply Prod.ext <;> dsimp [reflectCell] <;> ring

@[simp] theorem unshift (s c : Cell) : shiftCell (-s) (shiftCell s c) = c := by
  simp [shiftCell]

/-- The coordinate transposition, with its actual inverse, exchanges a and b. -/
theorem reflect_mem_iff (a b : ℤ) (c : Cell) :
    InBenzel b a (reflectCell c) ↔ InBenzel a b c := by
  dsimp [InBenzel,reflectCell,u,v,w]
  omega

theorem rotate_mem_iff (a b : ℤ) (c : Cell) :
    InBenzel a b (rotateCell c) ↔ InBenzel a b c := by
  dsimp [InBenzel,rotateCell,u,v,w]
  omega

end Benzel
