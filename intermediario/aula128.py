
# Modos de abertura de arquivo

from dados import produtos

caminho = './intermediario/texto/aula128.txt'

# w -> apaga, e reescrebe
# a -> só escreve

# with open(caminho, '+a') as arquivo:
# Trabalhando com a mesma codificação de caracteres dentro do arquivo
with open(caminho, 'w+', encoding='utf-8') as arquivo:
    print('Aberto')

    arquivo.write('ATENÇÃO, ESCRITA DOS PRODUTOS\n\n')

    for prod in produtos:
        for chave, valor in prod.items():
            arquivo.write(f'{chave}: {valor}; ')

        arquivo.write('\n')
    
    print('Leitura de uma linha na escrita: ')
    arquivo.seek(0, 0)

    # Funcionando como o next de um iter
    print(arquivo.readline(), end='')

    print('Fim da escrita')
    
with open(caminho, 'r') as arquivo:
    print('Lendo arquivo...')
    print(arquivo.read())
    print('Fim da escrita')