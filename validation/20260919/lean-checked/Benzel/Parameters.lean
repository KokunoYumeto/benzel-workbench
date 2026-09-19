import Mathlib.Data.Nat.Sqrt
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

namespace Benzel

/-- Recursive triangular number; the next theorem proves its original closed value. -/
def triangular : ℕ → ℕ
  | 0 => 0
  | n+1 => triangular n+n

@[simp] theorem triangular_step (n : ℕ) :
    triangular (n+1) = triangular n+n := rfl

/-- No rescaling is discarded: this proves the exact integer identity. -/
theorem twice_triangular (n : ℕ) :
    2*(triangular n : ℤ) = (n : ℤ)*((n : ℤ)-1) := by
  induction n with
  | zero => norm_num [triangular]
  | succ n ih =>
      simp only [triangular,Nat.cast_add,Nat.cast_succ]
      nlinarith

/-- Same integer-square-root algorithm as the frozen Python `block`. -/
def bandIndex (n : ℕ) : ℕ :=
  let r := (Nat.sqrt (8*n+1)-1)/2
  if r*(r+1)/2 < n then r+1 else r

inductive Route where
  | triangular | fixed (q : ℕ) | threefold (k : ℕ)
  | exceptional (k r : ℕ) | first (k : ℕ) | second (k : ℕ)
  deriving DecidableEq, Repr

/-- The four fixed and four exceptional counts remain explicit. -/
def route (q : ℕ) : Route :=
  if q = 0 then .triangular
  else if q = 1 ∨ q = 2 ∨ q = 4 ∨ q = 5 then .fixed q
  else if q % 3 = 0 then .threefold (q/3)
  else if q/3 = 2 ∨ q/3 = 3 then .exceptional (q/3) (q%3)
  else if q % 3 = 1 then .first (q/3)
  else .second (q/3)

/-- A closed specification, NOT a supplied proof of the square-root inverse. -/
def BandIndexGoal : Prop := ∀ n : ℕ, 1 ≤ n →
  1 ≤ bandIndex n ∧ triangular (bandIndex n) < n ∧
  n ≤ triangular (bandIndex n+1)

/-- Closed dispatch-domain goal for the next formalization stage. -/
def RouteDomainGoal : Prop := ∀ q : ℕ,
  match route q with
  | .triangular => q = 0
  | .fixed r => q = r ∧ (r=1 ∨ r=2 ∨ r=4 ∨ r=5)
  | .threefold k => 1 ≤ k ∧ q = 3*k
  | .exceptional k r => (k=2 ∨ k=3) ∧ (r=1 ∨ r=2) ∧ q=3*k+r
  | .first k => 4 ≤ k ∧ q=3*k+1
  | .second k => 4 ≤ k ∧ q=3*k+2

/-- Exact parameter carrier maps. The admissible integer h is nonnegative. -/
def parametersToInt (p : ℕ × ℕ) : ℤ × ℤ := (p.1,p.2)
def parametersToNat (p : ℤ × ℤ) : ℕ × ℕ := (p.1.toNat,p.2.toNat)

theorem parameters_nat_roundtrip (p : ℕ × ℕ) :
    parametersToNat (parametersToInt p) = p := by
  cases p
  rfl

theorem parameters_int_roundtrip (p : ℤ × ℤ)
    (hd : 0 ≤ p.1) (hh : 0 ≤ p.2) :
    parametersToInt (parametersToNat p) = p := by
  apply Prod.ext <;> dsimp [parametersToInt,parametersToNat] <;> omega

end Benzel
