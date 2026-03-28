import re
from typing import NamedTuple

class Token(NamedTuple):
    type: str
    value: str

# Deadass simple token spec
TOKEN_SPEC = [
    ('STRING',   r'"[^"]*"'),            # String literals
    ('NUMBER',   r'\d+'),                 # Integer literals
    ('IDENT',    r'[a-zA-Z_]\w*'),        # Identifiers (var, func, etc)
    ('ASSIGN',   r'='),                   # Assignment
    ('SEMICOLON',r';'),                   # Statement end
    ('OPAR',     r'\('),                  # (
    ('CPAR',     r'\)'),                  # )
    ('OBRACE',   r'\{'),                  # {
    ('CBRACE',   r'\}'),                  # }
    ('COMMA',    r','),                   # ,
    ('SKIP',     r'[ \t\n]+'),            # Whitespace (yeet)
    ('MISMATCH', r'.'),                   # Anything else
]

def tokenize(code: str) -> list[Token]:
    tokens = []
    regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)
    for mo in re.finditer(regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Yo, what is "{value}" doing here? (Line vibes: ruined)')
        tokens.append(Token(kind, value))
    return tokens
