"""
Имя проекта: №51
Номер версии: 1.0
Имя файла: practicum-1(№51).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 13/12/2020
Дата последней модификации: 13/12/2020
Описание: Решение задач № 51 практикума № 1
описание: Заданы M строк символов, которые вводятся с клавиатуры. Найти количество символов в самой длинной строке. Выровнять строки по самой длинной строке, поставив перед каждой строкой соответствующее количество звёздочек.
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""


A = [A * 3 for A in 'abc']
print(A)
B = ['1', '2', '3']
print(B)
list.sort(B, key=len)
print(B)

for i in range(len(B)):
    if len(B[i]) < len(B[i+1]):
        list.insert(0, '*')
        i = i + 1
        
print(B)
