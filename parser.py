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


# CFG Functions:


# PLY passes an object p into p_* function automatically
def p_program(p):
    "program : lines"
    print("BEFORE p_program:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])

    p[0] = Program(p[1])

    print("AFTER p_program:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])


def p_lines_single(p):
    "lines : line"
    print("BEFORE p_lines_single:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])

    if p[1] is None:
        p[0] = []
    else:
        p[0] = [p[1]]

    print("AFTER p_lines_single:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])


def p_lines_multi(p):
    "lines : lines line"
    print("BEFORE p_lines_multi:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])
    print("p[2]:", p[2])

    if p[2] is not None:
        p[1].append(p[2])
    p[0] = p[1]

    print("AFTER p_lines_multi:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])
    print("p[2]:", p[2])


def p_line_command_newline(p):
    "line : command NEWLINE"
    print("BEFORE p_line_command_newline:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])
    print("p[2]:", p[2])

    p[0] = p[1]

    print("AFTER p_line_command_newline:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])
    print("p[2]:", p[2])


def p_line_blank(p):
    "line : NEWLINE"
    print("BEFORE p_line_blank:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])

    p[0] = None

    print("AFTER p_line_blank:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])


# Grammar Rule for each commands:


def p_command_load(p):
    "command : LOAD VALUE"
    print("BEFORE p_command_load:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])
    print("p[2]:", p[2])

    p[0] = Command("LOAD", p[2])

    print("AFTER p_command_load:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])
    print("p[2]:", p[2])


def p_command_show(p):
    "command : SHOW VALUE"
    print("BEFORE p_command_show:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])
    print("p[2]:", p[2])

    p[0] = Command("SHOW", p[2])

    print("AFTER p_command_show:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])
    print("p[2]:", p[2])


def p_command_target(p):
    "command : TARGET VALUE"
    print("BEFORE p_command_target:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])
    print("p[2]:", p[2])

    p[0] = Command("TARGET", p[2])

    print("AFTER p_command_target:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])
    print("p[2]:", p[2])


def p_command_describe(p):
    "command : DESCRIBE"
    print("BEFORE p_command_describe:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])

    p[0] = Command("DESCRIBE")

    print("AFTER p_command_describe:")
    print("p[0]:", p[0])
    print("p[1]:", p[1])


# p_error is for missing command values


def p_error(p):
    if p is None:
        raise SyntaxError("Syntax error at EOF")
    raise SyntaxError(f"Syntax error at {p.value!r} on line {p.lineno}")


parser = yacc.yacc()


if __name__ == "__main__":
    print("Hello there, you're running the file directly")
