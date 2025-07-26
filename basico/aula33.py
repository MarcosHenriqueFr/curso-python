
# str, int, float, bool
# São imutaveis, não posso mudar seu valor

string = "Teste" 

# Saida = TesABCe
outra_variavel = f'{string[:3]}ABC{string[4:]}'

# string[2] = 'OPA'
print(outra_variavel)
print(string.__add__(" a partir dos métodos"))