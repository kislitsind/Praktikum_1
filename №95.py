"""
Имя проекта: №95
Номер версии: 1.0
Имя файла: practicum-1(№95).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 24/05/2021
Дата последней модификации: 24/05/2021
Описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Добавить к матрице столбец чисел и вставить его под номером K.
#версия Python: 3.8
"""

import numpy as np

N = 4
M = 5
H = np.random.randint(1, 3)

V = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}\n".format(V))

bool = V == H
col_sum = np.sum(bool, axis=1)

print("Строки в которых встречается значение {}:".format(H))
print(np.argwhere(col_sum).flatten())
print("Строки в которых нет значения {}:".format(H))
print(np.argwhere(col_sum == 0).flatten())
