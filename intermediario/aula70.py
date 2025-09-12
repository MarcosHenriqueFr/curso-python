
def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
        
    return total

resultado = multiplicacao(1, 2, 3, 4, 5)
resultado_prova = 1 * 2 * 3 * 4 * 5

if resultado == resultado_prova:
    print('A multiplicação funcionou')
    print(f'{resultado=} é igual à {resultado_prova=}')