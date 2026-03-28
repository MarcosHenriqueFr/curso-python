
# Em dicionários e sets é exatamente a mesma coisa

import pprint

produto = {
    'nome': 'caneta',
    'preco': 2,
    'categoria': 'escritorio'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}

# Para sets se trabalha com um único valor
s1 = {i * 2 for i in range(10)}

pprint.pprint(dc)
pprint.pprint(s1)