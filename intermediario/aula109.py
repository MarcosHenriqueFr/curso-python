
# def fora(x=0):
#     a = x

#     def dentro():
#         return a
    
#     return dentro

# print(fora()())
# print(fora(10)())
# print(fora(20)())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        # Não dá porque é uma variavel livre
        # valor_final += valor_a_concatenar

        nonlocal valor_final # O python tenta buscar em um valor acima
        valor_final += valor_a_concatenar
        
        return valor_final
    
    return interna

frase = concatenar('a')
print(frase('b'))
print(frase('c'))
print(frase('d'))

final = frase()

print(f'{final=}')