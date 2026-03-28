
# O filter

from dados import produtos

def print_iter(iter):
    print(*list(iter), sep='\n', end='\n\n')

acima_20 = [
    p
    for p in produtos
    if p['preco'] > 20
]

print_iter(acima_20)

acima_20 = filter(
    lambda x: x['preco'] > 20,
    produtos
)

print_iter(acima_20)