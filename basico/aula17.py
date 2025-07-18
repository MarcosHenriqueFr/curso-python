
# pass e ... -> placeholders, semelhante 

valor_idade = input('Insira uma idade: ')
idade = int(valor_idade)

if idade >= 18 and idade < 65:
    print('Voto obrigatório')
elif idade < 16:
    print('Não vota')
else:
    print('Voto opcional')