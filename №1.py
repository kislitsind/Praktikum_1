"""
Имя проекта: min_max
Номер версии: 1.0
Имя файла: practicum-1(№2).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Нарисуйте блок-схему к следующей задаче: Преобразовать дату в «компьютерном» представлении (системную дату) в «российский» формат, 
т.е. день/месяц/год (например, 17/05/2009).
Описание: Решение задач № 1-7 практикума № 3
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""

T="2009-06-15"
date=T.split ("-")
print (date)
['2009', '06', '15']
print (date [2] + "." + date [1] + "." + date[0])





