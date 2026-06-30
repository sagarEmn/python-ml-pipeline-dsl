"""Run the ML Pipeline DSL."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

from parser import Program, parse


@dataclass
class State:
    data: pd.DataFrame | None = None
    target: str | None = None
    model: object | None = None
    features: list[str] = field(default_factory=list)
    x_test: pd.DataFrame | None = None
    y_test: pd.Series | None = None


def resolve_path(path: str) -> Path:
    candidate = Path(path) # construct a path object from the input string
    
    # if a path exists, return it
    if candidate.is_file():
        return candidate
    repo_path = Path(__file__).resolve().parent / path # otherwise resolve the path relative to main.py
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
        raise ValueError("LOAD first") # erorr to make the user load first showing the data
    if what == "head":
        print(state.data.head())
    elif what == "columns":
        print(list(state.data.columns))
    elif what == "shape":
        print(state.data.shape)
    else:
        raise ValueError("SHOW needs head, columns, or shape")


def describe(state: State) -> None:
    if state.data is None:
        raise ValueError("LOAD first")
    print(state.data.describe(include="all"))


def set_target(state: State, column: str | None) -> None:
    if state.data is None:
        raise ValueError("LOAD first")
    if not column:
        raise ValueError("TARGET needs a column name")
    state.target = column
    # for console debug purpose: 
    print(f"Target set to {column}")


def make_model(name: str):
    name = name.lower()
    if name == "linearregression":
        return LinearRegression()
    if name == "decisiontree":
        return DecisionTreeRegressor(random_state=42)
    raise ValueError(f"Unknown model {name}")


def train(state: State, model_name: str | None) -> None:
    if state.data is None or state.target is None:
        raise ValueError("LOAD and TARGET first")
    if not model_name:
        raise ValueError("TRAIN needs a model name")

    x = pd.get_dummies(state.data.drop(columns=[state.target]))
    y = state.data[state.target]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    state.model = make_model(model_name)
    state.model.fit(x_train, y_train)
    state.features = list(x.columns)
    state.x_test = x_test
    state.y_test = y_test
    print(f"Trained {model_name}")


def evaluate(state: State, metric: str | None) -> None:
    if state.model is None or state.x_test is None or state.y_test is None:
        raise ValueError("TRAIN first")
    if not metric:
        raise ValueError("EVALUATE needs a metric")

    prediction = state.model.predict(state.x_test)
    metric = metric.lower()
    if metric == "r2":
        score = r2_score(state.y_test, prediction)
    elif metric == "mae":
        score = mean_absolute_error(state.y_test, prediction)
    elif metric == "rmse":
        score = mean_squared_error(state.y_test, prediction, squared=False)
    else:
        raise ValueError("Unknown metric")
    print(f"{metric.upper()}: {score:.4f}")


def predict(state: State, path: str | None) -> None:
    if state.model is None:
        raise ValueError("TRAIN first")
    if not path:
        raise ValueError("PREDICT needs a file path")

    data = pd.read_csv(resolve_path(path))
    x = pd.get_dummies(data).reindex(columns=state.features, fill_value=0)
    print(pd.Series(state.model.predict(x), name="prediction"))


def run(program: Program) -> None:
    state = State()
    actions = {
        "LOAD": lambda arg: load(state, arg),
        "SHOW": lambda arg: show(state, arg),
        "DESCRIBE": lambda _arg: describe(state),
        "TARGET": lambda arg: set_target(state, arg),
        "TRAIN": lambda arg: train(state, arg),
        "EVALUATE": lambda arg: evaluate(state, arg),
        "PREDICT": lambda arg: predict(state, arg),
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
