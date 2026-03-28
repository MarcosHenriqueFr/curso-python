
# Iteravel - Tem que ter todos os valores
# Iterator - Tem que entregar um valor por vez / Uma classe que tem que ter método iter e next

import sys

iteravel = ['Eu', 'sou', 'a', 'velocidade']
iterador = iteravel.__iter__()

# O for usa o iterator para fazer a passagem pelos valores
# print(next(iterador))

# Generator - Funções que saber pausar
# Não salva a lista inteira na memória, o que ajuda muito na performance
# lista = [n for n in range(1000)]
generator = (n for n in range(1000))

# print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# Da para acessar todos os itens da lista de forma escolhida, mas no generator não, só o próximo

for n in generator:
    print(n)
