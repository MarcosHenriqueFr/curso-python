
'''
Enumerate -> Enumera itens, é um objeto que já pode ser chamado para mostrar valores
'''

lista = ['Maria', 'Paula', 'Isabella']
lista.append('Milena')

# lista_enumerada = enumerate(lista) Menos comum

# Ele consegue desempacotar dentro
# for item in enumerate(lista, start=7):
#     indice, valor = item
#     print(indice, valor)

# E também dessa forma
for indice, valor in enumerate(lista, start=1):
    print(indice, valor)