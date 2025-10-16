# Dict em python
# Uma estrutura chave e valor, como um Map
# São usadas as chaves
# Mutável: dict e list. Os outros tipos são imutáveis

# dessa forma escrita
pessoa = {
    'nome': 'Mario',
    'idade': 20,
    'trabalho': ['estudante', 'desempregado'],
    'endereço': {
        'rua': 10,
        'casa': 80,
        'bairro': 'Pedra'
    }
}

# Ou com argumentos nomeados

pessoa2 = dict(nome='Maria Eduarda', idade=20)

print(pessoa)
print(pessoa2)

print(pessoa['trabalho'])

for chave in pessoa:
    print(chave, pessoa[chave])