
# # Sets são bons para remover valores duplicados
# # Podem ser feitos dessas formas

# # s1 = set() // Mande somente outros conjuntos de dados aqui dentro
# # s2 = {1, 2} // Cuidado para não confundir com dicionários, eles não tem chave e valor

# # Valores mutáveis não podem entrar em sets, como listas/sets
# setos = {'Maria', 'Luiz', 1, 2, 3}

# # NÃO EXISTE GARANTIA DE ORDEM
# print(f'O 3 está no set? {4 in setos}')

# setos.add(25)
# setos.update(('Bom dia', 3, 3, 6, 7, 8)) # iteráveis imutáveis

# print(setos)

# # setos.clear() // Limpa o set

# # Descarte por valor e não por indice
# setos.discard('Bom dia')
# print(setos)

# # Operadores:

conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
uniao = conjunto1 | conjunto2
intersecao = conjunto1 & conjunto2
left_join = conjunto1 - conjunto2
dif_simetrica = conjunto1 ^ conjunto2

print(conjunto1, conjunto2)
print(f'{uniao=}')
print(f'{intersecao=}')
print(f'{left_join=}')
print(f'{dif_simetrica=}')