
# map, filter e reduce

from dados import produtos
from copy import deepcopy
from functools import partial
from types import GeneratorType

def print_iter(iter):
    print(*list(iter), sep='\n', end='\n\n')

def aumentar_porcentagem(valor, perc):
    return round(valor * perc, 2)

# O partial faz o trabalho da closure/decorator
aumentar_em_dez = partial(
    aumentar_porcentagem,
    perc=1.1
)

# Com list comprehension
novos_p = [
    {**p, 'preco': aumentar_em_dez(p['preco'])}
    for p in deepcopy(produtos)
]

# Com map, usando lambda:
novos_p = map(
    lambda prod: {**prod, 'preco': aumentar_em_dez(prod['preco'])},
    deepcopy(produtos)
)

# Esse map é um iterator
print(novos_p)
print('É generator?', isinstance(novos_p, GeneratorType))
print_iter(novos_p)

# Saber o que é generator
novos_p2 = (p for p in produtos)
print(novos_p2)
print('É generator?', isinstance(novos_p2, GeneratorType))
print_iter(novos_p2)

# É BOM SE LEMBRAR QUE ITERATOR SE ESGOTA, SÓ SE CONSOME UMA VEZ
# LEMBRE-SE DE CONVERTER

print(
    list(
        map(
            lambda x: x ** 3,
            [1, 2, 3, 4]
        )
    )
)