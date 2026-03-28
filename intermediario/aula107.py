
# Exercícios

import pprint, copy


def mostrar_array(array, nome_array):
    print(nome_array)
    pprint.pprint(array)
    print()
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

from dados import produtos

# É melhor fazer a cópia e depois a alteração

novos_produtos = [
    {**prod, 'preco': round(prod['preco'] * 1.1, 2)}
    for prod in copy.deepcopy(produtos)
] 

mostrar_array(produtos, 'Produtos originais')
mostrar_array(novos_produtos, 'Novos produtos:')

# Para organizar os dicionários, é bom usar o atributo key=lambda

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
novos_produtos.sort(key=lambda item: item['nome'], reverse=True)
produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
mostrar_array(produtos_ordenados_por_nome, 'Produtos ordenador por nome:')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
novos_produtos.sort(key=lambda item: item['preco'])
produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
mostrar_array(produtos_ordenados_por_preco, 'Produtos ordenados por preço:')