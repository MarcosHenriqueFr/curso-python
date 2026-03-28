
# Os módulos em python e como usar eles
# A forma como você importa não muda nada, só legibilidade

# import datetime, sys

# print(datetime.datetime.now())
# print(sys.platform)

# Tomar cuidado com nomes
# from datetime import datetime

# print(datetime.now())

# Sempre busque mudar o nome da sua variavel interna ao invés do nome do módulo
import datetime as dt
from sys import platform as pt

datetime = 'SOBRESCREVEU'
print(datetime, dt.datetime.now())
print('Sua plataforma:', pt)

# EVITE IMPORTE COM *, PIORA A LEGIBILIDADE, e todos os objetos podem ser usados