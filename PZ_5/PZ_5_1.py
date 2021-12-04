# Вариан 27.
# Составить программу, в которой функция генерирует четырёхзначное
# число и определяет, есть ли в числе одинаковые цифры.

import random


def generate4digit():
    number = str(random.randint(1000, 9999))
    i = 0
    result = 0
    while i < len(number):
        if number[i] in number[i + 1:]:
            result = 1
            break
        i += 1
    if result == 0:
        print(f"В числе {number} нет повторяющихся цифр")
    else:
        print(f"В числе {number} есть повторяющиеся цифры")


generate4digit()