# Operadores lógicos and, or e not
# falsy -> valores vazios
# None -> null em outras linguagens

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Digite uma senha: ')

senha_permitida = '1234' # Compare valores do mesmo tipo

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')

print(True and 0 and False)