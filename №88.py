"""
Имя проекта: №88
Номер версии: 1.0
Имя файла: practicum-1(№88).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 24/05/2021
Дата последней модификации: 24/05/2021
Описание:
#версия Python: 3.8
"""

import numpy as np

N = 4
M = 5

V = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}\n".format(V))

col = [i % 2 for i in np.sum(V, axis=1)]
V = np.insert(V, M, col, axis=1)

print("Новая матрица:\r\n{}\n".format(V))
