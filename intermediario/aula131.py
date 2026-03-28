
# O python reutiliza sempre o mesmo parâmetro mutável
# Então o ideal é não usar valores padrões para parâmetros mutáveis
# def adiciona_cliente(nome, lista=[]):
#     lista.append(nome)
#     return lista

# Solução ideal
def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

clientes1 = adiciona_cliente('João')
adiciona_cliente('Maria', clientes1)

print(clientes1)

clientes2 = adiciona_cliente('Helena')
adiciona_cliente('Joana', clientes2)

print(clientes2)

print(f'Locais na memória: \nl1: {id(clientes1)}, \nl2: {id(clientes2)}')
# O python começa a apontar ambos para o mesmo objeto, caso tenha valor padrão para mutável