
# Filter
# Vem depois do for no list comprehension

import pprint

def p(valor):
    pprint.pprint(valor)

produtos = [
    {'nome':'Calça', 'preco': 40},
    {'nome':'Camiseta', 'preco':20},
    {'nome':'Sapato', 'preco':15}
]

# Essa lógica de filter não está 100% correta
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.2}
    if produto['preco'] > 30 else {**produto}
    for produto in produtos
    if produto['preco'] >= 20 
]


p(novos_produtos)

# O filtro é um if depois do for sem else
# lista = [n for n in range(10) if n % 2 != 0]

# p(lista)
