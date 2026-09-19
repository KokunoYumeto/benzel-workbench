import Benzel.OneStone

namespace Benzel

/-- Exact residue-zero target for a total, explicit constructor.
This definition states a goal; it does not assume or prove the goal. -/
def ConstructionCorrect (construct : ℕ → ℕ → List Tile) : Prop :=
  ∀ d h : ℕ, 2 ≤ d → h ≤ triangular d →
    IsTilingList (d+3*h) (2*d+3*h) (construct d h) ∧
    rightCount (construct d h) = triangular d-h ∧
    boneCount (construct d h) = 3*h*(h+d)

/-- Original unscaled Conway--Lagarias numerator. Multiplication by two retains
all integer coefficients and avoids a division convention in the statement. -/
def twiceCL (a b : ℤ) : ℤ :=
  if (a+b)%3 = 0 then 3*a^2-6*a*b+3*b^2-a-b
  else if (a+b)%3 = 1 then -a^2+4*a*b-b^2-a-b+2
  else 3*a^2-6*a*b+3*b^2+a+b-2


/-- The original area-unit Conway--Lagarias invariant, with its denominator. -/
def originalCL (a b : ℤ) : ℚ := (twiceCL a b : ℚ)/2

theorem originalCL_numerator (a b : ℤ) :
    2*originalCL a b = (twiceCL a b : ℚ) := by
  dsimp [originalCL]
  ring

/-- This is a named final target, NOT an axiom or an imported theorem. -/
def FullP7Goal : Prop := ∀ a b : ℤ,
  Admissible a b → 0 ≤ originalCL a b →
  ∃ ts : List Tile, IsTilingList a b ts

/-- Separate the exact remaining published-dependency target from our proof.
Do not create an axiom of this type. Formalize the dependency or retain the
residue-zero theorem as the completed formal scope. -/
def ResidueTwoGoal : Prop := ∀ a b : ℤ,
  Admissible a b → (a+b)%3 = 2 →
  ∃ ts : List Tile, IsTilingList a b ts

end Benzel
