import re
from typing import NamedTuple

class Token(NamedTuple):
    type: str
    value: str
    line: int

# Updated spec for the new vibe
TOKEN_SPEC = [
    ('COMMENT_MULTI', r'/\*[\s\S]*?\*/'),    # Multi-line comments
    ('COMMENT_SINGLE',r'#.*'),               # Single-line comments
    ('STRING',        r'"[^"]*"'),           # Strings
    ('NUMBER',        r'\d+'),                # Numbers
    ('IDENT',         r'[a-zA-Z_]\w*'),       # Identifiers
    ('ASSIGN',        r'='),                  # =
    ('SEMICOLON',     r';'),                  # ;
    ('OPAR',          r'\('),                 # (
    ('CPAR',          r'\)'),                 # )
    ('OBRACE',        r'\{'),                 # {
    ('CBRACE',        r'\}'),                 # }
    ('COMMA',         r','),                  # ,
    ('NEWLINE',       r'\n'),                 # Track lines
    ('SKIP',          r'[ \t\r]+'),           # Spaces
    ('MISMATCH',      r'.'),                  # Error
]

def tokenize(code: str) -> list[Token]:
    tokens = []
    line_num = 1
    regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)
    for mo in re.finditer(regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NEWLINE':
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'COMMENT_SINGLE' or kind == 'COMMENT_MULTI':
            tokens.append(Token(kind, value, line_num))
            line_num += value.count('\n')
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Line {line_num}: Yo, "{value}" is killing the vibe.')
        tokens.append(Token(kind, value, line_num))
    return tokens
