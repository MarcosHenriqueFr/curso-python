# Imprecisão de numeros de pontos flutuantes para a melhora da performance de calculos

import decimal

num1 = 0.1
num2 = 0.7
num3 = num1 + num2

print(num3)

# 1 metodo
print(f'{num3:.2f}')

# 2 metodo
print(round(num3, 2))

# 3 metodo (usando decimal) - Para números muito grandes
num4 = decimal.Decimal('0.1')
num5 = decimal.Decimal('0.7')
num6 = num4 + num5

print(num6)