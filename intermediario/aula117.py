# Count é um iterador sem fim

from itertools import count
c1 = count(6, 6)
r1 = range(6, 100, 6)

print('count:', hasattr(c1, '__iter__'))
print('count:', hasattr(c1, '__next__'))

# ELe chama ele mesmo
print('count:')

for i in c1:

    if i > 100:
        break

    print(i, end=' ')

print()
print('range:')

for i in r1:
    print(i, end=' ')

print()