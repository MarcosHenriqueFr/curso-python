
# Validar o segundo digito verificador do CPF

# O mesmo processo do primeiro + incluir o primeiro digito e mesma soma e multiplicação a partir
# de uma contagem regressiva começando de 11

cpf = '818678120'
contagem_regressiva_1 = 10
soma = 0

for numero in cpf:
    numero = int(numero)
    soma += numero * contagem_regressiva_1
    
    contagem_regressiva_1-=1
    
resultado_1 = (soma * 10) % 11

primeiro_digito_verificador = 0 if resultado_1 > 9 else resultado_1

print(primeiro_digito_verificador)

cpf += f'{primeiro_digito_verificador}'

soma = 0
contagem_regressiva_2 = 11
for numero in cpf:
    numero = int(numero)
    soma += numero * contagem_regressiva_2
    
    contagem_regressiva_2 -= 1
    
resultado_2 = (soma * 10) % 11

segundo_digito_verificador = 0 if resultado_2 > 9 else resultado_2
cpf += f'{segundo_digito_verificador}'

print('CPF completo e verificado: ')
for indice in range(len(cpf)):
    if indice == 2 or indice == 5:
        print(cpf[indice] + '.', end='')
    elif indice == 8:
        print(cpf[indice] + '-', end='')
    else:
        print(cpf[indice], end='')
        
print()