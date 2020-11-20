"""
Имя проекта: min_max
Номер версии: 1.0
Имя файла: practicum-1(№9).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 20/11/2020
Дата последней модификации: 20/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач №№ 1-7 практикума № 9
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""

num = int(input("Введите число для проверки:"))
if num % 2 == 1 and num % 7 == 0:
    print("Число", num, "нечетно и кратно 7")
else:
    print("Число не соответствует условиям")
