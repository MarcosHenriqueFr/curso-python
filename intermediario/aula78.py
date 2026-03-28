# Métodos úteis em dicionarios em python

pessoa = {
    'nome': 'Mario',
    'idade': 20,
    'idade': 21
}

# Método under
print(pessoa.__len__())

# Esse é mais comum por facilidade de leitura
print(len(pessoa)) 
print(pessoa.keys())

# O python já considera as chaves

for valor in pessoa.keys():
    print(valor)

for valor in pessoa.values():
    print(valor)

# Chave e valor
print(list(pessoa.items()))
for chave, valor in pessoa.items():
    print(chave, valor)

# Para evitar erros de inexistência de chaves
pessoa.setdefault('job', None)
print(pessoa['job'])