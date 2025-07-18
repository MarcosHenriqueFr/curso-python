# Uso das f-strings -> Strings formatadas

nome = 'Marcos'
altura = 1.81
peso = 79.2
IMC = peso / altura ** 2

# Mesmo round de c
# f-strings
linha_1 = f'{nome} tem {altura}m e pesa {peso:.2f}Kgs'
linha_2 = f'Seu imc é {IMC:.2f}'

print(linha_1)
print(linha_2)