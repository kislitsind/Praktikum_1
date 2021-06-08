"""
Имя проекта: №86
Номер версии: 1.0
Имя файла: practicum-1(№86).py
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

V = np.random.randint(low=-10, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(V))

a = b = np.fliplr(V).diagonal(1)
a_prod = a.prod()
print("Элементы которые выше побочной диагонали: \n" + str(a) + "\nИх сумма = " + str(a_prod))
b = np.fliplr(V).diagonal(-1)
b_prod = b.prod()
print("Элементы которые ниже побочной диагонали: \n" + str(b) + "\nИх сумма = " + str(b_prod))
