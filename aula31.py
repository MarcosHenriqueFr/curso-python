# id's flags, is, is not, none

# v1 = 'a'
# v2 = 'v'

# print(id(v1)) # Mesmo endereço de memoria, economia de memoria
# print(id(v2))

# Use as variaveis somente no escopo necessário, não use fora
# Flag -> marcar um local

condicao = False
passou = None

if condicao:
    passou = True
    print('Faça algo!')
else:
    print('Não faça algo!')

# Basicamente o passou == null -> is é específico para o none
if passou is None:
    print('Não passou no if')
else:
    print('Não passou >:)')