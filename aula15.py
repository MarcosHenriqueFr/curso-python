# Coletar dados -> input
# Mesma coisa em java com scanners

# var= -> me retorna o valor ja formatado
# pode usar tanto um try ou uma verificação posterior

nome = str(input('Qual o seu nome: '))
valor_idade = input('Digite a sua idade: ')

idade = int(valor_idade)
print(f'Seu nome é {nome=}')
print(f'Sua idade é {idade} anos')