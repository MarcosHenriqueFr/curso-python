
texto = "Pedro Veras"

cont = 0
nova_string = ""
while cont < len(texto):
    novo_elemento = f'*{texto[cont]}'
    nova_string += novo_elemento
    cont += 1

print(nova_string)