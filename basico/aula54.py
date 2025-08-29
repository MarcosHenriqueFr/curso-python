
# Fazer um programa de lista de compras

lista_compras = []
while True:
    print('Selecione uma opção:')
    input_usuario = input('[i]nserir [a]pagar [l]istar [s]air: ')
    
    match input_usuario:
        case 'i':
            novo_valor = input('Digite o valor a ser inserido: ')
            lista_compras.append(novo_valor)
            print('Valor inserido com sucesso!')
        case 'a':
            indice = input('Digite o indice do item que vai ser apagado: ')
            try: 
                indice = int(indice)
                del lista_compras[indice]
                print('Valor removido com sucesso.')
            except:
                print('O valor de indice não existe na lista.')
        case 'l':
            if len(lista_compras) == 0:
                print('Não tem nada para ser listado')
            else:
                for indice, valor in enumerate(lista_compras):
                    print(indice, valor)
        case 's':
            print('Saiu do programa.')
            break
        case _: 
            print('Não é uma opção válida')