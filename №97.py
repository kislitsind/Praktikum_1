"""
Имя проекта: №97
Номер версии: 1.0
Имя файла: practicum-1(№97).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 24/05/2021
Дата последней модификации: 24/05/2021
Описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Добавить к элементам каждой строки такой новый элемент, чтобы сумма положительных элементов стала бы равна модулю суммы отрицательных элементов. Результат оформить в виде матрицы из N строк и M + 1 столбцов.
#версия Python: 3.8
"""

import numpy as np

N = 6
M = 2
K = np.random.randint(0 , 10)

A = np.random.randint(low=-4, high=9, size= (N, M))
print("Матрица:\r\n{}\n".format( A))

M_n = np.sum(A, axis= 1 ) * (- 1)
A = np.hstack((A, M_n.reshape(- 1, 1)))

print("Новая матрица:\r\n{}\n".format( A))
