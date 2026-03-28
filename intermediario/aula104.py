
# Todo import de um módulo é um Singleton, só se carrega uma vez
# Sempre que quiser recarregar use o importlib, só que se usa mais memória

import importlib
import aula104_m

for i in range(10):
    print(i)
    importlib.reload(aula104_m)

print('Fim')