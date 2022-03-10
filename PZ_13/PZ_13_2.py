# Вариант 27.
# Составить генератор (yield), который переведет символы строки из нижнего
# регистра в верхний.

def gen(str):
    for i in str:
        yield i.upper()

str = input("Введите предложение: ")

for i in gen(str):
    print(i, end="")
