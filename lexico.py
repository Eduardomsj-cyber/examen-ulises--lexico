import re

TOKEN_SPEC = [
    ('PALABRA_CLAVE', r'\bdef\b|\breturn\b'),
    ('IDENTIFICADOR', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('NUMERO', r'\b\d+\b'),
    ('OPERADOR', r'[+\-*/=]'),
    ('DELIMITADOR', r'[(),:]'),
    ('COMENTARIO', r'#.*'),
    ('ESPACIO', r'[ \t\n]+'),
    ('ERROR', r'.'),  # Cualquier otro símbolo
]

def tokenize(code):
    tokens = []
    regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)
    for match in re.finditer(regex, code):
        tipo = match.lastgroup
        valor = match.group()
        if tipo == 'ESPACIO':
            continue
        elif tipo == 'ERROR':
            raise SyntaxError(f"🚨 Error léxico pupu: carácter no válido '{valor}'")
        tokens.append((tipo, valor))
    return tokens

# error aqui esta
codigo = "a + $b"

try:
    resultado = tokenize(codigo)
    print("Tokens generados:")
    for token in resultado:
        print(token)
except SyntaxError as e:
    print(e)
