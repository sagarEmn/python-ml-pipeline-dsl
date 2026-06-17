# Lab Assignment 1 — ML Pipeline DSL

## Objective

Build a **ML Pipeline DSL** — a mini-language where someone can write simple commands in a `.dsl` file, and your Python program reads, parses, and **actually executes** those commands as a real ML pipeline.

## Example DSL syntax

```
LOAD data/fake_data.csv
TRAIN LinearRegression
EVALUATE accuracy
PREDICT test.csv
```

## What the code needs to do

1. **`lex.py`** — tokenize commands (recognize `LOAD`, `TRAIN`, filenames, model names, etc.)
2. **`parser.py`** — understand the grammar (e.g., `TRAIN` must be followed by a model name)
3. **`main.py`** — actually run the ML pipeline steps using `sklearn` or similar

## Current project state

| File | Status |
|------|--------|
| `lex.py` | Barely started — only has `NUMBER` and `PLUS` tokens (irrelevant) |
| `parser.py` | Empty |
| `main.py` | Empty |
| `data/fake_data.csv` | Fake data with Age, Salary, Department columns — good for regression |

## Plan

1. Design the DSL commands and grammar
2. Implement the lexer in `lex.py` using PLY
3. Implement the parser in `parser.py` using PLY
4. Wire up ML execution in `main.py`
5. Push to GitHub

---

# Implementation: 

1. Design Phase: 

Our DSL should contain: 

```
LOAD data/fake_data.csv
TRAIN LinearRegression
EVALUATE accuracy
PREDICT data/test.csv
```