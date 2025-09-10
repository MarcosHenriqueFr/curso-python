
# Validar o segundo digito verificador do CPF

# O mesmo processo do primeiro + incluir o primeiro digito e mesma soma e multiplicação a partir
# de uma contagem regressiva começando de 11

import re

# cpf_enviado = '630.930.380-57'.replace('.', '').replace('-', '')

entrada_usuario = input('Insira o CPF [630.930.380-57]: ')
# Mais 'imune' a erros de input do usuario
cpf_enviado = re.sub(
    r'[^0-9]',
    '',
    entrada_usuario
)

if (entrada_usuario[0] * len(entrada_usuario)) == entrada_usuario:
    print('Entrada inválida com os mesmos caracteres')

nove_digitos = cpf_enviado[:9]
contagem_regressiva_1 = 10
soma = 0

for numero in nove_digitos:
    numero = int(numero)
    soma += numero * contagem_regressiva_1
    
    contagem_regressiva_1-=1
    
resultado_1 = (soma * 10) % 11

primeiro_digito_verificador = 0 if resultado_1 > 9 else resultado_1

dez_digitos = nove_digitos + str(primeiro_digito_verificador)

soma = 0
contagem_regressiva_2 = 11
for numero in dez_digitos:
    numero = int(numero)
    soma += numero * contagem_regressiva_2
    
    contagem_regressiva_2 -= 1
    
resultado_2 = (soma * 10) % 11

segundo_digito_verificador = 0 if resultado_2 > 9 else resultado_2

cpf_final = f'{nove_digitos}{primeiro_digito_verificador}{segundo_digito_verificador}'

if cpf_enviado == cpf_final:
    print('CPF completo e verificado: ')
    for indice in range(len(cpf_final)):
        if indice == 2 or indice == 5:
            print(cpf_final[indice] + '.', end='')
        elif indice == 8:
            print(cpf_final[indice] + '-', end='')
        else:
            print(cpf_final[indice], end='')
            
    print()
else:
    print('CPF Inválido')