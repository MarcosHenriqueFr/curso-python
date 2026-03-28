
# Combinação, permutação e produto

from itertools import combinations, permutations, product

def print_iter(iter):
    print(*list(iter), sep='\n', end='\n\n')

pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g', 'x'],
    ['maculino', 'feminino', 'unissex'],
    ['algodão', 'poliester']
]

# Bom para quando for trabalhar com iteraveis

# Não permite repetição
# print_iter(combinations(pessoas, 3))

# Permite 'repetição de valores'
# print_iter(permutations(pessoas, 2))

print_iter(product(*camisetas))