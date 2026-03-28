
# Exercício
# Lista de tarefas com fazer e refazer
tarefas = []
historico = []

def checar_tarefa(lista, mensagem):
    if not lista:
        print(mensagem, end='')
        return False
    
    return True

def listar_tarefas():
    checar_tarefa(lista=tarefas, mensagem='Nenhuma tarefa a listar.')
    
    print(*tarefas, sep='\n') 

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)

def desfazer():
    checar_tarefa(lista=tarefas, mensagem='Nenhum item a desfazer.')

    ultimo_valor = tarefas.pop()
    historico.append(ultimo_valor)

def refazer():
    existe = checar_tarefa(lista=historico, mensagem='Nenhum item a refazer.')

    if existe:
        ultimo_valor = historico.pop()
        tarefas.append(ultimo_valor)

def limpar_historico():
    historico.clear()

while(True):
    print(f'Comandos: listar, desfazer, refazer')
    resposta_usuario = input('Digite uma tarefa ou comando: ')
    print()

    match resposta_usuario:
        case 'listar':
            listar_tarefas()
        case 'desfazer':
            desfazer()
            listar_tarefas()
        case 'refazer':
            refazer()
            listar_tarefas()
        case _:
            adicionar_tarefa(resposta_usuario)
            limpar_historico()
            listar_tarefas()

    print()
