
# Funções de primeira ordem/classe
# Posso passar funções como argumentos assim como também retornar elas
# Funções também são um tipo de dado em python

# Higher Order Functions - Funções que podem receber e/ou retornar outras funções

# First-Class Functions - 
# Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

def saudacao(texto, nome):
    return f'{texto}, {nome}!!!'

def executa_saudacao(saudacao, *args):
    return saudacao(*args)

resultado = executa_saudacao(saudacao, 'Bom dia', 'Maria')

print(resultado)