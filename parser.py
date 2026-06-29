# The grammar rule enforcer: tokens in, abstract syntax tree out. 

import ply.yacc as yacc

# tokens: yacc needs the list of token names to know the grammar's "terminals"
# lexer: we'll handle this to parser.parse() so it knows how to tokenize input. 

from lex import tokens, lexer

from dataclasses import dataclass

@dataclass
class Program: 
    statements: list

