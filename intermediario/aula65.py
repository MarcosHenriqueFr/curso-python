
# Argumentos nomeados e não-nomeados(posicional)
# Argumento nomeado -> keyword argument

def soma(x, y):
    print(f'{x=} {y=} | x + y = {x + y}')
    
# É melhor usar somente uma forma por chamada
# Os não nomeados são o padrão e dependem da ordem
soma(2, 4)

# os nomeados colocam o valor do parametro na parte dos argumentos
soma(y=4, x=2)