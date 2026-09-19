# Benzel P7: Lean / Codex handoff

**Start with [CODEX_START_HERE.md](CODEX_START_HERE.md).**

This project targets a formalization of the already audited residual-and-repair
argument; it does not replace that argument by Sharma's staircase construction.
The smaller centered-one-stone / positive-band-slide construction is the first
formal target. The full residue-zero constructor is the second. The published
residue-two dependency is a separate, explicit final task.

## Current state

* New Lean definitions and proof scripts are supplied, but **Lean was not
  installed in the delivery runtime**. No new declaration is claimed kernel-checked.
* The full final theorem is not represented by an axiom, an unfinished proof, a
  Boolean flag, or a theorem parameter that assumes construction correctness.
  Its exact target is `Benzel.ConstructionCorrect`; the final theorem does not
  yet exist in the Lean environment.
* The generated tables were parsed back from Lean literals and compared exactly
  with the frozen originals: **87 indexed edit groups, 23 double-indexed
  families, 274 original owner records, and five constant patch partitions**.
* Normal and optimized Python handoff checks pass. They are export and finite
  mathematical controls, not Lean proof certificates. See `evidence/`.

## Contents

`formal/` contains the pinned Lake project, original geometry and incidence,
actual finite patch proof scripts, the one-stone candidate constructor, exact
specifications, coefficient-certificate infrastructure, and generated tables.

`formal/Optional/SplitZeroAdapter.lean` uses the original upstream `Window`,
`ChainMap`, induced homology, and comparison-kernel API on actual finite cell
supports. It is a separately enabled draft adapter, not a completed formalization
of the whole release diagram.

`reference/audit_snapshot/` is the entire immutable audit handback, including its
131-entry frozen proof input, original Python constructors, written proofs,
LaTeX/PDF sources, exact receipts, and separate checking programs. The embedded
manifest is checked again by the handoff tools. No source file is silently edited.

`docs/PARALLEL_CONSTRUCTION.md` gives an exact same-region comparison with the
supplied Sharma staircase and identifies the additional centered/symmetric result.
`docs/FORMALIZATION_MAP.md` maps each formal task to the original source.
`TASKS.json` gives bounded, dependency-ordered jobs for Codex.

## Run the available checks

From this directory:

```sh
python tools/generate_lean_data.py --check
python tools/check_generated_data.py
python tools/check_handoff.py
python -O tools/check_handoff.py --output evidence/handoff-checks-optimized.json
python tools/lean_check.py --stage preflight
```

These commands do not certify any Lean theorem. To compile the starter after
installing the pinned Lean toolchain:

```sh
cd formal
lake update
# The following command must print the exact SHA in lakefile.toml.
git -C .lake/packages/mathlib rev-parse HEAD
lake exe cache get
cd ..
python tools/lean_check.py --stage starter
```

Do not describe a successful starter build as a full P7 formalization. The
separate one-stone, residue-zero and global gates check the actual closed theorem
types and their transitive axiom reports. At delivery they intentionally cannot
pass: the required proof modules are absent.

## Provenance

The earlier existence claim and the older bone-quotient result retain their
attribution. The parallel construction and audit supply mathematical evidence;
this package makes no first-priority assertion. The supplied Sharma PDF is not
redistributed. The comparison uses its explicit anchor and shaving definitions,
not the truth of its claimed final theorem.

No remote repository, PR, or external agent was changed or launched by this
handoff. New files can be added as an isolated formalization directory and later
integrated by Codex.
