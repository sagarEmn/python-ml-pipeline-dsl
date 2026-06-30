# The grammar rule enforcer: tokens in, abstract syntax tree out.

import ply.yacc as yacc

# tokens: yacc needs the list of token names to know the grammar's "terminals"
# lexer: we'll handle this to parser.parse() so it knows how to tokenize input.

from lex import tokens, lexer

from dataclasses import dataclass


@dataclass
class Program:
    statements: list


@dataclass
class Command:
    name: str
    arg: str | None = None


# PLY (yacc) registers p_* functions as reduction callbacks and calls them during parsing
# Although you're defining the function, PLY supplies these functions with the format: p_* as a ply function.


def p_program(p):
    "program : lines"  # docstring for this function
    p[0] = Program(p[1])


def p_lines_multi(p):
    "lines : lines line"
    if p[2] is not None:
        p[1].append(p[2])
    p[0] = p[1]


def p_lines_single(p):
    "lines : line"
    if p[1] is None:
        p[0] = []
    else:
        p[0] = [p[1]]


def p_line_command_newline(p):
    "line : command NEWLINE"
    p[0] = p[1]


def p_line_blank(p):
    "line : NEWLINE"
    p[0] = None


def p_command_load(p):
    "command : LOAD VALUE"
    p[0] = Command("LOAD", p[2])


def p_command_show(p):
    "command : SHOW VALUE"
    p[0] = Command("SHOW", p[2])


def p_command_describe(p):
    "command : DESCRIBE"
    p[0] = Command("DESCRIBE")


def p_command_target(p):
    "command : TARGET VALUE"
    p[0] = Command("TARGET", p[2])


def p_command_train(p):
    "command : TRAIN VALUE"
    p[0] = Command("TRAIN", p[2])


def p_command_evaluate(p):
    "command : EVALUATE VALUE"
    p[0] = Command("EVALUATE", p[2])


def p_command_predict(p):
    "command : PREDICT VALUE"
    p[0] = Command("PREDICT", p[2])


def p_error(p):
    if p is None:
        raise SyntaxError("Unexpected end of input")
    raise SyntaxError(
        f"Unexpected token {p.type!r} with value {p.value!r} at line {p.lineno}"
    )


parser = yacc.yacc(start="program")


def parse(text: str):
    if text and not text.endswith("\n"):
        text = text + "\n"
    lexer.input(text)
    return parser.parse(lexer=lexer)


if __name__ == "__main__":
    sample = """LOAD data/fake_data.csv\nSHOW head\nDESCRIBE\nTARGET Salary\nTRAIN LinearRegression\nEVALUATE r2\nPREDICT data/test.csv\n"""
    print(parse(sample))
