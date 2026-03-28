
def meuZipper(l1, l2):
    tamanho = min(len(l1), len(l2))

    return [(l1[i], l2[i]) for i in range(tamanho)]

from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Brasília']
ufs = ['BA', 'SP', 'MG', 'DF', 'RJ']

# Do programa
print(meuZipper(cidades, ufs))

# Classe do python
print(list(zip(cidades, ufs)))

# Classe que engloba valores sem assimilação na outra lista
print(list(zip_longest(cidades, ufs, fillvalue='SEM CIDADE')))