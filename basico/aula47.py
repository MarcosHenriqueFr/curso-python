# Insert em listas

lista = [10, 20, 30, 40]
lista.append('Pedro')
ultimo = lista.pop()

print(lista)
print('Valor removido:', ultimo)

# O insert funciona da seguinte forma:
# insert((local a ser inserido), (valor a ser inserido))

lista.insert(1, 'Novo Valor')

ultimo_local = len(lista)
lista.insert(ultimo_local, 'Novo Valor por Último') # Melhor usar o append
print(lista)

lista.clear()
print(lista)