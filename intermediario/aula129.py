
# Agindo sobre arquivos com o módulo os

from dados import produtos
import os

caminho = './intermediario/texto/aula129.txt'

with open(caminho, 'w+', encoding='utf-8') as arquivo:
    print('Aberto')

    arquivo.write('ATENÇÃO, ESCRITA DOS PRODUTOS\n\n')

    for prod in produtos:
        for chave, valor in prod.items():
            arquivo.write(f'{chave}: {valor}; ')

        arquivo.write('\n')
    
    print('Leitura de uma linha na escrita: ')
    arquivo.seek(0, 0)

    print(arquivo.readline(), end='')

    print('Fim da escrita')

# os.unlink(caminho)
# os.remove(caminho)

# Com rename dá para criar um path diferente