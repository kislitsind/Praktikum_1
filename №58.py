"""
Имя проекта: №58
Номер версии: 1.0
Имя файла: practicum-1(№58).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 18/12/2020
Дата последней модификации: 18/12/2020
Описание: Решение задач № 58 практикума № 1
описание:  Задана строка символов, в которой встречается символ «.». Поставить после каждого такого символа системное время ПК.
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""

from datetime import datetime
M = 3

list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

now = str(datetime.now())

for string in list_strings:
    print(string.replace('.', '.' + now))
