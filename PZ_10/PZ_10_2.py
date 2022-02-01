# Вариант №27
# Из предложенного текстового файла (text18-27.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку фразой введенной
# пользователем.

import string

text = open('text18-27.txt', encoding='utf-8').read()
print(text)

for p in string.punctuation + '\n':
    if p in text:
        text = text.replace(p, " ")
count = 0
for letter in text.replace(" ", ""):
    if letter.islower():
        count += 1
print('Строчных букв в исходном файле', count)

print(open('text18-27.txt', encoding='utf-8').read(172), file=open('new_file.txt', 'w', encoding='utf-8'))

with open('new_file.txt', 'a', encoding='utf-8') as f_in:
    f_in.write(input('Введите строку для записи последней строкой: '))