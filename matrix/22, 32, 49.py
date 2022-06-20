# В матрице найти сумму элементов второй половины матрицы

import random

stl = int(input('Введите количество столбцов: '))
str = int(input('Введите количество строк и размер массива: '))

matrix = [[random.randint(-3, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

n = int(stl / 2)
a = [sum(matrix[j]) for j in range(str) if j >= n]  # Находим сумму второй половины матрицы
m_sum = sum(a)

print('Сумма элементов второй половины матрицы:', '\n', m_sum)

