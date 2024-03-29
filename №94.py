"""
Имя проекта: №94
Номер версии: 1.0
Имя файла: practicum-1(№94).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 24/05/2021
Дата последней модификации: 24/05/2021
Описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Исключить из матрицы столбец с номером K. Сомкнуть столбцы матрицы.
#версия Python: 3.8
"""

import numpy as np

N = 4
M = 5
K = np.random.randint(1, 3)

V = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}\n".format(V))
print("K = " + str(K))
V = np.delete(V, (K-1), axis=1)
print("Новая матрица:\r\n{}\n".format(V))
