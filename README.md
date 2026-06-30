# ML Pipeline DSL — Minimal Demo

**Overview:**

- Simple domain-specific language (DSL) built with PLY (lex + yacc) to run small pipeline commands.
- Files of interest:
  - `lex.py` — lexer (tokens and reserved keywords)
  - `parser.py` — grammar rules producing a small AST (`Program` / `Command`)
  - `main.py` — interpreter that executes commands against an in-memory `State`
  - `pipeline.dsl` — example DSL script (input for the interpreter)

**Current (minimal) DSL commands:**

- `LOAD <path>` — load CSV into memory
- `SHOW head|columns|shape` — inspect the dataset quickly
- `TARGET <column>` — set target column (stored in `State`)

**Quick run**

From the project root run:

```zsh
"/home/pesos/Btech in AI Repos/2/fourth-semester-study-repo/ppai/lab/lab-assignment-1/.venv/bin/python" main.py pipeline.dsl
```

The interpreter will:

- parse `pipeline.dsl` with the `parser` module
- build a `Program` (list of `Command` objects)
- run each command in order using `main.py` (updates `State`, prints outputs)

**Example `pipeline.dsl`**

```
LOAD data/fake_data.csv
SHOW head
TARGET Salary
```