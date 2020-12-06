"""
Имя проекта: №45
Номер версии: 1.0
Имя файла: practicum-1(№45).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 05/12/2020
Дата последней модификации: 05/12/2020
Связанные файлы/пакеты: 
Описание: Решение задач № 45 практикума № 1
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""

import random
N = random.randint (0,15)
arr = [random.randint(-150, 150) for i in range(N)]
print(arr)
sum_plus = 0
sum_minus = 0
for i in range(N):
    if arr[i] > 0:
        sum_plus += arr[i]
    elif arr[i] < 0:
        sum_minus += arr[i]
print("сумма положительных элементов равна: " + str(sum_plus))
print("сумма отрицательных элементов равна: " +str(-sum_minus))
if sum_plus > -sum_minus:
    arr.appen(-(sum_minus + sum_plus))
elif sum_plus < -sum_minus:
    arr.append(-(sum_plus + sum_minus)
print(arr)
