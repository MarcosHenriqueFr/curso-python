
import random

# Esses tipos numericos possuem valores ilimitados
x = 1
y = 2.2
z = 1j # Um número complexo assim como na matemática

# Complexos não podem ser convertidos
# python é dinamico e forte
# z = int(y)

idade_aleatoria = random.randrange(1, 100)
print(f'Você possui {idade_aleatoria} anos.')

x2 = 2
x3 = 2

if x2 is x3:
    print('Mesmo local de memória')
if x2 is not x:
    print('Não é o mesmo local de memória')

cedo, comeu = True, False

if cedo | comeu:
    print('Da para usar as palavras ou os simbolos')

if cedo << 2:
    print("Banana")

x = 3
x+=1
print(x)
