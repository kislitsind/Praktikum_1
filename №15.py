"""
Имя проекта: №15
Номер версии: 1.0
Имя файла: practicum-1(№15).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 21/11/2020
Дата последней модификации: 21/11/2020
Связанные файлы/пакеты: 
Описание: Решение задач № 14 практикума № 1
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""

import random

X = random.randint (1,54)
print (X)
if X > 36:
    print ("боковое")
else:
    print ("купе")
if X%2 == 0:
    print ("верхнее")
else:
    print ("нижнее")
        
