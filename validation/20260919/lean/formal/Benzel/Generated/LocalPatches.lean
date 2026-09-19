import Benzel.Tiles

namespace Benzel.Generated

-- Source: turn10/PROOF.md: eight-bone bridge
def bridgeSixOld : List Tile :=
[
  tile .horizontal 0 4,
  tile .horizontal 0 5,
  tile .horizontal 0 6,
  tile .horizontal 1 2,
  tile .horizontal 1 3,
  tile .horizontal 1 7,
  tile .vertical 0 1,
  tile .vertical 3 4
]
def bridgeSixNew : List Tile :=
[
  tile .vertical 0 0,
  tile .vertical 0 3,
  tile .vertical 1 0,
  tile .vertical 1 3,
  tile .vertical 2 2,
  tile .vertical 2 5,
  tile .vertical 3 2,
  tile .vertical 3 5
]
def bridgeSixBefore : List Cell := [(0, 0), (1, 0), (1, 1)]
def bridgeSixAfter : List Cell := [(0, 6), (1, 6), (1, 7)]

theorem bridgeSix_partition :
    (patchCells bridgeSixOld bridgeSixBefore).Perm (patchCells bridgeSixNew bridgeSixAfter) := by
  decide

theorem bridgeSix_old_nodup : (patchCells bridgeSixOld bridgeSixBefore).Nodup := by
  decide

theorem bridgeSix_new_nodup : (patchCells bridgeSixNew bridgeSixAfter).Nodup := by
  decide

/-- Same occurrence permutation at every integer translation, no sampling. -/
theorem bridgeSix_translated (s : Cell) :
    ((patchCells bridgeSixOld bridgeSixBefore).map (shiftCell s)).Perm
    ((patchCells bridgeSixNew bridgeSixAfter).map (shiftCell s)) := by
  exact bridgeSix_partition.map (shiftCell s)

-- Source: turn10/small-q1-2.json
def terminalQ2Old : List Tile :=
[
  tile .horizontal (-1) 0,
  tile .horizontal 0 1,
  tile .horizontal 0 2,
  tile .horizontal 0 3,
  tile .vertical (-2) 1,
  tile .vertical 1 (-3),
  tile .vertical 2 (-5),
  tile .vertical 2 (-2),
  tile .vertical 3 (-4),
  tile .vertical 3 (-1),
  tile .vertical 3 2
]
def terminalQ2New : List Tile :=
[
  tile .diagonal 0 (-3),
  tile .diagonal 0 (-2),
  tile .diagonal 0 0,
  tile .diagonal 0 1,
  tile .diagonal 1 (-2),
  tile .horizontal (-3) 0,
  tile .horizontal (-3) 1,
  tile .horizontal (-2) 2,
  tile .horizontal (-2) 3,
  tile .vertical 1 1,
  tile .vertical 2 0,
  tile .vertical 2 3,
  tile .vertical 3 (-3),
  tile .vertical 3 0,
  tile .vertical 3 3
]
def terminalQ2Before : List Cell := [((-3), 0), ((-3), 1), ((-2), 0), ((-1), 1), ((-1), 2), ((-1), 3), (0, (-3)), (0, (-2)), (1, (-4)), (2, 4), (2, 5), (3, 5)]
def terminalQ2After : List Cell := []

theorem terminalQ2_partition :
    (patchCells terminalQ2Old terminalQ2Before).Perm (patchCells terminalQ2New terminalQ2After) := by
  decide

theorem terminalQ2_old_nodup : (patchCells terminalQ2Old terminalQ2Before).Nodup := by
  decide

theorem terminalQ2_new_nodup : (patchCells terminalQ2New terminalQ2After).Nodup := by
  decide

/-- Same occurrence permutation at every integer translation, no sampling. -/
theorem terminalQ2_translated (s : Cell) :
    ((patchCells terminalQ2Old terminalQ2Before).map (shiftCell s)).Perm
    ((patchCells terminalQ2New terminalQ2After).map (shiftCell s)) := by
  exact terminalQ2_partition.map (shiftCell s)

-- Source: turn10/small-direct-2.json
def directQ2Old : List Tile :=
[
  tile .horizontal (-1) 0,
  tile .horizontal (-1) 6,
  tile .horizontal 0 1,
  tile .horizontal 0 2,
  tile .horizontal 0 3,
  tile .horizontal 0 7,
  tile .vertical (-2) 1,
  tile .vertical (-1) 1,
  tile .vertical 1 (-3),
  tile .vertical 2 (-5),
  tile .vertical 2 (-2),
  tile .vertical 2 4,
  tile .vertical 3 (-4),
  tile .vertical 3 (-1),
  tile .vertical 3 2,
  tile .vertical 3 5
]
def directQ2New : List Tile :=
[
  tile .diagonal 0 (-3),
  tile .diagonal 0 (-2),
  tile .diagonal 0 0,
  tile .diagonal 0 1,
  tile .diagonal 1 (-2),
  tile .horizontal (-3) 0,
  tile .horizontal (-3) 1,
  tile .horizontal (-2) 2,
  tile .horizontal (-2) 3,
  tile .horizontal 1 6,
  tile .horizontal 1 7,
  tile .vertical 1 1,
  tile .vertical 2 0,
  tile .vertical 2 3,
  tile .vertical 3 (-3),
  tile .vertical 3 0,
  tile .vertical 3 3
]
def directQ2Before : List Cell := [((-3), 0), ((-3), 1), ((-2), 0), (0, (-3)), (0, (-2)), (1, (-4))]
def directQ2After : List Cell := [((-1), 6), (0, 6), (0, 7)]

theorem directQ2_partition :
    (patchCells directQ2Old directQ2Before).Perm (patchCells directQ2New directQ2After) := by
  decide

theorem directQ2_old_nodup : (patchCells directQ2Old directQ2Before).Nodup := by
  decide

theorem directQ2_new_nodup : (patchCells directQ2New directQ2After).Nodup := by
  decide

/-- Same occurrence permutation at every integer translation, no sampling. -/
theorem directQ2_translated (s : Cell) :
    ((patchCells directQ2Old directQ2Before).map (shiftCell s)).Perm
    ((patchCells directQ2New directQ2After).map (shiftCell s)) := by
  exact directQ2_partition.map (shiftCell s)

-- Source: turn10/small-q1-3.json
def terminalQ3Old : List Tile :=
[
  tile .horizontal (-1) 0,
  tile .horizontal 1 4,
  tile .vertical (-2) 1,
  tile .vertical (-1) 1,
  tile .vertical 0 2,
  tile .vertical 1 (-3),
  tile .vertical 2 (-5),
  tile .vertical 2 (-2),
  tile .vertical 3 (-4),
  tile .vertical 3 5,
  tile .vertical 4 (-3),
  tile .vertical 4 0,
  tile .vertical 4 3,
  tile .vertical 4 6
]
def terminalQ3New : List Tile :=
[
  tile .diagonal 0 (-3),
  tile .diagonal 0 (-2),
  tile .diagonal 1 (-2),
  tile .diagonal 1 (-1),
  tile .diagonal 2 (-1),
  tile .horizontal (-3) 0,
  tile .horizontal (-3) 1,
  tile .horizontal (-2) 2,
  tile .horizontal (-2) 3,
  tile .horizontal 0 0,
  tile .horizontal 0 4,
  tile .horizontal 2 7,
  tile .horizontal 2 8,
  tile .vertical (-1) 4,
  tile .vertical 3 4,
  tile .vertical 4 (-2),
  tile .vertical 4 1,
  tile .vertical 4 4
]
def terminalQ3Before : List Cell := [((-3), 0), ((-3), 1), ((-2), 0), ((-1), 4), ((-1), 5), ((-1), 6), (0, (-3)), (0, (-2)), (1, (-4)), (2, 7), (2, 8), (3, 8)]
def terminalQ3After : List Cell := []

theorem terminalQ3_partition :
    (patchCells terminalQ3Old terminalQ3Before).Perm (patchCells terminalQ3New terminalQ3After) := by
  decide

theorem terminalQ3_old_nodup : (patchCells terminalQ3Old terminalQ3Before).Nodup := by
  decide

theorem terminalQ3_new_nodup : (patchCells terminalQ3New terminalQ3After).Nodup := by
  decide

/-- Same occurrence permutation at every integer translation, no sampling. -/
theorem terminalQ3_translated (s : Cell) :
    ((patchCells terminalQ3Old terminalQ3Before).map (shiftCell s)).Perm
    ((patchCells terminalQ3New terminalQ3After).map (shiftCell s)) := by
  exact terminalQ3_partition.map (shiftCell s)

-- Source: turn10/small-direct-3.json
def directQ3Old : List Tile :=
[
  tile .horizontal (-1) 0,
  tile .horizontal (-1) 9,
  tile .horizontal 0 1,
  tile .horizontal 0 5,
  tile .horizontal 0 6,
  tile .horizontal 0 10,
  tile .horizontal 1 2,
  tile .horizontal 1 3,
  tile .horizontal 1 4,
  tile .vertical (-2) 1,
  tile .vertical (-1) 1,
  tile .vertical 0 2,
  tile .vertical 1 (-3),
  tile .vertical 2 (-5),
  tile .vertical 2 (-2),
  tile .vertical 2 7,
  tile .vertical 3 (-4),
  tile .vertical 3 (-1),
  tile .vertical 3 5,
  tile .vertical 3 8
]
def directQ3New : List Tile :=
[
  tile .diagonal 0 (-3),
  tile .diagonal 0 (-2),
  tile .diagonal 0 0,
  tile .diagonal 0 1,
  tile .diagonal 1 (-2),
  tile .horizontal (-3) 0,
  tile .horizontal (-3) 1,
  tile .horizontal (-2) 2,
  tile .horizontal (-2) 3,
  tile .horizontal 1 9,
  tile .horizontal 1 10,
  tile .vertical 0 4,
  tile .vertical 1 1,
  tile .vertical 1 4,
  tile .vertical 2 0,
  tile .vertical 2 3,
  tile .vertical 2 6,
  tile .vertical 3 (-3),
  tile .vertical 3 0,
  tile .vertical 3 3,
  tile .vertical 3 6
]
def directQ3Before : List Cell := [((-3), 0), ((-3), 1), ((-2), 0), (0, (-3)), (0, (-2)), (1, (-4))]
def directQ3After : List Cell := [((-1), 9), (0, 9), (0, 10)]

theorem directQ3_partition :
    (patchCells directQ3Old directQ3Before).Perm (patchCells directQ3New directQ3After) := by
  decide

theorem directQ3_old_nodup : (patchCells directQ3Old directQ3Before).Nodup := by
  decide

theorem directQ3_new_nodup : (patchCells directQ3New directQ3After).Nodup := by
  decide

/-- Same occurrence permutation at every integer translation, no sampling. -/
theorem directQ3_translated (s : Cell) :
    ((patchCells directQ3Old directQ3Before).map (shiftCell s)).Perm
    ((patchCells directQ3New directQ3After).map (shiftCell s)) := by
  exact directQ3_partition.map (shiftCell s)

end Benzel.Generated
