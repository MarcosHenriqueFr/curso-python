
# Criar funções que duplicam, triplicam e quadriplicam

# def aumentar(numOriginal, qtd):
#     return numOriginal * qtd

# print(5, aumentar(5, 3))

# Função que gera funções
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador;

    return multiplicar

duplicar = criar_multiplicador(2)
sextuplicar = criar_multiplicador(6)

print(duplicar(4))
print(sextuplicar(10))