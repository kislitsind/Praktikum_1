"""
Имя проекта: №43
Номер версии: 1.0
Имя файла: practicum-1(№43).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 05/12/2020
Дата последней модификации: 05/12/2020
Связанные файлы/пакеты: 
Описание: Решение задач № 43 практикума № 1
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""

import random
N = random.randint(1,15)
arr = [random.randint(-90,90) for i in range(N)]
print(arr)
arrP = []
arrN = []
for i in range(N):
    if arr[i] < 0:
        arrN.append(arr[i])
    if arr[i] > 0:
        arrP.append(arr[i])
    print (arrN)
    print (arrP)
