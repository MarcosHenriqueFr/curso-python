
# Saber valores de classes
# dir, hasattr, getattr

nome = 'Marcos'
metodo = 'upper'

# Mostra tudo definido dentro do objeto
# print(dir(nome))

if(hasattr(nome, metodo)):
    print('Existe upper')
    print(getattr(nome, metodo)())
else:
    print('Não existe upper')
