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
    "program : lines"
    p[0] = Program(p[1])
