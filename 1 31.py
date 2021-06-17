"""
Имя проекта: 1/31
Номер версии: 1.0
Имя файла: practicum-1().py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 03/03/2021
Дата последней модификации: 03/03/2021
Описание:Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Найти наибольший элемент столбца матрицы A, для которого сумма абсолютных значений элементов максимальна.
#версия Python: 3.6
"""

import numpy as np
print("Введите число строк:")
n = int(input())
print("Введите число столбцов:")
m = int(input())
arr = np.random.randint(10,20,(n,m))
arrt = np.transpose(arr)
arrabs = np.abs(arrt)
sums = np.sum(arrabs, axis=1)
max = np.argmax(sums)
m = np.max(arrt[max])
print(m)
