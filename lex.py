import ply.lex as lex

# Tuple
reserved = {
    k: k for k in ("LOAD", "SHOW", "DESCRIBE", "TARGET", "TRAIN", "EVALUATE", "PREDICT")
}

tokens = ["VALUE", "NEWLINE"] + list(reserved.values())

# t_ignore is a string to store space & tab space
t_ignore = " \t"


# Token Rule Functions: 

# Match a comment line and ignore it through 'pass'
def t_COMMENT(t):
    r"\#.*"
    pass


def t_NEWLINE(t):
    r"\n+"
    # lexer object and lineno attribute is available through lex imported as ply.lex
    t.lexer.lineno += len(t.value)
    return t


def t_VALUE(t):
    r"[A-Za-z0-9_./\-]+"
    # token's type is extracted from reserved list else replaced with VALUE
    t.type = reserved.get(t.value.upper(), "VALUE")
    return t


def t_error(t):
    raise SyntaxError(f"Illegal character {t.value[0]!r} at line {t.lexer.lineno}")


lexer = lex.lex()

if __name__ == "__main__":
    lexer.input("LOAD data.csv")
    for token in lexer:
        print(token)
