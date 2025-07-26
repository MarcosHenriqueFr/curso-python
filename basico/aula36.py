
qtd_linha = 5
qtd_coluna = 5

linha = 1

while linha <= qtd_linha:
    print(linha, end=": ")

    coluna = 1
    while coluna <= qtd_coluna:
        print(coluna, end=" ")
        coluna+=1

    print()
    linha+=1