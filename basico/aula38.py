
while True:
    # Código a ser desenvolvido
    num1_input = input('Digite o primeiro número para a operação: ')
    operador = input('Digite um operador para realizar o cálculo: ')[0]
    num2_input = input('Digite o segundo número para a operação: ')


    try:
        num1 = float(num1_input)
        num2 = float(num2_input)

        match operador:
            case '+':
                print(num1 + num2)
            case '-':
                print(num1 - num2)
            case '*':
                print(num1 * num2)
            case '/':
                print(num1 / num2)
            case _:
                print('Não é um operador válido')

    except:
        print('Não é um número válido')
        continue

    sair = input('Quer sair? s/any: ').lower().startswith('s')

    if sair:
        break