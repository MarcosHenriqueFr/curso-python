nomes = ["Alice", "João", "Clara", "Beatriz", "Amanda", "Julia"]

nomes_iniciam_a = [nome for nome in nomes if nome[0] == 'A']

print(nomes_iniciam_a)

quadrados_ate_10 = [val ** 2 for val in range(1, 11)]

print(quadrados_ate_10)

palavras = ["Sol", "Caixa", "Pedra", "Extintor", "Pão", "Lírio", "Giz", "Céu"]

palavras_3 = [pal for pal in palavras if len(pal) != 3]
print(palavras_3)