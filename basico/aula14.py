# Uso de funções format

a = 'A'
b = 'B'
c = 1.1

# Tudo é um objeto em python
# Passa os valores de acordo com a sua ordem na chave, uma array
# Tem a string original e os meus parametros, tal como um String.format na INSTANCIA

formato = 'a={0}, b={1}, c={2:.2f} teste={3}'.format(a, b, c, 'teste')
formato2 = 'b={nome2}, a={nome1}, c={nome3:.2f} teste={nome4}'.format(nome1=a, nome2=b, nome3=c, nome4='teste')

print(formato)
print(formato2)