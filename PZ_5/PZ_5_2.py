# Вариант 27.
# Описать функцию AddRightDigit(D, K), добавляющую к целому положительному
# числу K справа цифру D (D - входной параметр целого типа, лежащий
# в диапазоне 0-9, K - параметр целого типа, являющийся одновременно входным
# и выходным). С помощью этой функции последовательно добавить к данному числу К
# справа данные цифры D1 и D2, выводя результат каждого добавления.

def addrightdigit(a, b):
    b = str(b) + str(a)
    return b


K = int(input("Введите число K (> 0): "))
D1 = int(input("Введите D1 (в диапазоне 0-9): "))
while D1 < 0 or D1 > 9:
    print("Введено D1 вне диапазона")
    D1 = int(input("Введите D1 снова: "))
k = addrightdigit(D1, K)
print(K)
D2 = int(input("Введите D2 (в диапозоне 0-9): "))
while D2 < 0 or D2 > 9:
    print("Вы ввели D2 вне диапозона")
    D2 = int(input("Введите D2 снова: "))
K = addrightdigit(D2, K)
print(K)