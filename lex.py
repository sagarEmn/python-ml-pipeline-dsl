import ply.lex as lex

reserved = {k: k for k in ('LOAD', 'TRAIN', 'EVALUATE', 'PREDICT')}

tokens = [
    'VALUE', 'NEWLINE'
] + list(reserved.values())

t_ignore = ' \t'