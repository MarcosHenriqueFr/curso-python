
input_nome = input('Digite o seu primeiro nome: ')
nome = ''

# Só permite o primeiro nome
for letra in input_nome:
    possui_espacos = letra == ' '
    if not possui_espacos:
        nome += letra
    else:
        break

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) < 7:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')