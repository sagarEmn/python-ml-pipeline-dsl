from lex import lexer

script = open('pipeline.dsl').read()
lexer.input(script)

print('Tokens:')
for token in lexer:
    print(f'  {token.type}: {token.value!r}')

# !r takes in quotes