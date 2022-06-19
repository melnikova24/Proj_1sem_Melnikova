# В матрице найти отрицательные элементы, сформировать из них новый
# массив. Вывести размер полученного массива

import random

stl = int(input("Введите кол-во столбцов: "))
str = int(input("Введите кол-во строк: "))
matrix = [[random.randint(-10, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

n = []
for i in matrix:
    for t in i:
        if t < 0:
           n.append(t)
print('Одномерный массив: ')
print(n)
print('Размерность одномерного массива: ', len(n))