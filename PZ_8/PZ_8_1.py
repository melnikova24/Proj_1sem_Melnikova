# Вариант 27
# Организовать словарь на 10 англо-русских слов, обеспечивающий "перевод"
# английского слова на русский.

sl = {'star': 'звезда', 'vampire': 'вампир', 'had': 'голова', 'fox': 'лиса',
       'table': 'стол', 'computer': 'компьютер', 'keyboard': 'клавиатура',
       'sun': 'солнце', 'cloud': 'облако', 'nails': 'ногти'}

print("Добро пожаловать!")
while True:
    try:
        search = input("Введите слово: ")
        if search == 'завершить' or search == 'quit':
            print('Завершено.')
            break
        print(search + ' - ' + sl[search])
        print('ENG' + ('' * (len(search))) + 'RUS')
        print()
    except KeyError:
        print("Ошибка. Слово не существует в словаре программы")
        print()
