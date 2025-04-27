
lista_de_compras = ["Pão", "Pasta de Dente", "Feijão", "Sabonete", "Amaciante"]
print(lista_de_compras)

lista_de_compras.append("Sorvete")
print(lista_de_compras)

lista_de_compras.remove("Pão")
print(lista_de_compras)

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for num in lista_num:
    if num % 2 == 0: 
        pares.append(num)

print(pares)

novas_compras = lista_de_compras[::-1]
print(novas_compras)

novas_compras_inv = []
for compra in novas_compras:
    novas_compras_inv.append(compra[::-1])

print(novas_compras_inv)