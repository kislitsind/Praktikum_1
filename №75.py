"""
Имя проекта: №75
Номер версии: 1.0
Имя файла: practicum-1(№75).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 31/03/2021
Дата последней модификации: 31/03/2021
Описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Определить, сколько отрицательных элементов содержится в каждом столбце и в каждой строке матрицы. Результат оформить в виде матрицы из N + 1 строк и M + 1 столбцов.
#версия Python: 3.8
"""

import random

N = 7
M = 5

L = 3
K = 2


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(-9, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)

l_zeros = 0
k_zeros = 0


i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        if A[i][j] == 0:
            if i < L:
                l_zeros += 1

            if j < K:
                k_zeros += 1
        j += 1

    i += 1

print("В верхних %s строках содержится %s нулей" % (L, l_zeros))
print("В левых %s столбцах содержится %s нулей" % (K, k_zeros))
