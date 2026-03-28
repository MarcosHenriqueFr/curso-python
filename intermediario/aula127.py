
# Continuando com os métodos do context manager

from dados import produtos

caminho = './intermediario/texto/aula127.txt'

# Toda vez que ele abre ele apaga os valores e reescreve
# Alguns métodos não funcionam dependendo da forma como você está acessando o arquivo
with open(caminho, 'w') as arquivo:
    print('Aberto')

    for prod in produtos:
        for chave, valor in prod.items():
            arquivo.write(f'{chave}: {valor}; ')

        arquivo.write('\n')
    
    print('Fim da escrita')
    
with open(caminho, 'r') as arquivo:
    print('Lendo arquivo...')
    print(arquivo.read())
    print('Fim da escrita')