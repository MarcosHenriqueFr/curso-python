
# Decoradores em python - syntax sugar
# São como as classes funcionais do java

def criar_funcao(funcao):
    def interna(*args, **kwargs):
        resultados = []

        for arg in args:
            try:
                e_string(arg)
                resultado = funcao(arg, **kwargs)
                resultados.append(resultado)
            except TypeError as error:
                print('Erro:', error)
            
        return resultados
    
    # Esse aqui é o fechamento da closure
    return interna

def e_string(param):
    if not isinstance(param, str):
        raise TypeError(f'{param} não é uma string')

@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

# A função de inverter string é reescrita pelo seu decorador
print(inverte_string('123', 'Marcos', 21, True, 'Teste'))