
import random
# Gerador de cpf

nove_digitos = ''
for _ in range(0, 9):
    nove_digitos += str(random.randint(0, 9))

print(nove_digitos)

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

for indice in range(len(cpf_final)):
    if indice == 2 or indice == 5:
        print(cpf_final[indice] + '.', end='')
    elif indice == 8:
        print(cpf_final[indice] + '-', end='')
    else:
        print(cpf_final[indice], end='')
        
print()