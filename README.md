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

**Presentation bullets** (short, speakable)

- "Goal: show how a tiny DSL can control an ML pipeline with clear separation of concerns."
- "Lexer (`lex.py`) — recognizes keywords and values."
- "Parser (`parser.py`) — grammar written as `p_*` functions; produces an AST (list of `Command`s)."
- "Runner (`main.py`) — receives AST, maintains `State`, and executes `LOAD`, `SHOW`, `TARGET`."
- "Demo: run `python main.py pipeline.dsl` and show the output (load -> show -> target confirmation)."

**Notes / next steps (optional)**

- If you want to add training again, we can reintroduce a single `TRAIN` command that takes `Model:Target` or restore `TRAIN` + `PREDICT` with minimal dependencies.
- Add a short slide deck or Jupyter notebook for a live walkthrough if you prefer.

---

If you want, I can also:

- Add a `Makefile` or small shell script for `./run-demo.sh` to simplify demo commands.
- Generate a one-slide PDF with the bullets.
