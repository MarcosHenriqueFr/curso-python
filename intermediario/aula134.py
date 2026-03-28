# Solução do professor:

# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os, json

# método só entra em dicionário se for adiado com lambda

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()

def criar_db(caminho):
    print('Criando um novo arquivo de banco de dados...')
    with open(caminho, 'w') as arquivo:
        tarefas = []
        json.dump(tarefas, arquivo, indent=2)

        return tarefas

def checar_db(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            tarefas_do_json = json.load(arquivo)

            return tarefas_do_json
    except FileNotFoundError as error:
        print('Não foi possível encontrar o arquivo.')

        return criar_db(caminho)
    
def salvar_db(tarefas, caminho):
    with open(caminho, 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=2)
        
def executar_menu(tarefas, tarefas_refazer):
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
    elif tarefa == 'clear':
        os.system('clear')
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)

caminho_db = './intermediario/texto/aula134.json'
tarefas = checar_db(caminho_db)
tarefas_refazer = []

while True:
    try:
        executar_menu(tarefas, tarefas_refazer)
        continue
    except KeyboardInterrupt as error:
        salvar_db(tarefas, caminho_db)
        raise error