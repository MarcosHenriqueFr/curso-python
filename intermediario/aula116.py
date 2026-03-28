
from itertools import zip_longest

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

def somador(l1, l2):
    tamanho = min(len(l1), len(l2))

    return [
        l1[i] + l2[i]
        for i in range(tamanho)
    ]

soma_com_metodo = somador(l1, l2)
soma_com_zip = list(x + y for x, y in zip(l1, l2))
soma_com_zip_maior = list(x + y for x, y in zip_longest(l1, l2, fillvalue=0))

print(f'{soma_com_metodo=}')
print(f'{soma_com_zip=}')
print(f'{soma_com_zip_maior=}')
