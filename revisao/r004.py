# Coleções em Python -> Quando for escolher um deles e importante saber suas propriedades

# Armazenam diferentes valores em uma unica variavel

lista_ex = ["elmt1", "elmt2", "elmt3", "elmt4", "elmt5"]
print(f'{len(lista_ex)} elementos', lista_ex)

# Pode conter dados de diferentes tipos

list1 = ["str", True, 123, 3j]

# Pode usar o contrutor de lista para fazer ela

essaLista = list(("Banana", "Maçã", "Melancia"))
print(essaLista)

# Isso aqui retorna uma nova lista e funciona com string tambem
print(essaLista[0:3:2])

essaLista[1] = "Maracujá"

if "Maçã" in essaLista:
    print('Esse elemento está na lista')
elif "Maracujá" not in essaLista:
    print('Não tem maracujá nessa lista')
else:
    print("A maçã não está e o maracujá está")

# Colocando um elemento onde quiser
essaLista.insert(1, "Melão")
print(essaLista)

# Colocando um elemento na ultima posição da lista
essaLista.append("Abacaxi")
print(essaLista)

# Colocando elementos de uma outra lista nessa lista, ou qualquer coleção
novaLista = ["Jabuticaba", "Jaca"]
essaLista.extend(novaLista)
print(essaLista)

# Removendo -> remove o primeiro que aparecer
essaLista.remove("Melancia")
print(essaLista)

# Removendo a partir de um index, se não especificado remove o ultimo
essaLista.pop(1)
print(essaLista)

essaLista.pop()
print(essaLista)

# Limpa a lista como um todo
essaLista.clear()
print(essaLista)