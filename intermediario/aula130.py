
# Usando JSON com Python

import json, pprint

caminho = './intermediario/texto/aula130.json'
# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }


# Json só guarda dados e não ações, então é bom tomar cuidado em conversões

# with open(caminho, 'w') as arquivo:
#     # O objeto dict/list a ser passado / o obj arquivo criado / os kwargs
#     json.dump(pessoa, arquivo, indent=2)

# Para fazer a leitura do json para dict python:
# dumps e loads é diferente de dump e load
# Quando tem o s é para manipular strings

# Sets não serializáveis para json
with open(caminho, 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)

    pprint.pprint(pessoa)