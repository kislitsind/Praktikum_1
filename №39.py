"""
Имя проекта: №38
Номер версии: 1.0
Имя файла: practicum-1(№38).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 28/11/2020
Дата последней модификации: 28/11/2020
Связанные файлы/пакеты: 
Описание: Решение задач № 38 практикума № 1
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""

import random

N = int(input("Введите количество элементов в массиве: "))
A = [random.randint(-1, 1) for i in range(0, N)]

print(A)
B = filter(bool, A)
print(list(B))
