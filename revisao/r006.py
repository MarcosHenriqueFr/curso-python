
# Dicionarios funcionam com chave e valor

dicionario = {
    "marca": "Porsche",
    "modelo": "Cayenne",
    "ano": 2012, 
    "cores": ["azul", "verde", "preto"]
    # "ano": 2000 simplesmente sobrescreve
}

# São ordenados, modificaveis e não permitem duplicidade
# Podem ter um indice, podem ser alterados
print(dicionario, f'Tamanho do dict {len(dicionario)}', sep="\n")

dicionario_const = dict(nome = "Jorge", idade = "12", pais = "Brasil")
print(dicionario_const)
print(dicionario_const["nome"])
print(dicionario_const.get("idade"))

dicionario_const["trabalha"] = False
print(dicionario_const)

dicionario_const["nome"] = "Pedro Moirão"
print(dicionario_const)