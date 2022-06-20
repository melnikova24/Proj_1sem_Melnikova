# В матрице отрицательные элементы возвести в квадрат

import random

stl = int(input("Введите кол-во столбцов: "))
str = int(input("Введите кол-во строк: "))

matrix = [[random.randint(-10, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

for g in range(stl):
    for t in range(str):
        if matrix[g][t] < 0:
            matrix[g][t] = matrix[g][t] ** 2
print('Результат: ')
for v in matrix:
    print(v)
