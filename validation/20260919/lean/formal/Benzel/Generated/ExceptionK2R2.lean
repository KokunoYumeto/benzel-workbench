import Benzel.IndexedTables

namespace Benzel.Generated
open Benzel.Tables

-- Literal source: turn10/edits-k2-r2.json
-- SHA-256: 8641a900567a06ba510a296c6a45e770f6ccffa63c59a696671c5e462cef7bc5
def exceptionK2R2 : List EditGroup :=
[
  { name := "first/channel-low", count := ⟨1, 0, (-8)⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 1, 9⟩, ⟨(-1), 0, 1, (-2)⟩⟩
],
    newTiles := [

],
    owners := [
      .common 1 ⟨0, 0, 1, 9⟩ ⟨0, 0, 0, 3⟩ "tail"
] },
  { name := "first/channel-high", count := ⟨1, 0, (-9)⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 1, 9⟩, ⟨(-1), 0, 1, 1⟩⟩
],
    newTiles := [

],
    owners := [
      .common 1 ⟨0, 0, 1, 9⟩ ⟨0, 0, 0, 2⟩ "tail"
] },
  { name := "first/channel-new", count := ⟨1, 0, (-9)⟩,
    oldTiles := [

],
    newTiles := [
      ⟨.diagonal, ⟨0, 0, 1, 8⟩, ⟨(-1), 0, 1, 1⟩⟩,
      ⟨.diagonal, ⟨0, 0, 1, 8⟩, ⟨(-1), 0, 1, 2⟩⟩
],
    owners := [

] },
  { name := "first/p0D", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 1, 4⟩, ⟨(-1), 0, 1, (-6)⟩⟩,
      ⟨.vertical, ⟨0, 0, 1, 5⟩, ⟨(-1), 0, 1, (-8)⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨0, 0, 1, 3⟩, ⟨(-1), 0, 1, (-6)⟩⟩,
      ⟨.diagonal, ⟨0, 0, 1, 3⟩, ⟨(-1), 0, 1, (-5)⟩⟩
],
    owners := [
      .common 1 ⟨0, 0, 1, 4⟩ ⟨0, 0, 0, 3⟩ "prefix",
      .common 1 ⟨0, 0, 1, 5⟩ ⟨0, 0, 0, 4⟩ "prefix"
] },
  { name := "first/p0U", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 0, 4⟩, ⟨(-1), 0, 3, (-3)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 5⟩, ⟨(-1), 0, 3, (-5)⟩⟩
],
    newTiles := [
      ⟨.vertical, ⟨0, 0, 0, 4⟩, ⟨(-1), 0, 3, (-5)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 5⟩, ⟨(-1), 0, 3, (-6)⟩⟩
],
    owners := [
      .common 1 ⟨0, 0, 0, 4⟩ ⟨0, 0, (-1), 2⟩ "prefix",
      .common 1 ⟨0, 0, 0, 5⟩ ⟨0, 0, (-1), 3⟩ "prefix"
] },
  { name := "first/p0T", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 0, 5⟩, ⟨(-1), 0, 0, (-2)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 6⟩, ⟨(-1), 0, 0, (-4)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 0, (-3)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 8⟩, ⟨(-1), 0, 0, (-2)⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨0, 0, 0, 4⟩, ⟨(-1), 0, 0, (-2)⟩⟩,
      ⟨.diagonal, ⟨0, 0, 0, 4⟩, ⟨(-1), 0, 0, (-1)⟩⟩,
      ⟨.diagonal, ⟨0, 0, 0, 5⟩, ⟨(-1), 0, 0, (-1)⟩⟩,
      ⟨.diagonal, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 0, 1⟩⟩,
      ⟨.horizontal, ⟨0, 0, 0, 5⟩, ⟨(-1), 0, 0, 0⟩⟩,
      ⟨.horizontal, ⟨0, 0, 0, 6⟩, ⟨(-1), 0, 0, (-1)⟩⟩,
      ⟨.horizontal, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 0, (-2)⟩⟩
],
    owners := [
      .common 1 ⟨0, 0, 0, 5⟩ ⟨0, 0, 0, 2⟩ "prefix",
      .common 1 ⟨0, 0, 0, 6⟩ ⟨0, 0, 0, 3⟩ "prefix",
      .common 1 ⟨0, 0, 0, 7⟩ ⟨0, 0, 0, 3⟩ "prefix",
      .common 1 ⟨0, 0, 0, 8⟩ ⟨0, 0, 0, 3⟩ "prefix"
] },
  { name := "first/p2D", count := ⟨0, 0, 2⟩,
    oldTiles := [
      ⟨.vertical, ⟨1, 0, 1, 0⟩, ⟨0, 0, 1, (-8)⟩⟩,
      ⟨.vertical, ⟨1, 0, 1, 1⟩, ⟨0, 0, 1, (-10)⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨1, 0, 1, (-1)⟩, ⟨0, 0, 1, (-8)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 1, (-1)⟩, ⟨0, 0, 1, (-7)⟩⟩
],
    owners := [
      .common 1 ⟨1, 0, 1, 0⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 1 ⟨1, 0, 1, 1⟩ ⟨0, 0, 0, 3⟩ "tail"
] },
  { name := "first/p2R", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, 3, (-3)⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 3, (-4)⟩, ⟨0, 0, 0, (-2)⟩⟩
],
    newTiles := [
      ⟨.horizontal, ⟨1, 0, 3, (-5)⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 3, (-5)⟩, ⟨0, 0, 0, (-2)⟩⟩
],
    owners := [
      .parent "corner" 6 2 ⟨0, 0, 0, 1⟩ ⟨0, 0, (-1), 1⟩,
      .parent "corner" 7 2 ⟨0, 0, (-1), 0⟩ ⟨0, 0, 0, 0⟩
] },
  { name := "direct-bridge", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, 3⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, 4⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, (-1)⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, (-6)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-8)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-5)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, 1⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-7)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, 2⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-6)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-5)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, (-5)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-2)⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-2)⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-1)⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-1)⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, 3⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, 4⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-6)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, 0⟩⟩
],
    owners := [
      .parent "corner" 6 2 ⟨0, 0, 0, 1⟩ ⟨0, 0, 0, 0⟩,
      .common 2 ⟨0, 0, 0, 3⟩ ⟨0, 0, 0, 2⟩ "prefix",
      .parent "corner" 9 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 10 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 11 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .common 2 ⟨0, 0, 0, 4⟩ ⟨0, 0, 0, 3⟩ "prefix",
      .parent "corner" 3 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .common 1 ⟨1, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩ "tail",
      .common 1 ⟨1, 0, 0, 2⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 1 ⟨1, 0, 0, 3⟩ ⟨0, 0, 0, 3⟩ "tail",
      .common 1 ⟨1, 0, 0, 3⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 1 ⟨1, 0, 0, 3⟩ ⟨0, 0, 0, 0⟩ "tail",
      .common 1 ⟨1, 0, 0, 4⟩ ⟨0, 0, 0, 3⟩ "tail",
      .common 1 ⟨1, 0, 0, 4⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 1 ⟨1, 0, 0, 4⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 1 ⟨1, 0, 0, 4⟩ ⟨0, 0, 0, 0⟩ "tail"
] },
  { name := "second/channel-low", count := ⟨1, 0, (-8)⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, (-2), (-11)⟩, ⟨0, 0, 1, 9⟩⟩
],
    newTiles := [

],
    owners := [
      .common 2 ⟨0, 0, 1, 9⟩ ⟨0, 0, 0, 2⟩ "tail"
] },
  { name := "second/channel-high", count := ⟨1, 0, (-9)⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, (-2), (-14)⟩, ⟨0, 0, 1, 9⟩⟩
],
    newTiles := [

],
    owners := [
      .common 2 ⟨0, 0, 1, 9⟩ ⟨0, 0, 0, 1⟩ "tail"
] },
  { name := "second/channel-new", count := ⟨1, 0, (-9)⟩,
    oldTiles := [

],
    newTiles := [
      ⟨.vertical, ⟨1, 0, (-2), (-11)⟩, ⟨0, 0, 1, 8⟩⟩,
      ⟨.vertical, ⟨1, 0, (-2), (-12)⟩, ⟨0, 0, 1, 8⟩⟩
],
    owners := [

] },
  { name := "second/p0D", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, (-2), (-2)⟩, ⟨0, 0, 1, 4⟩⟩,
      ⟨.horizontal, ⟨1, 0, (-2), (-1)⟩, ⟨0, 0, 1, 5⟩⟩
],
    newTiles := [
      ⟨.vertical, ⟨1, 0, (-2), 1⟩, ⟨0, 0, 1, 3⟩⟩,
      ⟨.vertical, ⟨1, 0, (-2), 0⟩, ⟨0, 0, 1, 3⟩⟩
],
    owners := [
      .common 2 ⟨0, 0, 1, 4⟩ ⟨0, 0, 0, 2⟩ "prefix",
      .common 2 ⟨0, 0, 1, 5⟩ ⟨0, 0, 0, 3⟩ "prefix"
] },
  { name := "second/p0U", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, (-3), (-5)⟩, ⟨0, 0, 0, 4⟩⟩,
      ⟨.horizontal, ⟨1, 0, (-3), (-4)⟩, ⟨0, 0, 0, 5⟩⟩
],
    newTiles := [
      ⟨.horizontal, ⟨1, 0, (-3), (-3)⟩, ⟨0, 0, 0, 4⟩⟩,
      ⟨.horizontal, ⟨1, 0, (-3), (-3)⟩, ⟨0, 0, 0, 5⟩⟩
],
    owners := [
      .common 2 ⟨0, 0, 0, 4⟩ ⟨0, 0, (-1), 1⟩ "prefix",
      .common 2 ⟨0, 0, 0, 5⟩ ⟨0, 0, (-1), 2⟩ "prefix"
] },
  { name := "second/p0T", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, 0, (-7)⟩, ⟨0, 0, 0, 5⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-6)⟩, ⟨0, 0, 0, 6⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-8)⟩, ⟨0, 0, 0, 7⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-10)⟩, ⟨0, 0, 0, 8⟩⟩
],
    newTiles := [
      ⟨.vertical, ⟨1, 0, 0, (-4)⟩, ⟨0, 0, 0, 4⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, (-5)⟩, ⟨0, 0, 0, 4⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, (-6)⟩, ⟨0, 0, 0, 5⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, (-10)⟩, ⟨0, 0, 0, 7⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, (-9)⟩, ⟨0, 0, 0, 7⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, (-9)⟩, ⟨0, 0, 0, 8⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, (-9)⟩, ⟨0, 0, 0, 9⟩⟩
],
    owners := [
      .common 2 ⟨0, 0, 0, 5⟩ ⟨0, 0, 0, 1⟩ "prefix",
      .common 2 ⟨0, 0, 0, 6⟩ ⟨0, 0, 0, 2⟩ "prefix",
      .common 2 ⟨0, 0, 0, 7⟩ ⟨0, 0, 0, 2⟩ "prefix",
      .common 2 ⟨0, 0, 0, 8⟩ ⟨0, 0, 0, 2⟩ "prefix"
] },
  { name := "second/p2D", count := ⟨0, 0, 2⟩,
    oldTiles := [
      ⟨.horizontal, ⟨(-1), 0, (-2), 4⟩, ⟨1, 0, 1, 0⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, (-2), 5⟩, ⟨1, 0, 1, 1⟩⟩
],
    newTiles := [
      ⟨.vertical, ⟨(-1), 0, (-2), 7⟩, ⟨1, 0, 1, (-1)⟩⟩,
      ⟨.vertical, ⟨(-1), 0, (-2), 6⟩, ⟨1, 0, 1, (-1)⟩⟩
],
    owners := [
      .common 2 ⟨1, 0, 1, 0⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 2 ⟨1, 0, 1, 1⟩ ⟨0, 0, 0, 2⟩ "tail"
] },
  { name := "second/p2R", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.diagonal, ⟨(-1), 0, (-3), 2⟩, ⟨1, 0, 3, (-1)⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, (-3), 2⟩, ⟨1, 0, 3, (-2)⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨(-1), 0, (-3), 4⟩, ⟨1, 0, 3, (-3)⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, (-3), 3⟩, ⟨1, 0, 3, (-3)⟩⟩
],
    owners := [
      .parent "corner" 6 1 ⟨0, 0, 0, 1⟩ ⟨0, 0, (-1), 1⟩,
      .parent "corner" 7 1 ⟨0, 0, (-1), 0⟩ ⟨0, 0, 0, 0⟩
] },
  { name := "small-terminal", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.diagonal, ⟨(-1), 0, 0, (-1)⟩, ⟨1, 0, 0, 2⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-3)⟩, ⟨1, 0, 0, 3⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-4)⟩, ⟨1, 0, 0, 3⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-5)⟩, ⟨1, 0, 0, 3⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-1)⟩, ⟨1, 0, 0, (-1)⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, 0⟩, ⟨1, 0, 0, 2⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, 1⟩, ⟨1, 0, 0, 3⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-2)⟩, ⟨1, 0, 0, 3⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-1)⟩, ⟨1, 0, 0, 4⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-4)⟩, ⟨1, 0, 0, 4⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-7)⟩, ⟨1, 0, 0, 4⟩⟩
],
    newTiles := [
      ⟨.vertical, ⟨(-1), 0, 0, 3⟩, ⟨1, 0, 0, 1⟩⟩,
      ⟨.vertical, ⟨(-1), 0, 0, 2⟩, ⟨1, 0, 0, 1⟩⟩,
      ⟨.vertical, ⟨(-1), 0, 0, 0⟩, ⟨1, 0, 0, 1⟩⟩,
      ⟨.vertical, ⟨(-1), 0, 0, (-1)⟩, ⟨1, 0, 0, 1⟩⟩,
      ⟨.vertical, ⟨(-1), 0, 0, 1⟩, ⟨1, 0, 0, 2⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, 1⟩, ⟨1, 0, 0, 0⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, 0⟩, ⟨1, 0, 0, 0⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-2)⟩, ⟨1, 0, 0, 1⟩⟩,
      ⟨.diagonal, ⟨(-1), 0, 0, (-3)⟩, ⟨1, 0, 0, 1⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-4)⟩, ⟨1, 0, 0, 2⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-4)⟩, ⟨1, 0, 0, 3⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-7)⟩, ⟨1, 0, 0, 3⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-2)⟩, ⟨1, 0, 0, 4⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-5)⟩, ⟨1, 0, 0, 4⟩⟩,
      ⟨.horizontal, ⟨(-1), 0, 0, (-8)⟩, ⟨1, 0, 0, 4⟩⟩
],
    owners := [
      .parent "corner" 6 1 ⟨0, 0, 0, 1⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 9 1 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 10 1 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 11 1 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 3 1 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .common 2 ⟨1, 0, 0, 2⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 2 ⟨1, 0, 0, 3⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 2 ⟨1, 0, 0, 3⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 2 ⟨1, 0, 0, 4⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 2 ⟨1, 0, 0, 4⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 2 ⟨1, 0, 0, 4⟩ ⟨0, 0, 0, 0⟩ "tail"
] }
]

end Benzel.Generated
