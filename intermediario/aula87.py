
# Empacotamento e desempacotamento em dicts

a, b = 1, 2
a, b = b, a

print(f'{a=}, {b=}')

# a, b = pessoa.values()

# print(a, b)

# # Também se usa o empacotamento e desempacotamento muitas vezes em loops
# # Como:

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

pessoa_completa1 = {**pessoa, **dados_pessoa}

print(pessoa_completa1)

# Kwargs convertendo em dicionario
def mostrar_kwargs(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_kwargs(nome='Pedro', idade=12, status='Estudante')
mostrar_kwargs(**pessoa)

