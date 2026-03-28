
def executa(funcao, *args):
    return funcao(*args)


# Lambda geralmente é para algo rápido e fácil
duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(10))
