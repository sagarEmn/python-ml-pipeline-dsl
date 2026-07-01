import ply.lex as lex

# Dictionary
reserved = {k: k for k in ("LOAD", "SHOW", "TARGET", "TARGET", "DESCRIBE")}

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

    # print("tokens:", tokens)

    # # print lexer:
    # print("Lexer object:", lexer)

    # # print lexer input:
    # lexer.input('show data.csv')
    # for hehe in lexer:
    #     print(hehe)

    # Test cases
    tests = [
        "LOAD data.csv",
        "TRAIN LinearRegression",
        "DESCRIBE",
        "SHOW head",
        "load data.csv",
        "# Commment this is.",
        "LOAD data/train.csv",
        "LOAD data.csv\nTRAIN LinearRegression",
        
        # error keyword @
        "LOAD @data.csv",
    ]
    for src in tests:
        # !r shows the raw source with quotes/escapes (e.g. newlines) visible
        print(f"\nINPUT: {src!r}")

        lexer.input(src)
        # a bad char raises SyntaxError from t_error; catch it so one
        # failing input doesn't abort the rest of the test run
        try:
            for token in lexer:
                print(token)
        except SyntaxError as err:
            print("LEX ERROR:", err)
