
produtos = [
    {'nome':'Calça', 'preco': 40},
    {'nome':'Camiseta', 'preco':20},
    {'nome':'Sapato', 'preco':15}
]

# novos_produtos = [{**produto} for produto in produtos]
# novos_produtos1 = [produto['nome'] for produto in produtos]

# print(*novos_produtos, sep='\n')
# print()
# print(*novos_produtos1, sep='\n')

# Uso de if ternário + list comprehension
novos_produtos = [
    {**produto, 'preco':produto['preco'] * 1.1 } 
    if produto['preco'] >= 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')