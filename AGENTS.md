# AGENTS.md

Python learning repo (Midudev course). All content is in Spanish; comments, docstrings, and identifiers use Spanish snake_case (e.g. `lista_a`, `person_1`). Keep new code in the same style.

## Commands
- Run any file as a standalone script: `python3 <file>` (e.g. `python3 03_loops/02_loop_for.py`).
- **`python` is NOT installed on this machine — always use `python3`.**
- No tests, linter, formatter, or build tooling exist. Do not invent or add any.

## Structure
- `01_basic/`, `02_flow_control/`, `03_loops/`, `04_logic/`, `05_regex/` — each holds independent teaching scripts numbered `NN_topic.py`.
- Files run top-to-bottom with module-level `print()`; many rely on `input()` and some clear the console (`system("clear")`), so running them may block on input or wipe your terminal output.
- `04_logic/NN_challenge_*.py` are coding challenges described in a module docstring; the function to implement is often not pre-sketched — read the docstring and implement from scratch.
- Exercises ship as `*_ejercicios.py` (blank stubs) paired with `*_soluciones.py`/`for_solutions.py` (worked solutions). Keep the pair in sync when adding content.
- `README.md` only documents through `04_logic`; newer topics (`05_regex`, etc.) are intentionally absent — update it only if asked.

## Repo-specific notes
- Git history (non-atomic commits, sparse messages like `logica`, `range`) is not a source of truth for structure.
- `.gitignore` excludes pyre artifacts (`.pyre`) — a leftover type-checker directory was committed once then removed; don't recreate it.
- `04_logic/.commandcode/taste/taste.md` is an empty leftover; ignore it.