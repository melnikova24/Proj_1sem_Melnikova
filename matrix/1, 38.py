# Перенести в новую матрицу Matr1 элементы, которые не находятся в
# первых и последних строках и столбцах матрицы Matr2 произвольного
# размера

import random

stl = int(input('Введите количество столбцов: '))
str = int(input('Введите количество строк: '))

Matr2 = [[random.randint(1, 10) for i in range(stl)] for j in range(str)]
Matr1 = []
print('Исходная: ')
for v in Matr2:
    print(v)

for i in range(stl):
    n = []
    for j in range(str):
        if i != 0 and i != str - 1 and j != 0 and j != stl - 1:
            n.append(Matr2[i][j])
    if n:
        Matr1.append(n)
print('Matr1: ')
print(Matr1)