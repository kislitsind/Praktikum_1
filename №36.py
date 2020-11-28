"""
Имя проекта: №36
Номер версии: 1.0
Имя файла: practicum-1(№36).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 28/11/2020
Дата последней модификации: 28/11/2020
Связанные файлы/пакеты: 
Описание: Решение задач № 36 практикума № 1
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""

import array
import random

N = int(input("Введите количество элементов массива "))
M = int(input("Количество элементов в группе "))
K = int(input(" K "))
A = [random.randint(0, 100) for i in range(0, N)]
B = [random.randint(0, 100) for b in range(0, M)]

print(A)
print(B)

A.insert(K, B)
print(A)
