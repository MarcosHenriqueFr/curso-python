
# Retorno das funções

# Funções que somente executam, e funções que retornam valores

def imprimir(a):
    print(a)
    
def soma(x, y):
    return x + y

saida = imprimir('teste')
print(f'Saída é None?', saida is None)

soma1 = soma(10, 20)
soma2 = soma(30, 40)
print(soma1 + soma2)