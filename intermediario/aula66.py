
# Valores padrões para parametros

# Considerando o parâmetro como None, considerando que o código foi refatorado
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} | x + y + z = {x + y + z}')
    else:
        print(f'{x=} {y=} | x + y = {x + y}')
        
soma(20, 40)
soma(1, 7)
soma(10, 70, 80)
soma(y=8, x=9)