
idade = 0

while idade < 18:
    try:
        idade_input = input('Digite a sua idade: ')
        idade = int(idade_input)
        if idade < 18:
            print('Você não pode entrar')
    except: 
        print('Você não digitou uma idade.')

print('Você entrou no sistema.')
