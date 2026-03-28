
# Em relação à /: Antes - Posicional (args), Depois - Nomeado(kwargs)
# def soma(x, y, /):
#     return sum(x, y)

# Se for *, tudo tem que ser nomeado
def soma(x, y, *, c):
    return sum(x, y, c)

# print(soma(10, 2))
print(soma(10, 2, c=10))
