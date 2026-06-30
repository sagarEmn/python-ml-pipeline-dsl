from lex import lexer
from parser import parse

# dsl command
dsl_command = "LOAD data/fake_data.csv\n"

print("Source:")
print(dsl_command)

print("Tokens:")
lexer.input(dsl_command)
for token in lexer:
    print(f"  {token.type}: {token.value!r}")

print("\nAST:")
print(parse(dsl_command))
