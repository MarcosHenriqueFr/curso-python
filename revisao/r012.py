
from random import randint, choice

num_al = randint(1, 10)
cores = ["Vermelho", "Amarelo", "Azul", "Preto", "Branco", "Roxo", "Lilás"]

cor_al = choice(cores)

print(num_al, cor_al)

from datetime import datetime as dt
data = dt.now()
print(data)

# import modulo_inexistente

import math, statistics

nums = [50, 30, 10, 20, 40, 60]

soma = math.fsum(nums)
media = statistics.mean(nums)

print(f'A soma dos números resultou em {soma} e uma média de {media}')