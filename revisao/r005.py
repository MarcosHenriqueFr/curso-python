
lista_num = [1, 4, 6, 7]

# Olha o forEach
for num in lista_num:
    print(lista_num.index(num), num)

# Olha o for não convencional
for cont in range(len(lista_num)):
    print(f'Posição {cont}: valor={lista_num[cont]}')

# Shorthand para loopar e printar
[print(num, end=" ") for num in lista_num]

print()
nome = str("")

while len(nome) == 0:
    nome = input('Digite o seu nome: ')


print(f'\nFim do programa {nome}')

