# Вариант 27
# Дан символ C и строка S. Удвоить каждое вхождение символа C в строку S.

print("Добро пожаловать!")
C = input("Введите удваиваемый символ: ")
text = list(input("Введите текст: "))
textLen = len(text)

def convert(s):
    str1 = ""
    return (str1.join(s))


for i in range(0, textLen):
    if (text[i]) == C:
        text[i] = text[i] + C

print("Итоговый текст: " + convert(text))
