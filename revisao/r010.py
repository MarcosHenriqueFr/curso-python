
a = [2, 3, 4, 5]

# Uma forma mais concisa de fazer uma lista a partir de outra
# Forma longa

res1 = []

for val in a:
    res1.append(val**2)

# Resultado (O que entra) / loop forEach / Condição (Se houver)
res = [val ** 2 for val in a]
res2 = [val for val in a if val % 2 == 0]

# Os quadrados
print(res)
print(res1)

coordenadas = [(x, y) for x in range(3) for y in range(3)]
print(coordenadas)