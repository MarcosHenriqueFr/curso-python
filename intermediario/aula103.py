
# Modularização - DOS SEUS PACOTES
# O primeiro módulo a ser executado se chama __main__
# O módulo executa só de ser importado
import aula103_m
# import sys

print('O nome desse módulo é:', __name__)
# print(*sys.path, sep='\n')  # O python busca módulos que estão dentro desses pacotes

print(aula103_m.nome)
print(aula103_m.soma(10, 20))

# USE SEMPRE O MAIN COMO O PONTO DE ENTRADA