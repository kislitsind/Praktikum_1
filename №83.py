"""
Имя проекта: №83
Номер версии: 1.0
Имя файла: practicum-1(№83).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 24/05/2021
Дата последней модификации: 24/05/2021
Описание:
#версия Python: 3.8
"""

k = [int(el) for el in input().split()]
print('Start:')
import random
matrix = [[random.randint(0, 30) for _ in range(6)] for _ in range(6)]
max_len = max([len(str(e)) for r in matrix for e in r])
for row in matrix:
  print(*list(map('{{:>{length}}}'.format(length=max_len).format, row)))
 
l = int(input('Chose number L: '))
matrix.insert(l-1,k)
print('Finish:')
max_len = max([len(str(e)) for r in matrix for e in r])
for row in matrix:
   print(*list(map('{{:>{length}}}'.format(length=max_len).format, row)))
