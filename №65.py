"""
Имя проекта: №65
Номер версии: 1.0
Имя файла: practicum-1(№65).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 03/03/2021
Дата последней модификации: 03/03/2021
Описание:Вводятся положительные числа. Определить сумму чисел, делящихся на положительное число B нацело. При вводе отрицательного числа закончить работу.
#версия Python: 3.6
"""

import re

list_numbers = []

B = 5
sum = 0

while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if number < 0:
        break

    if number % B == 0:
        sum += number

print("Сумма:", sum)
