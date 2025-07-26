
str_num = input('Digite um número inteiro: ')

try:
    num_int = int(str_num)
    if num_int % 2 == 0:
        print('É um número par!!')
    else:
        print('É um número impar')
except:
    print('Não é um número inteiro!!!')