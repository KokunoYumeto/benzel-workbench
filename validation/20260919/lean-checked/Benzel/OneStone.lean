import Benzel.Incidence
import Benzel.Parameters

namespace Benzel

/-- Literal shifted packing, s=1, for the invariant-one ray.
This is a candidate port of the audited constructor. Its full correctness
statement below is deliberately not declared as a theorem in this scaffold. -/
def oneStonePacking (d : ℕ) : List Tile := Id.run do
  let h := triangular d - 1
  let mut out := []
  for a in List.range (2*h+d) do
    let y := a+1
    let left : ℤ := if y ≤ h then
        1 - 2*(y : ℤ) - (bandIndex (y+1) : ℤ)
      else (y : ℤ) - 3*(h : ℤ) - (d : ℤ) + 1
    let n := if y ≤ h then y else min h (2*h+d-y)
    for j in List.range n do
      for p in List.range 3 do
        out := out ++ [reflectTile (rotateTileN p
          (tile .horizontal (left+3*(j : ℤ)) (y : ℤ)))]
  return out

def oneStoneCandidate (d : ℕ) : List Tile :=
  oneStonePacking d ++ [tile .right 0 0]

/-- The two original positive band tables at a transport stage r. -/
def slideOld (r : ℕ) : List Tile :=
  (List.range (triangular (r+1))).map fun j : ℕ =>
    tile .horizontal (1-(r : ℤ)^2+3*(j : ℤ)) (triangular (r+1))

def slideNew (r : ℕ) : List Tile :=
  (List.range (triangular (r+1))).map fun j : ℕ =>
    tile .horizontal (2-(r : ℤ)^2+3*(j : ℤ)) (triangular (r+1))

def startEndpoint (r : ℕ) : Cell :=
  (triangular (r+2),triangular (r+1))

def endEndpoint (r : ℕ) : Cell :=
  (1-(r : ℤ)^2,triangular (r+1))

/-- Closed target for a parameter-uniform band chain homotopy. -/
def BandSlideGoal : Prop := ∀ r : ℕ, 1 ≤ r →
  boundary (listChain (slideNew r)-listChain (slideOld r)) =
    cellVector (startEndpoint r)-cellVector (endEndpoint r)

/-- The standalone centered-one-stone target. Exact tile counts are retained. -/
def OneStoneGoal : Prop := ∀ d : ℕ, 3 ≤ d →
  let h := triangular d-1
  IsTilingList (d+3*h) (2*d+3*h) (oneStoneCandidate d) ∧
  (oneStoneCandidate d).filter (fun t => decide (t.kind = Kind.right)) = [tile .right 0 0] ∧
  ((oneStoneCandidate d).map rotateTile).Perm (oneStoneCandidate d) ∧
  boneCount (oneStoneCandidate d) = 3*h*(h+d)

end Benzel
