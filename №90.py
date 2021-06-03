"""
Имя проекта: №90
Номер версии: 1.0
Имя файла: practicum-1(№90).py
Автор: 2020 © Н.Д.Кислицын, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 24/05/2021
Дата последней модификации: 24/05/2021
Описание: 
#версия Python: 3.8
"""

from random import randint
 
 
def print_sum(p):
    print('{} = {}'.format('+'.join(map(str, p)), sum(p)))
 
N = 5
M = 5
 
A = [[randint(1, 9) for _ in range(M)] for _ in range(N)]
print(*A, sep='\n')
 
L = 2
K = 2
 
print()
print(*[[A[r][e] if (r != L and e != K) else 0 for e in range(M)] for r in range(N)], sep='\n')
 
print()
print_sum([c for r in A[:L] for c in r[:K]])
print_sum([c for r in A[:L] for c in r[K+1:]])
print_sum([c for r in A[L+1:] for c in r[:K]])
print_sum([c for r in A[L+1:] for c in r[K+1:]])
