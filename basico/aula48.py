
# Concatenação de Listas

# Não modifica os valores iniciais
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b

print('Valores originais preservados:', lista_c)

# Modifica os valores da lista a original

lista_a.extend(lista_b)
print('Lista A modificada:', lista_a)