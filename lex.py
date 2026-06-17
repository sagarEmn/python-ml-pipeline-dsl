import ply.lex as lex

reserved = {k: k for k in ('LOAD', 'TRAIN', 'EVALUATE', 'PREDICT')}

tokens = [
    'VALUE', 'NEWLINE'
] + list(reserved.values())

t_ignore = ' \t'

def t_COMMENT(t):
    r'\#.*'
    pass


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t


def t_VALUE(t):
    r'[A-Za-z0-9_./\-]+'
    t.type = reserved.get(t.value.upper(), 'VALUE')
    return t


def t_error(t):
    raise SyntaxError(f"Illegal character {t.value[0]!r} at line {t.lexer.lineno}")


lexer = lex.lex()