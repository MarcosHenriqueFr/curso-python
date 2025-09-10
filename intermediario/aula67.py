# Escopo de funções
# Assim como no Java a mais interna é priorizada

# O escopo global -> é mais um escopo do módulo
x = 'de fora'

def escopo():
    def outra_funcao():
        # global x; para mudar globalmente -> não é uma boa prática
        x = 'de dentro'
        print(x)
        
    print(x)
    outra_funcao()
    
escopo()