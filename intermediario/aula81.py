
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for item in perguntas:
    print(item.get('Pergunta'))

    i = 0
    for opcao in item['Opções']:
        print(f'{item["Opções"].index(opcao)}) {opcao}')
        i += 1
    
    try :
        escolha = int(input('Escolha uma opção: '))
    except :
        escolha = -1

    if item['Opções'][escolha] == item['Resposta']:
        acertos += 1 
        print('Acertou 🤙')
    else:
        print('Errou 🫷')

print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')