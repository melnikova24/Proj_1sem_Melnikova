# В квадратной матрице все элементы, не лежащие на главной диагонали
# увеличить в 2 раза

import random

stl = int(input("Введите кол-во столбцов: "))
str = int(input("Введите кол-во строк: "))
matrix = [[random.randint(-10, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

for i in range(stl):
    for j in range(str):
        if j != i:
            matrix[i][j] = matrix[i][j] ** 2

print('Результат: ')
for v in matrix:
    print(v)
