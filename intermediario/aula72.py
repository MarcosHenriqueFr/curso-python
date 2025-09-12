


a = 2
b = a

print(a, b)
print(f'a: {id(a)}', f'b: {id(b)}')

a = 10

print(a, b)
print(f'a: {id(a)}', f'b: {id(b)}')