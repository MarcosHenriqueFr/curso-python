# Generator functions - Pausam e executam de onde pararam, enquanto o programa (como um todo) está na memória

def generator(n=0):
    count = 1 # Pausa e a variavel não é perdida

    # A função tem que ter noção que está em um loops 
    while count <= n:
        yield count
        count += 1
    
    return 'ACABOU'

gen = generator(3)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

