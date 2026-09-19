import Mathlib

namespace Benzel.Certificate
open scoped BigOperators

/-- Constant terms use the last coordinate of x, fixed to 1 in generated goals. -/
def dot {n : ℕ} (a x : Fin n → ℚ) : ℚ := ∑ j, a j*x j

def combination {r n : ℕ} (weights : Fin r → ℚ)
    (rows : Fin r → Fin n → ℚ) : Fin n → ℚ :=
  fun j => ∑ i, weights i*rows i j

theorem dot_combination {r n : ℕ} (weights : Fin r → ℚ)
    (rows : Fin r → Fin n → ℚ) (x : Fin n → ℚ) :
    dot (combination weights rows) x = ∑ i, weights i*dot (rows i) x := by
  simp only [dot,combination,Finset.sum_mul,Finset.mul_sum,mul_assoc]
  exact Finset.sum_comm

/-- The verifier checks an exact nonnegative rational linear combination.
The hypothesis `hidentity` is the displayed finite coefficient equality, to be
proved by ordinary kernel reduction on each imported certificate. It is not
an assumption of the final benzel theorem. -/
theorem combination_nonnegative {r n : ℕ} (weights : Fin r → ℚ)
    (rows : Fin r → Fin n → ℚ) (target x : Fin n → ℚ)
    (hidentity : combination weights rows = target)
    (hw : ∀ i, 0 ≤ weights i) (hr : ∀ i, 0 ≤ dot (rows i) x) :
    0 ≤ dot target x := by
  rw [← hidentity,dot_combination]
  exact Finset.sum_nonneg (fun i _ => mul_nonneg (hw i) (hr i))

end Benzel.Certificate
