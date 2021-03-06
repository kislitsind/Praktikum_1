"""
Имя проекта: №25
Номер версии: 1.0
Имя файла: practicum-1(№25).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 26/11/2020
Дата последней модификации: 26/11/2020
Дано вещественное число A. Вычислить f(A),если f(x) = x^2+4x+5, при x<=2;в противном случае f(x)=1/x^2+4x+5
Описание: Решение задач № 25 практикума № 1
#версия Python: 3.6
"""

"""
Оригинал публикации: Практикум №1 - набиваем руку (Бизнес-информатика 2020)
"""

a = float(input("Введите число А:"))
x = a
if x <= 2:
    fx = x**2 + 4*x + 5
    print("x <= 2; f(a) =:", fx)
else:
    fx = 1 / (x**2 + 4*x + 5)
    print("x > 2; f(a) =:", fx)
