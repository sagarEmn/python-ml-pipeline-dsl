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
