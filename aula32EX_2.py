
str_hour = input('Informe a hora atual(h): ')

try:
    hour = int(str_hour)
    manha = hour >= 0 and hour < 12
    tarde = hour >= 12 and hour < 18
    noite = hour >= 18 and hour < 24

    if manha:
        print('Bom dia!')
    elif tarde:
        print('Boa tarde')
    elif noite:
        print('Boa noite...')
    else:
        print('Hora inválida!!!')
except:
    print('Você não digitou um número.')