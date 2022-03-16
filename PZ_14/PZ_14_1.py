# Вариант 27
# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации
# за 1857  год и поместить ее в новый текстовый файл.

import re

inp = open('Dostoevsky.txt', 'r', encoding="utf-8")
out = open('output.txt', 'w', encoding="utf-8")
all = inp.read()

block = re.search('1857 год[а-яА-ЯёЁ\W]*Христа.', all)[0]
out.write(block)
out.close()