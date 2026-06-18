import ply.yacc as yacc
from lex import tokens, lexer

def p_program(p):
    # program : command_list
    p[0] = p[1]
    
def p_commmand_list(p): 
    # command_list : command : command_list command
    if len(p) == 2:
        p[0] = [p[1]]
    else: 
        p[0] = p[1] + [p[2]]
        
def p_command(p):
    # command : LOAD VALUE NEWLINE (eg)
    p[0] = (p[1], p[2])
    
def p_person(p):
    if p: 
        raise SyntaxError(f"Syntax error at '{p.value}' line {p.lineno}")
    else: 
        raise SyntaxError("Syntax error at EOF")