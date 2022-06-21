# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE

import random   # не уверена, вообще странное условие задачи

stl = int(input('Введите количество столбцов: '))
str = int(input('Введите количество строк: '))

matrix = [[random.randint(-10, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

for g in matrix:
    for t in g:
        if t > 0:
            print('TRUE')
        else:
            print('FALSE')