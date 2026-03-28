
# Try - except e finally

try:
    c = 'abc'[100]
    a = 10
    b = 0
    c = a / b
except ZeroDivisionError:
    print('Aconteceu uma divisão por zero.')
except (NameError, IndexError) as error:
    print('NameError + IndexError')
    print('Mensagem PADRÃO:', error)
except TypeError:
    print('O tipo da variável não está correto')
except Exception as error:
    print('Erro desconhecido.')
    print('MSG:', error)
    print('Nome do erro:', error.__class__.__name__)