# Вариант 27
# В матрице найти среднее арифметическое положительных элементов, кратных 3.

import random

M = 3
matrix = [[random.randint(-2, 10) for j in range(M)] for i in range(M)]
print(*matrix, sep='\n')

n = []
for i in matrix:
    for t in i:
        if t % 3 == 0 and t > 0:
            n.append(t)
print(f"Положительные элементы матрицы, кратные трём: {n}")
print("Их среднее арифметическое значение:", sum(n)/len(n))