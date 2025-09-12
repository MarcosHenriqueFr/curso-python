
# Closures 

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!!!'
    
    return saudar

f_bom_dia = criar_saudacao('Bom dia')
f_prazer = criar_saudacao('Prazer conhecer')
f_boa_tarde = criar_saudacao('Boa tarde')

# Força a manutenção dos dados em memória para que sejam executados depois
# Salva os dados na call stack
# Permite criar funções que criam funções

print(f_bom_dia('Maria'), f_prazer('Jorge'), f_boa_tarde('Julia'), sep='\n')