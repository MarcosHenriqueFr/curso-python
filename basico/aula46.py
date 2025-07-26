
# Listas em Python:
# Em python elas são implementadas como Arrays dinâmicas
# Colocar itens no fim não exige tanto processamento, diferente de remoções ou adições no meio dela

lista = [10, 20, 30, 40]

print(lista)
del lista[2] # Apaga indices

lista.append('abc')
lista.append(90)
lista.pop()
lista.pop(0)

print(lista)