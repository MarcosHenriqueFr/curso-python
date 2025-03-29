# Condicionais em python

entrada = input('Você quer "entrar" ou "sair"? ')
entrada = entrada.lower()

if entrada == 'entrar':
    print('Usuário entrou no sistema!')
elif entrada == 'sair': 
    print('Usuário saiu do sistema')
else:
    print('Valor inválido de entrada!')

print('Fim do Programa')