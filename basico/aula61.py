
# Validar o pprimeiro digito do CPF

# Soma dos 9 primeiros números por uma multiplicação com uma contagem regressiva começando de 10

cpf = '72573806006'
contagem_regressiva_1 = 10
soma = 0

for numero in cpf:
    numero = int(numero)
    soma += numero * contagem_regressiva_1
    
    contagem_regressiva_1-=1
    
resultado_1 = (soma * 10) % 11

primeiro_digito_verificador = 0 if resultado_1 > 9 else resultado_1

print(primeiro_digito_verificador)
    