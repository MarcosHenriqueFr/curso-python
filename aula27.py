# Fatiando Strings -> elas são arrays
# [inicio:fim:passo] -> o passo é o quanto que ele pula
# O comportamento padrão é mostrar o inicio e pular o fim

variavel = 'Olá Mundo'


#Indice final não é incluido
print(variavel[5])

print(variavel[4:])

# Não permite inverter -> sem usar o passo
print(variavel[-1:-5:2])

# Agora é possivel inverter
print(variavel[-1:-10:-1])
print(variavel[::-1])
print(variavel[0:len(variavel):2])

print(f'O tamanho da minha string {variavel} é {len(variavel)}')