# Lab Assignment 1 — ML Pipeline DSL

## Objective

Build a **ML Pipeline DSL** — a mini-language where someone can write simple commands in a `.dsl` file, and your Python program reads, parses, and **actually executes** those commands as a real ML pipeline.

## What the code needs to do

1. **`lex.py`** — tokenize commands (recognize `LOAD`, `TRAIN`, filenames, model names, etc.)
2. **`parser.py`** — understand the grammar (e.g., `TRAIN` must be followed by a model name)
3. **`main.py`** — actually run the ML pipeline steps using `sklearn` or similar

## Plan

1. Design the DSL commands and grammar
2. Implement the lexer in `lex.py` using PLY
3. Implement the parser in `parser.py` using PLY
4. Wire up ML execution in `main.py`
5. Push to GitHub

---

# Implementation

## 1. Design Phase

The DSL covers **EDA** and a **simple ML pipeline**. Sample script:

```
# Load a dataset
LOAD data/fake_data.csv

# EDA
SHOW head
SHOW columns
SHOW shape
DESCRIBE

# ML pipeline
TARGET Salary
TRAIN LinearRegression
EVALUATE r2
PREDICT data/test.csv
```

## 2. Commands

| Command | Argument | Action |
|---------|----------|--------|
| `LOAD` | path | Read a CSV into a dataframe |
| `SHOW` | `head` / `columns` / `shape` | Print a quick look at the data |
| `DESCRIBE` | — | Summary statistics |
| `TARGET` | column | Set the column to predict |
| `TRAIN` | `LinearRegression` / `DecisionTree` | Fit a model on the data |
| `EVALUATE` | `r2` / `mae` / `rmse` | Score the trained model |
| `PREDICT` | path | Predict on a new CSV |

## 3. Grammar

```
program      -> command_list
command_list -> command | command_list command
command      -> LOAD VALUE
              | SHOW VALUE
              | DESCRIBE
              | TARGET VALUE
              | TRAIN VALUE
              | EVALUATE VALUE
              | PREDICT VALUE
```

## 4. Build Steps

1. `lex.py` — add `SHOW`, `DESCRIBE`, `TARGET` keywords to the reserved set
2. `parser.py` — grammar rules for all commands (incl. no-arg `DESCRIBE`); fix error rule
3. `main.py` — interpreter holding state (`df`, `model`, `target`); execute each command via pandas / sklearn
4. `pipeline.dsl` — sample script
5. Update `requirements.txt` (add `scikit-learn`)