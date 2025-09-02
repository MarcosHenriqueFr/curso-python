# Métodos úteis em strings (str)

frase = 'Olá, bom dia senhor.'

# Split usa espaços em branco para separar
lista_palavras1 = frase.split(',') # Geralmente usado com regex ou caracteres

# É possível porque a lista é mutável
# Como trim de java
# for i, frase in enumerate(lista_palavras1):
#     lista_palavras1[i] = lista_palavras1[i].strip()

# Uma boa prática
lista_final = []
for i, frase in enumerate(lista_palavras1):
    lista_final.append(frase.strip())

print(lista_final)

# Funciona como uma string unica, join só aceita iteravel
frase_unida = '___'.join(lista_final)
print(type(frase_unida), frase_unida)