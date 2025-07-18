
# Pode ter o uso do while/else. Grande parte das estruturas em python possuem else
# É como um finally no try, porém ele quebra o com o break

texto = "Texto Simples"
cont = 0

# Simplesmente quando não atende a condição

while cont <= len(texto):
    letra = texto[cont]
    
    print(letra, end='')
    
    if letra == ' ':
        print('\nEspaço Vazio.')
    
    if letra == 's':
        break
    
    cont+=1
else:
    print('O else do while.')
    
print('\nSaiu do while.')