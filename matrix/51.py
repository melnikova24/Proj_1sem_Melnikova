# В матрице найти среднее арифметическое положительных элементов

import random

stl = int(input("Введите кол-во столбцов: "))
str = int(input("Введите кол-во строк: "))
matrix = [[random.randint(-10, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

n = []           # создаем пустой список для положительных чисел
for i in matrix:           # проверяем положительность (i строка, t элемент в матрице)
    for t in i:
        if t > 0:
            n.append(t)
print(f"Положительные элементы матрицы: {n}")
print("Их среднее арифметическое значение:", sum(n)/len(n))