
#Geral -> {variavel:formatacao}
variavel = 'ABC'
print(f'{variavel}')

# Paddings
# variavel:(qualCaractere)(direcao)(quantidade)
# > - esquerda, < - direita, ^ - Centro
print(f'{variavel: >10}')

# Tem formas mais faceis
print(f'{10201.2873274:0=+15,.2f}')

print(f'O hexadecimal de 1500 é {1500:08X}')

# Conversion flag -> no futuro, repr, str, ask
print(f'{variavel!r}')