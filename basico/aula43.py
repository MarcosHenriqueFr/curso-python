
'''
Iterável -> possui um método __iter__
'''

frase = 'Maria Luisa'
iterador = iter(frase)
nova_frase = ''

while True:
    try:
        letra = f'*{next(iterador)}'
        nova_frase += letra
        print(letra, end=" ")
    except StopIteration as si:
        print('Fim da Frase')
        break
    
nova_frase += "*"
print(nova_frase)