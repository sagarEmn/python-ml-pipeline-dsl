"""Run the ML Pipeline DSL."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from parser import Program, parse


@dataclass
class State:
    data: pd.DataFrame | None = None
    target: str | None = None


def resolve_path(path: str) -> Path:
    candidate = Path(path)  # construct a path object from the input string

    # if a path exists, return it
    if candidate.is_file():
        return candidate
    repo_path = (
        Path(__file__).resolve().parent / path
    )  # otherwise resolve the path relative to main.py
    if repo_path.is_file():
        return repo_path
    raise FileNotFoundError(path)


# Store csv file in state object's data
def load(state: State, path: str | None) -> None:
    if not path:
        raise ValueError("LOAD needs a file path")
    state.data = pd.read_csv(resolve_path(path))
    print(f"Loaded {path}")


# Takes in state object
# Takes in parameters of what, such as "head", "columns", "shape"
def show(state: State, what: str | None) -> None:
    if state.data is None:
        raise ValueError(
            "LOAD first"
        )  # erorr to make the user load first showing the data
    if what == "head":
        print(state.data.head())
    elif what == "columns":
        print(list(state.data.columns))
    elif what == "shape":
        print(state.data.shape)
    else:
        raise ValueError("SHOW needs head, columns, or shape")


# takes in state param and col param
def set_target(state: State, column: str | None) -> None:

    # if data isn't loaded meaning, state object's data property is empty
    if state.data is None:
        raise ValueError("LOAD first")
    if not column:
        raise ValueError("TARGET needs a column name")
    state.target = column


# TRAIN / EVALUATE / PREDICT removed — minimal DSL supports only LOAD, SHOW, TARGET


def run(program: Program) -> None:
    state = State()
    actions = {
        "LOAD": lambda arg: load(state, arg),
        "SHOW": lambda arg: show(state, arg),
        "TARGET": lambda arg: set_target(state, arg),
    }

    for command in program.statements:
        actions[command.name](command.arg)


def main() -> None:
    # creates a command line argument parser
    argument_parser = argparse.ArgumentParser()

    # add the arguments named dsl_file
    # nargs allows the argument to be optional
    argument_parser.add_argument("dsl_file", nargs="?", default="pipeline.dsl")
    args = argument_parser.parse_args()
    script = resolve_path(args.dsl_file)
    run(parse(script.read_text()))


if __name__ == "__main__":
    main()
