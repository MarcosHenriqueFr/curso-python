# Inverte expressões

print(not True)

senha = input('Digite uma senha: ')

if not senha:
    print('Voce nao digitou nada')
elif senha == '123':
    print('Entrou no sistema!')
else:
    print('Senha incorreta!!!')