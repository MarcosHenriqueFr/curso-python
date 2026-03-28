
# Funções decorators - Funções que decoram outras funções
# Vai ter que fazer o uso de closures

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
    
    return interna

def e_string(param):
    if not isinstance(param, str):
        raise TypeError(f'{param} não é uma string')

def inverte_string(string):
    return string[::-1]

print(inverte_string('123'))
inverte_string_checando_param = criar_funcao(inverte_string)

lista = inverte_string_checando_param('abc', 1, 'a12')
print(lista)