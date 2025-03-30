
valor_nome = input('Digite o seu nome: ')
valor_idade = input('Digite a sua idade: ')

nome = valor_nome
idade = int(valor_idade)

if not nome and not idade:
    print('Os campos não foram digitados!!!')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    espacos = 0
    for letra in nome:
        if letra == ' ': espacos+=1
    
    if espacos == 0:
        print('Seu nome não contém espaços')
    else:
        print('Seu nome contém espaços')

    print(f'Seu nome possui {len(nome) - espacos} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[len(nome) - 1]}')
