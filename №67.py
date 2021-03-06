"""
Имя проекта: №67
Номер версии: 1.0
Имя файла: practicum-1(№67).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 03/03/2021
Дата последней модификации: 03/03/2021
Описание:Для вводимых чисел определить процент положительных и отрицательных чисел. При вводе числа −65432 закончить работу.
#версия Python: 3.6
"""

import random

N = 2  # строк
M = 3  # столбцов


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def listsum(list):
    sum = 0
    for element in list:
        sum += element

    return sum


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

tmp = list(zip(*A))

max_sum = 0
index_column_max_sum = 0

i = 0
while i < len(tmp):
    column = tmp[i]
    current_list_sum = listsum(column)
    if current_list_sum > max_sum:
        max_sum = current_list_sum
        index_column_max_sum = i

    i += 1

print("Матрица:")
print_matrix(A)
print("Cтолбец для которого сумма абсолютных значений элементов максимальна:",
      index_column_max_sum)
print("Наибольший элемент этого столбца:", max(tmp[index_column_max_sum]))
