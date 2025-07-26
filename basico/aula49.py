
# As listas apontam para o mesmo valor na memória se somente assimilar elas
# Assim como em grande parte das linguagens de programação

lista_a = ['Luiz', 'Pedro', 1.8, 9, False]
lista_b = lista_a
lista_c = lista_a.copy()

lista_a[0] = 'Outro Valor'

print('Apontam para o mesmo.', f'{lista_b=}')
print('Somente uma cópia.', f'{lista_c=}')