# Uso do try except -> try catch
# Except captura o erro

# Linguagem interpretada
#print(2)
#int('a')

ent_numero = input('Vou dobrar o numero que vc digitar: ')

# if não evita erros, o try sim
# Não é uma forma ideal de usar

try:
    numero = float(ent_numero) # Fail fast -> a primeira linha gera o erro
    print(f'O dobro de {numero} é {numero * 2:.1f}')
except:
    print('Isso não é um numero!!!')

