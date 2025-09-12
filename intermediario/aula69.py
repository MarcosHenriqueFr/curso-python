# A mesma lógica de empacotamento e desempacotamento
# Argumentos não-nomeados variáveis
# Uma tupla dentro de outra

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    
    return total

resultado = soma(1, 2, 3, 4, 5, 6, 7)

print(resultado)

# O sum já existe
# Sempre lembrar do * para empacotar e desempacotar

print(sum((1, 2, 3, 4, 5)))
numeros = 1, 2, 3, 4

print(sum(numeros))
print(soma(*numeros))