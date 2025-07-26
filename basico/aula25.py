# Interpolação de strings, mesma coisa com format
# O tal do c -> Como o python
# x e X para hexadecimal
# Escolha uma das tres para formatacao: interpolacao, f-strings e format

nome = 'Luiz'
preco = 1203.3344
variavel = '%s, o preco total foi R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (150, 150)) # Conversão direta para hexadecimal