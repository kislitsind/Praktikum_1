"""
Имя проекта: №48
Номер версии: 1.0
Имя файла: practicum-1(№48).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/12/2020
Дата последней модификации: 11/12/2020
Дан одномерный массив числовых значений, насчитывающий N элементов. Вместо каждого элемента с нулевым значением поставить сумму двух предыдущих элементов массива.
Описание: Решение задач № 48 практикума № 1
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""

import random

N = random.randint(1,25)
arr=[random.randint(-1,1) for i in range(N)]
print(arr)

for i in range(N):
    if arr[i] ==0:
     t = arr[i-1] + arr[i-2]
     arr[i] = t
print(arr)
