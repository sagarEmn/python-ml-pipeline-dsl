import ply.yacc as yacc
from lex import tokens, lexer
from dataclasses import dataclass


@dataclass
class Program:
    statements: list


@dataclass
class Command:
    name: str
    arg: str | None = None


def p_program(p):
    "program : lines"
    p[0] = Program(p[1])


def p_lines_single(p):
    "lines: line"
    if p[1] is None:
        p[0] = []
    else:
        p[0] = [p[1]]


def p_lines_multi(p):
    "lines : lines line"
    if p[2] is not None:
        p[1].append(p[2])
    p[0] = p[1]


def p_line_command_newline(p):
    "line : command NEWLINE"
    p[0] = p[1]


def p_line_blank(p):
    "line : NEWLINE"
    p[0] = None

