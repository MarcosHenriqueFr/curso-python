
frase = 'Python é uma linguagem de programação multiparadigma. '\
        'Python foi criado por Guido Von Rossum.'
        
i = 0
letra_mais = ''
qtd_letra_mais = 0

while i < len(frase):
    letra_atual = frase[i]
    qtd_vezes_atual = frase.count(letra_atual)
    
    i += 1
    
    if letra_atual == ' ':
        continue
    
    if qtd_letra_mais < qtd_vezes_atual:
        letra_mais = letra_atual
        qtd_letra_mais = qtd_vezes_atual
        
    
print(letra_mais, qtd_letra_mais)
    