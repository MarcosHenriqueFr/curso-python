
# Exercício - Adiando execução de funções, o programa guarda a função semi-executada na stack
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

# Essa função está se precipitando e executando direto
# Dá para aumentar a zona de escopo dessa função
def criar_funcao(funcao, x):
    def interna(y):
        # Já que as funções criadas tem os mesmo parâmetros
        return funcao(x, y)

    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(5))