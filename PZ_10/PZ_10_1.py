# Вариант №27
# Средствами языка Python формировать два текстовых файла (.txt), содержащих
# по одной последовательности из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно
# выполнив требуемую обработку элементов:
# Элементы перового и второго файлов;
# Элементы первого файла, присутствующие во втором;
# Элементы второго файла, присутствующие в первом;
# Количество элементов;
# Количество отрицательных элементов;
# Количество положительных элементов;

import random

n = 0
a = []
b = []

# Создаём список из "рандомных" цифр и помещаем их в файл 1
f1 = open("file1.txt", "w", encoding="UTF-8")
for i in range(10):
    a.append(random.randint(-5, 10))
    f1.write(str(a[i]))
    f1.write(" ")
f1.close()

# Создаём список из "рандомных" цифр и помещаем их в файл 2
f2 = open("file2.txt", "w", encoding="UTF-8")
for i in range(10):
    b.append(random.randint(-10, -1))
    f2.write(str(b[i]))
    f2.write(" ")
f2.close()    # Мы создали список из отрицательных "рандомных" цифр и заполнили ими файл

f1 = open("file1.txt")
i = f1.read()
f1.close()

f2 = open("file2.txt")
q = f2.read()
f2.close()
# Построчно выполняем задания
# 1 пункт
f3 = open("file3.txt", "w", encoding="UTF-8")
f3.write("Элементы первого и второго файлов: \n")
f3.write(i)
f3.write(q)
f3.write("\n")
# 2 пункт
f3.write("Элементы первого файла, присутствующие во втором: \n")
for i in range(len(a)):
    if a[i] in b:
        f3.write(str(a[i]))
f3.write("\n")
# 3 пункт
f3.write("Элементы второго файла, присутствующие в первом:\n")
for i in range(len(a)):
    if b[i] in a:
        f3.write(str(b[i]))
f3.write("\n")
# 4 пункт
f3.write("Количество элементов:\n")
both = len(a) + len(b)
f3.write(str(both))
f3.write("\n")
# 5 пункт
f3.write("Количество отрицательных элементов:\n")
for i in range(len(a)):
    if a[i] < 0:
        n += 1
for i in range(len(b)):
    if b[i] < 0:
        n += 1
f3.write(str(n))
n = 0
f3.write("\n")
# 6 пункт
f3.write("Количество положительных элементов:\n")
for i in range(len(a)):
    if a[i] > 0:
        n += 1
for i in range(len(b)):
    if b[i] > 0:
        n += 1
f3.write(str(n))

f3.close()
