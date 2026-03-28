
# Funções recursivas - ela se chama de novo como um loop
# Tudo que se faz com funcional se faz com loop

def fatorial(n=0):

    if(n <= 1):
        return 1

    # Pode mandar da forma que for preferivel
    return n * fatorial(n - 1)

numero = int(input('Preencha um número para ser fatorial: '))

res = fatorial(n=numero)
print(res)
