"""
Имя проекта: №44
Номер версии: 1.0
Имя файла: practicum-1(№44).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 05/12/2020
Дата последней модификации: 05/12/2020
Дан одномерный массив числовых значений, насчитывающий N элементов. Добавить столько элементов, чтобы элементов с положительными и отрицательными значениями стало бы поровну.
Описание: Решение задач № 44 практикума № 1
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""

import random
N = random.randint(0,15)
arr = [random.randint(-90,190) for i in range(N)]
print(arr)
plus = 0
minus = 0
for i in range(N):
    if arr[i] >0:
        plus+=1
if plus > minus:
    for i in range(minus , plus):
        arr.append(random.randint(-90,-5))
elif plus < minus:
    for i in range(plus , minus):
        arr.append(random.randint(3,15))
print("Номер плюс: " + str(plus))
print("Номер минус: " + str(minus))
print(arr)
