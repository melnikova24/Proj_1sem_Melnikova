# В матрице найти среднее арифметическое положительных элементов

import random

stl = int(input('Введите количество столбцов: '))
str = int(input('Введите количество строк: '))

matrix = [[random.randint(-5, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

n = []
for i in matrix:           # проверяем кратность элементов (i строка, t элемент в матрице)
    for t in i:
        if t > 0:
            n.append(t)
print(f'Положительные элементы: {n}')
print('Их среднее арифметическое значение: ', sum(n)/len(n))