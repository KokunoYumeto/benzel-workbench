import Benzel.IndexedTables

namespace Benzel.Generated
open Benzel.Tables

-- Original source families; J coefficient permutation has an inverse.
def threefoldSource : List DoubleFamily :=
[
  ⟨.horizontal, ⟨(-1), 0, (-2), 1, 0⟩, ⟨0, 0, 1, 1, 1⟩, ⟨0, 1, (-1)⟩, some ⟨0, 3, (-1), 0⟩⟩,
  ⟨.horizontal, ⟨(-1), 3, (-3), 1, (-1)⟩, ⟨0, 3, 0, 1, 1⟩, ⟨0, 1, (-1)⟩, some ⟨1, (-1), 0, (-4)⟩⟩,
  ⟨.horizontal, ⟨0, 2, (-2), 1, (-4)⟩, ⟨1, 2, 1, 1, (-2)⟩, ⟨0, 1, (-1)⟩, some ⟨0, 0, 0, 2⟩⟩,
  ⟨.horizontal, ⟨(-1), (-2), 1, 0, 2⟩, ⟨0, 1, 1, 0, 0⟩, ⟨0, 2, 1⟩, none⟩,
  ⟨.horizontal, ⟨(-1), 0, 1, 0, 2⟩, ⟨0, 3, 1, 0, 1⟩, ⟨1, 0, (-2)⟩, none⟩,
  ⟨.horizontal, ⟨(-1), (-2), (-2), 1, 0⟩, ⟨0, 1, 1, 1, 1⟩, ⟨0, 1, (-1)⟩, some ⟨0, 1, (-1), 0⟩⟩
]

-- Original corner families; J coefficient permutation has an inverse.
def threefoldCorner : List DoubleFamily :=
[
  ⟨.horizontal, ⟨0, 0, 3, 0, 2⟩, ⟨0, 0, 0, 0, 2⟩, ⟨0, 1, (-1)⟩, none⟩,
  ⟨.horizontal, ⟨0, 0, 1, 3, 3⟩, ⟨0, 0, 1, 0, 3⟩, ⟨0, 1, (-2)⟩, some ⟨0, 1, (-1), (-2)⟩⟩,
  ⟨.horizontal, ⟨0, 0, 2, 3, 3⟩, ⟨0, 0, (-1), 0, 1⟩, ⟨0, 1, (-1)⟩, some ⟨0, 1, (-1), (-1)⟩⟩,
  ⟨.diagonal, ⟨0, (-1), 3, 0, 1⟩, ⟨0, (-1), (-3), 0, 4⟩, ⟨0, 1, 0⟩, none⟩,
  ⟨.diagonal, ⟨0, 0, (-1), 3, 1⟩, ⟨0, 0, (-1), (-3), 1⟩, ⟨0, 1, (-1)⟩, some ⟨0, 0, 1, 1⟩⟩,
  ⟨.diagonal, ⟨0, 0, (-1), 3, 1⟩, ⟨0, 0, (-1), (-3), 2⟩, ⟨0, 1, (-1)⟩, some ⟨0, 0, 1, 1⟩⟩,
  ⟨.vertical, ⟨0, (-2), 1, 0, 1⟩, ⟨0, 1, (-2), 3, 0⟩, ⟨0, 1, 0⟩, some ⟨0, 1, 0, 0⟩⟩,
  ⟨.vertical, ⟨0, (-1), 0, 0, 1⟩, ⟨0, (-1), 3, 0, 5⟩, ⟨0, 1, (-1)⟩, none⟩,
  ⟨.vertical, ⟨0, (-1), 1, 0, 2⟩, ⟨0, (-1), 1, 3, 4⟩, ⟨0, 1, (-1)⟩, some ⟨0, 1, (-1), (-1)⟩⟩,
  ⟨.vertical, ⟨0, (-1), 1, 0, 1⟩, ⟨0, (-1), (-2), 0, 0⟩, ⟨0, 1, (-1)⟩, none⟩,
  ⟨.vertical, ⟨0, 0, 2, 0, 0⟩, ⟨0, (-3), (-1), 0, 3⟩, ⟨0, 1, 0⟩, none⟩,
  ⟨.vertical, ⟨0, 0, 2, 0, 1⟩, ⟨0, (-3), (-1), 0, 2⟩, ⟨0, 1, 0⟩, none⟩,
  ⟨.vertical, ⟨0, 0, 2, 0, 4⟩, ⟨0, 0, (-4), 3, (-2)⟩, ⟨0, 1, (-2)⟩, some ⟨0, 0, 1, 1⟩⟩,
  ⟨.vertical, ⟨0, 0, 2, 0, 5⟩, ⟨0, 0, (-4), 3, (-3)⟩, ⟨0, 1, (-2)⟩, some ⟨0, 0, 1, 1⟩⟩,
  ⟨.vertical, ⟨0, 2, 0, 0, 0⟩, ⟨0, (-4), 3, 0, 6⟩, ⟨0, 1, (-1)⟩, none⟩
]

-- Original long families; J coefficient permutation has an inverse.
def threefoldLong : List DoubleFamily :=
[
  ⟨.horizontal, ⟨0, 1, 2, 1, 1⟩, ⟨(-1), 1, (-1), 1, 1⟩, ⟨0, 1, 0⟩, some ⟨1, (-3), 1, 0⟩⟩
]

-- Original deleted families; J coefficient permutation has an inverse.
def threefoldDeleted : List DoubleFamily :=
[
  ⟨.right, ⟨1, 0, (-1), 0, (-2)⟩, ⟨0, 0, (-1), 0, 0⟩, ⟨0, 1, 0⟩, none⟩
]

end Benzel.Generated
