
pessoa = {
    'nome': 'Mario',
    'idade': 20,
    'idade': 21
}

print(pessoa.get('nome', None))
nome = pessoa.pop('idade')

print(nome) # Assim como em outras linguagens
print(pessoa)

#pop_item remove a ultima chave

# Update atualiza os itens sem modificar os já existentes
pessoa.update(sobrenome='Oliveira', idade=30)
print(pessoa)