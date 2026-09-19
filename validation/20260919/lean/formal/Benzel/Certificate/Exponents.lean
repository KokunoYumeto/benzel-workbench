import Benzel.Geometry

namespace Benzel.Certificate

/-- Variable order: x,y,mx,my,kx,ky. All exponents remain signed integers. -/
abbrev Exponent6 := Fin 6 → ℤ

/-- The actual specialization on Laurent exponent groups. -/
def specializeExponent (m k : ℤ) : Exponent6 →+ Benzel.Cell where
  toFun e := (e 0 + m*e 2 + k*e 4, e 1 + m*e 3 + k*e 5)
  map_zero' := by simp
  map_add' a b := by
    apply Prod.ext <;> simp <;> ring

abbrev FormalLaurent := AddMonoidAlgebra ℤ Exponent6
abbrev CellLaurent := AddMonoidAlgebra ℤ Benzel.Cell

/-- Inputs are coefficient lists, not asserted equalities.
The next task must extend specializeExponent to the actual group-algebra map,
prove the sparse verifier's soundness, and relate each formula to its original
finite index set before importing a zero-coefficient certificate. -/
abbrev SparseTerms := List (Exponent6 × ℤ)

end Benzel.Certificate
