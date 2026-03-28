
# Reduce - toda a lista em um só valor

from dados import produtos
from functools import reduce

def print_iter(iter):
    print(*list(iter), sep='\n', end='\n\n')

# Não vem com o python
# Usa um acumulador, SEMPRE PASSE UM VALOR INICIAL
soma_precos = reduce(
    lambda a, p: round(a + p['preco'], 2),
    produtos,
    0
)

print(soma_precos)