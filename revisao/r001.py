
print('Hello, World');

# A identação é um ponto importante em python
# Caso seja quebrada o código em python gera um erro

# Multiplos valores
num1, num2 = 4, 2

if num1 > num2:
    print(f'{num1} é maior que {num2}!!!')
    print('Isso ainda pertence ao bloco de controle do if!')

# Para especificar um valor, é preciso fazer casting

x = int(1)
y = float(1)
z = str(1)

# Não existe diferenciação entre ' e ""
print(type(x), type(y), type(z))

# O nome de uma variavel não pode usar as keywords de python

meuNome = "Pedro" # Camel Case
MeuNome = "Pedro" # Pascal Case
meu_nome = "Pedro" # Snake Case

# Lista
# Isso é chamado de unpacking
frutas = ["maça", "banana", "cereja"]
b1, b2, b3 = frutas

str1 = "Bom "
str2 = 'dia '

# Concatena
print(str1 + str2)
print(str1, str2) # Mostra os dois valores