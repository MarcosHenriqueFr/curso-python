# Manipulação de arquivos
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# Da raiz do vscode, até o local do arquivo
caminho_arquivo = './intermediario/texto/aula126.txt'

# Sempre feche objetos de arquivo, usando de forma pura

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# Com context manager - abre e fecha

with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo.')
    print('Esse arquivo vai ser fechado')