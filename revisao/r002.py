
nome = "Jorge"
num1, num2 = 10, 3
print(num1 + num2)

# Posso fazer a demonstração no mesmo print mesmo com diferentes data types
print(nome, num1)

# Variaveis globais

idade = 21

def dizer_idade():

    # Bom para mudar valores que sejam globais aqui dentro
    global data
    data = "Terça"

    # É um valor diferente da de fora
    idade = 32 # A mais encapsulada sempre aparece
    print(f'Minha idade é {idade} anos!')

dizer_idade()

# Consigo usar uma variavel global dentro da função fora??????
print(data)

# Tipos de dados: 
'''
    str -> texto
    int, float, complex -> Numericos
    list, tuple, range -> tipos sequenciais
    dict -> tipo mapping
    set, frozenset -> tipos set
    bool -> tipos bool
    bytes, bytesarray, memoryview -> binaryTypes
    NoneType -> seria um tipo null ?????
'''

# Deve ser parecido com como as collections funcionam em java
frutasLista = ["Banana", "Maçã"]
frutasSet = {"Banana", "Maçã"}
frutasTupla = ("Banana", "Maçã")
nenhum = None # Isso aqui é um tipo específico

# É possível confirmar o tipo desejado escolhendo o tipo de dado na inicialização
vf = bool(5)
print(vf) # Tudo que não é vazio é true3