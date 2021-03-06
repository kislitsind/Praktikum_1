"""
Имя проекта: №66
Номер версии: 1.0
Имя файла: practicum-1(№66).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 03/03/2021
Дата последней модификации: 03/03/2021
Описание:Для вводимых чисел определить процент положительных и отрицательных чисел. При вводе числа −65432 закончить работу.
#версия Python: 3.6
"""

import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]
n = 0
m = 0
N = -65432
for i in range(M):
    arr[i] = input()
for i in range(M):
    if int(arr[i]) > 0:
        n += 1
    if int(arr[i]) < 0:
        m += 1
    if int(arr[i]) == -65432:
        break
print(" % положительных чисел: " + str(100/ len(arr) * n))
print(" % процент отрицательных чисел: " + str(100 / len(arr) * m))
