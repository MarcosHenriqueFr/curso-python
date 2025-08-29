
frutas = ['Banana', 'Abacaxi', 'Tomate']
# fruta1, fruta2, fruta3 = frutas
# fruta1, *resto = frutas

fruta1, *_ = frutas

# A quantidade de variáveis tem que ser igual a quantidade de valores dentro da Array
# Esse é um conceito de desempacotamento
print(fruta1)