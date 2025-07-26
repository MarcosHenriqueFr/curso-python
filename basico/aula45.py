
from os import system, name
import random

palavras = ['Água', 'Cavalo', 'Elefante', 'Prédio', 'Bom', 'Lírio', 'Ponto', 'Bula', 'Cachoeira']
indice_random = random.randint(0, len(palavras) - 1)
palavra_original = palavras[indice_random]

print(palavra_original)
palavra_jogador = ''

for letra in palavra_original:
    palavra_jogador += '*'
lista_palavra_jogador = list(palavra_jogador)
lista_palavra_jogo = list(palavra_original)

tentativas = 0

print('Atenção!!! Palavras com acento são caracteres diferentes!')

while True:
    letra = input('Digite uma letra para descobrir a palavra: ')
    tentativas += 1
    
    if len(letra) > 1:
        print('Digite somente uma letra.')
        continue
    
    if len(letra) == 0: 
        print('Digite algo...')
        continue
    
    # Analisar quais letras iguais aquelas tem esse indice
    i = 0
    while i < len(lista_palavra_jogo):
        if lista_palavra_jogo[i].lower() == letra:
            lista_palavra_jogador[i] = lista_palavra_jogo[i]
            palavra_jogador = ''.join(lista_palavra_jogador)
        i += 1
        
    print(palavra_jogador)
        
    if palavra_jogador == palavra_original:
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        
        print('Você ganhou o jogo!!!')
        print(f'Tentativas: {tentativas}')
        break