
# Todas as importações que acontecem no meu programa dever ser relacionadas ao meu main
# Por causa da política de loading do python de sempre manter esse módulos disponíveis

# Tudo funciona desde que a execução/stack comece no main

from aula105_package.modulo import numero_potencia, falar_frase

print(numero_potencia(12, 2))
falar_frase()