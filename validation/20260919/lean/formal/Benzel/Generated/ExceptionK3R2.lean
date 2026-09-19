import Benzel.IndexedTables

namespace Benzel.Generated
open Benzel.Tables

-- Literal source: turn10/edits-k3-r2.json
-- SHA-256: 20207862007b1fa3b35f87dc95437e8c156eee5f01b479d30795e4e6c2943548
def exceptionK3R2 : List EditGroup :=
[
  { name := "first/channel-low", count := ⟨1, 0, (-11)⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 1, 12⟩, ⟨(-1), 0, 1, (-2)⟩⟩
],
    newTiles := [

],
    owners := [
      .common 1 ⟨0, 0, 1, 12⟩ ⟨0, 0, 0, 4⟩ "tail"
] },
  { name := "first/channel-high", count := ⟨1, 0, (-12)⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 1, 12⟩, ⟨(-1), 0, 1, 1⟩⟩
],
    newTiles := [

],
    owners := [
      .common 1 ⟨0, 0, 1, 12⟩ ⟨0, 0, 0, 3⟩ "tail"
] },
  { name := "first/channel-new", count := ⟨1, 0, (-12)⟩,
    oldTiles := [

],
    newTiles := [
      ⟨.diagonal, ⟨0, 0, 1, 11⟩, ⟨(-1), 0, 1, 1⟩⟩,
      ⟨.diagonal, ⟨0, 0, 1, 11⟩, ⟨(-1), 0, 1, 2⟩⟩
],
    owners := [

] },
  { name := "first/p0D", count := ⟨0, 0, 2⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 1, 6⟩, ⟨(-1), 0, 1, (-10)⟩⟩,
      ⟨.vertical, ⟨0, 0, 1, 7⟩, ⟨(-1), 0, 1, (-12)⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨0, 0, 1, 5⟩, ⟨(-1), 0, 1, (-10)⟩⟩,
      ⟨.diagonal, ⟨0, 0, 1, 5⟩, ⟨(-1), 0, 1, (-9)⟩⟩
],
    owners := [
      .common 1 ⟨0, 0, 1, 6⟩ ⟨0, 0, 0, 5⟩ "prefix",
      .common 1 ⟨0, 0, 1, 7⟩ ⟨0, 0, 0, 6⟩ "prefix"
] },
  { name := "first/p0U", count := ⟨0, 0, 2⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 3, (-6)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 8⟩, ⟨(-1), 0, 3, (-8)⟩⟩
],
    newTiles := [
      ⟨.vertical, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 3, (-8)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 8⟩, ⟨(-1), 0, 3, (-9)⟩⟩
],
    owners := [
      .common 1 ⟨0, 0, 0, 7⟩ ⟨0, 0, (-1), 4⟩ "prefix",
      .common 1 ⟨0, 0, 0, 8⟩ ⟨0, 0, (-1), 5⟩ "prefix"
] },
  { name := "first/p0T", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 0, 8⟩, ⟨(-1), 0, 0, (-2)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 9⟩, ⟨(-1), 0, 0, (-4)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 10⟩, ⟨(-1), 0, 0, (-3)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 11⟩, ⟨(-1), 0, 0, (-2)⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 0, (-2)⟩⟩,
      ⟨.diagonal, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 0, (-1)⟩⟩,
      ⟨.diagonal, ⟨0, 0, 0, 8⟩, ⟨(-1), 0, 0, (-1)⟩⟩,
      ⟨.diagonal, ⟨0, 0, 0, 10⟩, ⟨(-1), 0, 0, 1⟩⟩,
      ⟨.horizontal, ⟨0, 0, 0, 8⟩, ⟨(-1), 0, 0, 0⟩⟩,
      ⟨.horizontal, ⟨0, 0, 0, 9⟩, ⟨(-1), 0, 0, (-1)⟩⟩,
      ⟨.horizontal, ⟨0, 0, 0, 10⟩, ⟨(-1), 0, 0, (-2)⟩⟩
],
    owners := [
      .common 1 ⟨0, 0, 0, 8⟩ ⟨0, 0, 0, 3⟩ "prefix",
      .common 1 ⟨0, 0, 0, 9⟩ ⟨0, 0, 0, 4⟩ "prefix",
      .common 1 ⟨0, 0, 0, 10⟩ ⟨0, 0, 0, 4⟩ "prefix",
      .common 1 ⟨0, 0, 0, 11⟩ ⟨0, 0, 0, 4⟩ "prefix"
] },
  { name := "first/p2D", count := ⟨0, 0, 4⟩,
    oldTiles := [
      ⟨.vertical, ⟨1, 0, 1, 0⟩, ⟨0, 0, 1, (-11)⟩⟩,
      ⟨.vertical, ⟨1, 0, 1, 1⟩, ⟨0, 0, 1, (-13)⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨1, 0, 1, (-1)⟩, ⟨0, 0, 1, (-11)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 1, (-1)⟩, ⟨0, 0, 1, (-10)⟩⟩
],
    owners := [
      .common 1 ⟨1, 0, 1, 0⟩ ⟨0, 0, 0, 3⟩ "tail",
      .common 1 ⟨1, 0, 1, 1⟩ ⟨0, 0, 0, 4⟩ "tail"
] },
  { name := "first/p2R", count := ⟨0, 0, 2⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, 3, (-4)⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 3, (-5)⟩, ⟨0, 0, 0, (-3)⟩⟩
],
    newTiles := [
      ⟨.horizontal, ⟨1, 0, 3, (-6)⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 3, (-6)⟩, ⟨0, 0, 0, (-3)⟩⟩
],
    owners := [
      .parent "corner" 6 2 ⟨0, 0, 0, 2⟩ ⟨0, 0, (-1), 2⟩,
      .parent "corner" 7 2 ⟨0, 0, (-1), 1⟩ ⟨0, 0, 0, 0⟩
] },
  { name := "direct-bridge", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, 5⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, 1⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, 2⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, 6⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-7)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 5⟩, ⟨0, 0, 0, (-9)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 5⟩, ⟨0, 0, 0, (-6)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 5⟩, ⟨0, 0, 0, 3⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, (-8)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, (-5)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, 1⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, 4⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-7)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-6)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-6)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, 5⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, 6⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 5⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 5⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 5⟩, ⟨0, 0, 0, 2⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, (-7)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, 2⟩⟩
],
    owners := [
      .parent "corner" 6 2 ⟨0, 0, 0, 2⟩ ⟨0, 0, 0, 0⟩,
      .common 2 ⟨0, 0, 0, 5⟩ ⟨0, 0, 0, 4⟩ "prefix",
      .parent "corner" 9 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 10 2 ⟨0, 0, 0, 1⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 11 2 ⟨0, 0, 0, 1⟩ ⟨0, 0, 0, 0⟩,
      .common 2 ⟨0, 0, 0, 6⟩ ⟨0, 0, 0, 5⟩ "prefix",
      .parent "corner" 9 2 ⟨0, 0, 0, 1⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 10 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 11 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 3 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .common 1 ⟨1, 0, 0, 2⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 1 ⟨1, 0, 0, 3⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 1 ⟨1, 0, 0, 4⟩ ⟨0, 0, 0, 3⟩ "tail",
      .common 1 ⟨1, 0, 0, 5⟩ ⟨0, 0, 0, 4⟩ "tail",
      .common 1 ⟨1, 0, 0, 5⟩ ⟨0, 0, 0, 3⟩ "tail",
      .common 1 ⟨1, 0, 0, 5⟩ ⟨0, 0, 0, 0⟩ "tail",
      .common 1 ⟨1, 0, 0, 6⟩ ⟨0, 0, 0, 4⟩ "tail",
      .common 1 ⟨1, 0, 0, 6⟩ ⟨0, 0, 0, 3⟩ "tail",
      .common 1 ⟨1, 0, 0, 6⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 1 ⟨1, 0, 0, 6⟩ ⟨0, 0, 0, 0⟩ "tail"
] },
  { name := "second/channel-low", count := ⟨1, 0, (-11)⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, (-2), (-14)⟩, ⟨0, 0, 1, 12⟩⟩
],
    newTiles := [

],
    owners := [
      .common 2 ⟨0, 0, 1, 12⟩ ⟨0, 0, 0, 3⟩ "tail"
] },
  { name := "second/channel-high", count := ⟨1, 0, (-12)⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, (-2), (-17)⟩, ⟨0, 0, 1, 12⟩⟩
],
    newTiles := [

],
    owners := [
      .common 2 ⟨0, 0, 1, 12⟩ ⟨0, 0, 0, 2⟩ "tail"
] },
  { name := "second/channel-new", count := ⟨1, 0, (-12)⟩,
    oldTiles := [

],
    newTiles := [
      ⟨.vertical, ⟨1, 0, (-2), (-14)⟩, ⟨0, 0, 1, 11⟩⟩,
      ⟨.vertical, ⟨1, 0, (-2), (-15)⟩, ⟨0, 0, 1, 11⟩⟩
],
    owners := [

] },
  { name := "second/p0D", count := ⟨0, 0, 2⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, (-2), 0⟩, ⟨0, 0, 1, 6⟩⟩,
      ⟨.horizontal, ⟨1, 0, (-2), 1⟩, ⟨0, 0, 1, 7⟩⟩
],
    newTiles := [
      ⟨.vertical, ⟨1, 0, (-2), 3⟩, ⟨0, 0, 1, 5⟩⟩,
      ⟨.vertical, ⟨1, 0, (-2), 2⟩, ⟨0, 0, 1, 5⟩⟩
],
    owners := [
      .common 2 ⟨0, 0, 1, 6⟩ ⟨0, 0, 0, 4⟩ "prefix",
      .common 2 ⟨0, 0, 1, 7⟩ ⟨0, 0, 0, 5⟩ "prefix"
] },
  { name := "second/p0U", count := ⟨0, 0, 2⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, (-3), (-5)⟩, ⟨0, 0, 0, 7⟩⟩,
      ⟨.horizontal, ⟨1, 0, (-3), (-4)⟩, ⟨0, 0, 0, 8⟩⟩
],
    newTiles := [
      ⟨.horizontal, ⟨1, 0, (-3), (-3)⟩, ⟨0, 0, 0, 7⟩⟩,
      ⟨.horizontal, ⟨1, 0, (-3), (-3)⟩, ⟨0, 0, 0, 8⟩⟩
],
    owners := [
      .common 2 ⟨0, 0, 0, 7⟩ ⟨0, 0, (-1), 3⟩ "prefix",
      .common 2 ⟨0, 0, 0, 8⟩ ⟨0, 0, (-1), 4⟩ "prefix"
] },
  { name := "second/p0T", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, 0, (-10)⟩, ⟨0, 0, 0, 8⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-9)⟩, ⟨0, 0, 0, 9⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-11)⟩, ⟨0, 0, 0, 10⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-13)⟩, ⟨0, 0, 0, 11⟩⟩
],
    newTiles := [
      ⟨.vertical, ⟨1, 0, 0, (-7)⟩, ⟨0, 0, 0, 7⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, (-8)⟩, ⟨0, 0, 0, 7⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, (-9)⟩, ⟨0, 0, 0, 8⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, (-13)⟩, ⟨0, 0, 0, 10⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, (-12)⟩, ⟨0, 0, 0, 10⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, (-12)⟩, ⟨0, 0, 0, 11⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, (-12)⟩, ⟨0, 0, 0, 12⟩⟩
],
    owners := [
      .common 2 ⟨0, 0, 0, 8⟩ ⟨0, 0, 0, 2⟩ "prefix",
      .common 2 ⟨0, 0, 0, 9⟩ ⟨0, 0, 0, 3⟩ "prefix",
      .common 2 ⟨0, 0, 0, 10⟩ ⟨0, 0, 0, 3⟩ "prefix",
      .common 2 ⟨0, 0, 0, 11⟩ ⟨0, 0, 0, 3⟩ "prefix"
] },
  { name := "second/p2D", count := ⟨0, 0, 4⟩,
    oldTiles := [
      ⟨.horizontal, ⟨(-1), 0, (-2), 7⟩, ⟨1, 0, 1, 0⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, (-2), 8⟩, ⟨1, 0, 1, 1⟩⟩
],
    newTiles := [
      ⟨.vertical, ⟨(-1), 0, (-2), 10⟩, ⟨1, 0, 1, (-1)⟩⟩,
      ⟨.vertical, ⟨(-1), 0, (-2), 9⟩, ⟨1, 0, 1, (-1)⟩⟩
],
    owners := [
      .common 2 ⟨1, 0, 1, 0⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 2 ⟨1, 0, 1, 1⟩ ⟨0, 0, 0, 3⟩ "tail"
] },
  { name := "second/p2R", count := ⟨0, 0, 2⟩,
    oldTiles := [
      ⟨.diagonal, ⟨(-1), 0, (-3), 4⟩, ⟨1, 0, 3, (-2)⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, (-3), 4⟩, ⟨1, 0, 3, (-3)⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨(-1), 0, (-3), 6⟩, ⟨1, 0, 3, (-4)⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, (-3), 5⟩, ⟨1, 0, 3, (-4)⟩⟩
],
    owners := [
      .parent "corner" 6 1 ⟨0, 0, 0, 2⟩ ⟨0, 0, (-1), 2⟩,
      .parent "corner" 7 1 ⟨0, 0, (-1), 1⟩ ⟨0, 0, 0, 0⟩
] },
  { name := "small-terminal", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.diagonal, ⟨(-1), 0, 0, (-2)⟩, ⟨1, 0, 0, 4⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-8)⟩, ⟨1, 0, 0, 6⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-2)⟩, ⟨1, 0, 0, 1⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-3)⟩, ⟨1, 0, 0, 2⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-5)⟩, ⟨1, 0, 0, 3⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-1)⟩, ⟨1, 0, 0, 4⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, 0⟩, ⟨1, 0, 0, 5⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-3)⟩, ⟨1, 0, 0, 5⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-2)⟩, ⟨1, 0, 0, 6⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-11)⟩, ⟨1, 0, 0, 6⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-4)⟩, ⟨1, 0, 0, 7⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-7)⟩, ⟨1, 0, 0, 7⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-10)⟩, ⟨1, 0, 0, 7⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-13)⟩, ⟨1, 0, 0, 7⟩⟩
],
    newTiles := [
      ⟨.vertical, ⟨(-1), 0, 0, 2⟩, ⟨1, 0, 0, 3⟩⟩,
      ⟨.vertical, ⟨(-1), 0, 0, 1⟩, ⟨1, 0, 0, 3⟩⟩,
      ⟨.vertical, ⟨(-1), 0, 0, 0⟩, ⟨1, 0, 0, 4⟩⟩,
      ⟨.vertical, ⟨(-1), 0, 0, (-1)⟩, ⟨1, 0, 0, 4⟩⟩,
      ⟨.vertical, ⟨(-1), 0, 0, (-2)⟩, ⟨1, 0, 0, 5⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, 0⟩, ⟨1, 0, 0, 2⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-1)⟩, ⟨1, 0, 0, 2⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-3)⟩, ⟨1, 0, 0, 3⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-4)⟩, ⟨1, 0, 0, 3⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-3)⟩, ⟨1, 0, 0, 5⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-7)⟩, ⟨1, 0, 0, 5⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-12)⟩, ⟨1, 0, 0, 7⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-13)⟩, ⟨1, 0, 0, 7⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-6)⟩, ⟨1, 0, 0, 2⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-10)⟩, ⟨1, 0, 0, 6⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-5)⟩, ⟨1, 0, 0, 7⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-8)⟩, ⟨1, 0, 0, 7⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-11)⟩, ⟨1, 0, 0, 7⟩⟩
],
    owners := [
      .parent "corner" 6 1 ⟨0, 0, 0, 2⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 11 1 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 3 1 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .common 2 ⟨1, 0, 0, 2⟩ ⟨0, 0, 0, 0⟩ "tail",
      .common 2 ⟨1, 0, 0, 3⟩ ⟨0, 0, 0, 0⟩ "tail",
      .common 2 ⟨1, 0, 0, 4⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 2 ⟨1, 0, 0, 5⟩ ⟨0, 0, 0, 3⟩ "tail",
      .common 2 ⟨1, 0, 0, 5⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 2 ⟨1, 0, 0, 6⟩ ⟨0, 0, 0, 3⟩ "tail",
      .common 2 ⟨1, 0, 0, 6⟩ ⟨0, 0, 0, 0⟩ "tail",
      .common 2 ⟨1, 0, 0, 7⟩ ⟨0, 0, 0, 3⟩ "tail",
      .common 2 ⟨1, 0, 0, 7⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 2 ⟨1, 0, 0, 7⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 2 ⟨1, 0, 0, 7⟩ ⟨0, 0, 0, 0⟩ "tail"
] }
]

end Benzel.Generated
