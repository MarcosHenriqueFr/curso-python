
import copy

# Cópia rasa e cópia profunda

pessoa = {
    'nome': 'Mario',
    'idade': 20,
    'nums': [1, 2, 3]
}

pessoa2 = pessoa

pessoa2['nome'] = 'Jorge'

# O mesmo objeto sendo modificado
print(pessoa, pessoa2)

# Cópia rasa para objetos diferentes / Não entra em subníveis, como sublistas
pessoa3 = pessoa.copy()

pessoa3['nome'] = 'Maria'
pessoa3['nums'][0] = 1000

print(pessoa, pessoa3)

# Cópia profunda com import, entra em toda a árvore

pessoa4 = copy.deepcopy(pessoa)

pessoa4['nums'][0] = 10

print(pessoa, pessoa4)