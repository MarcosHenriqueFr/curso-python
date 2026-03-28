pessoa = {}

# Usando chaves dinâmicas 
chave = 'nome'
pessoa[chave] = 'João Augusto'
pessoa['email'] = 'abc@gmail.com'

print(pessoa)
print(pessoa['email'])

del pessoa['email']
print(pessoa)

# Gera exception se a chave não existir

if pessoa.get('email', None) is None:
    print('Não existe')
else:
    print('Existe')

# lista = []