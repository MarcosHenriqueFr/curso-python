produtos = [
    dict(nome = "Sapato", preco = 300),
    dict(nome = "Notebook", preco = 2200.90), 
    dict(nome = "Sasnug", preco = 4600.25)
]

print(produtos)
preco_medio = 0.0

for prod in produtos:
    preco_medio += prod["preco"]
    print(prod["nome"], f'R${prod["preco"]}', sep=": ")

preco_medio /= len(produtos)

print(f'O preço médio é R${round(preco_medio, 2)}')