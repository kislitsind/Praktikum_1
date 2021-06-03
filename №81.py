"""
Имя проекта: №81
Номер версии: 1.0
Имя файла: practicum-1(№81).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 24/05/2021
Дата последней модификации: 24/05/2021
Описание:Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Все элементы имеют целый тип. Дано целое число H. Определить, какие столбцы имеют хотя бы одно такое число, а какие не имеют.
#версия Python: 3.8
"""


from random import randint
 
number_of_colomn = int(input('Введите N: '))
number_of_row = int(input('Введите M: '))
H = int(input('Введите H: '))
my_array = []
for i in range(number_of_colomn):
    temp=[]
    for j in range(number_of_row):
        n = randint(0,10) 
        temp.append(n)
    my_array.append(temp)
print(my_array)
