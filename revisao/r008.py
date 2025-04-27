aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia"
}

print(aluno)
print(aluno["nome"])
aluno["nota"] = 8.5

print(aluno)

frase = "teste de frase de"
palavras = frase.split(" ")
contagem_palavras = {}
palavras_adicionadas = set()

for i, palavra in enumerate(palavras):
    if palavra not in palavras_adicionadas:
        contagem_palavras[i] = palavra
        palavras_adicionadas.add(palavra)

print(contagem_palavras)

inventario = {
    "camiseta": 50,
    "calca": 30, 
    "sapato": 20 
}

print(inventario)

item = input('Digite o nome de um item: ')

if item in inventario.keys():
    print(inventario[item], item + 's')
else:
    print("Item não encontrado/inexistente")