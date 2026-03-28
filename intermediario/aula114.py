
def zipper(cidades, ufs):
    
    resultado = []
    n_conjunto = len(cidades) if len(cidades) < len(ufs) else len(ufs)

    for indice in range(n_conjunto):
        resultado.append((cidades[indice], ufs[indice]))

    return resultado
         

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Brasília']
ufs = ['BA', 'SP', 'MG', 'DF', 'RJ']

print(zipper(cidades, ufs))