"""
Имя проекта: №34
Номер версии: 1.0
Имя файла: practicum-1(№34).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 27/11/2020
Дата последней модификации: 27/11/2020
Дан одномерный массив числовых значений, насчитывающий N элементов. Поменять местами первую и вторую половины массива
Описание: Решение задач № 34 практикума № 1
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""

import random

N = int(input("Введите количество элементов массива "))
a = [random.randint(0, 100) for i in range(0, N)]
print(a)
for i in range(len(a) // 2):
    a[i], a[i + len(a) // 2] = a[i + len(a) // 2], a[i]
    
print(a)
