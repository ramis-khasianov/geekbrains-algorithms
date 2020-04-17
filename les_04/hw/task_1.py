"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать,
для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""

import random
import timeit
import cProfile
import sys

sys.setrecursionlimit(5001)

"""
Урок 2 Задача 3
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

# для генерации
def get_number(n):
    string = ''
    for i in range(n):
        string = string + str(random.randint(0,9))
    return int(string)


long_100 = get_number(100)
long_200 = get_number(200)
long_500 = get_number(500)

sys.setrecursionlimit(10000)  # исключительно в образовательных целях... )

long_1000 = get_number(1000)
long_2000 = get_number(2000)
long_5000 = get_number(5000)


# 1. Как я решил изначально рекурсией
def reverse_bad_recursion(num):
    num_str = str(num)
    n = 0
    last = ''
    first = ''
    length = len(num_str)
    if length == 1:
        return num_str
    for i in num_str:
        if n == 0:
            first = i
            n = 1
        else:
            last = last + i
    return reverse_bad_recursion(last) + first


print(timeit.timeit('reverse_bad_recursion(long_100)', number=100, globals=globals()))  # 0.04562265798449516
print(timeit.timeit('reverse_bad_recursion(long_200)', number=100, globals=globals()))  # 0.157394367037341
print(timeit.timeit('reverse_bad_recursion(long_500)', number=100, globals=globals()))  # 0.9636170889716595
print(timeit.timeit('reverse_bad_recursion(long_1000)', number=100, globals=globals()))  # 4.03147089201957
print(timeit.timeit('reverse_bad_recursion(long_5000)', number=100, globals=globals()))  # 119.54796384414658

cProfile.run('reverse_bad_recursion(long_100)')  # 100/1    0.000    0.000    0.000    0.000 <input>:2(reverse_bad_recursion)
cProfile.run('reverse_bad_recursion(long_200)')  # 200/1    0.002    0.000    0.002    0.002 <input>:2(reverse_bad_recursion)
cProfile.run('reverse_bad_recursion(long_500)')  # 500/1    0.011    0.000    0.011    0.011 <input>:2(reverse_bad_recursion)
cProfile.run('reverse_bad_recursion(long_1000)')  # 999/1    0.049    0.000    0.049    0.049 <input>:2(reverse_bad_recursion)
cProfile.run('reverse_bad_recursion(long_5000)')  # 4999/1    1.199    0.000    1.199    1.199 <input>:2(reverse_bad_recursion)


# 2. Как вы решили :)

def reverse_correct(num):
    BASE = 10
    result = 0
    while num > 0:
        result = result * BASE + num % BASE
        num = num // BASE
    return result


print(timeit.timeit('reverse_correct(long_100)', number=100, globals=globals()))  # 0.003075686050578952
print(timeit.timeit('reverse_correct(long_200)', number=100, globals=globals()))  # 0.008960746927186847
print(timeit.timeit('reverse_correct(long_500)', number=100, globals=globals()))  # 0.04170881398022175
print(timeit.timeit('reverse_correct(long_1000)', number=100, globals=globals()))  # 0.1509382000658661
print(timeit.timeit('reverse_correct(long_5000)', number=100, globals=globals()))  # 3.46456678211689

cProfile.run('reverse_correct(long_100)')
cProfile.run('reverse_correct(long_200)')
cProfile.run('reverse_correct(long_500)')
cProfile.run('reverse_correct(long_1000)')
cProfile.run('reverse_correct(long_5000)')


# 3. Еще один
def reverse_massive(num):
    num_str = str(num)
    massive = [None] * len(num_str)
    for i, item in enumerate(num_str):
        massive[-i - 1] = item
    return ''.join(massive)


print(timeit.timeit('reverse_massive(long_100)', number=100, globals=globals()))  # 0.001146594062447548
print(timeit.timeit('reverse_massive(long_200)', number=100, globals=globals()))  # 0.002180380979552865
print(timeit.timeit('reverse_massive(long_500)', number=100, globals=globals()))  # 0.005717024905607104
print(timeit.timeit('reverse_massive(long_1000)', number=100, globals=globals()))  # 0.01410221983678639
print(timeit.timeit('reverse_massive(long_5000)', number=100, globals=globals()))  # 0.09146086988039315

cProfile.run('reverse_massive(long_100)')
cProfile.run('reverse_massive(long_200)')
cProfile.run('reverse_massive(long_500)')
cProfile.run('reverse_massive(long_1000)')
cProfile.run('reverse_massive(long_5000)')


# 4. Уже стало интересно
def reverse_indexing(num):
    num_str = str(num)
    result = ''
    for i in range(len(num_str)):
        result = result + num_str[-i - 1]
    return result


print(timeit.timeit('reverse_indexing(long_100)', number=100, globals=globals()))  # 0.0014102288987487555
print(timeit.timeit('reverse_indexing(long_200)', number=100, globals=globals()))  # 0.0027916559483855963
print(timeit.timeit('reverse_indexing(long_500)', number=100, globals=globals()))  # 0.006981656999869301
print(timeit.timeit('reverse_indexing(long_1000)', number=100, globals=globals()))  # 0.017370499903336167
print(timeit.timeit('reverse_indexing(long_5000)', number=100, globals=globals()))  # 0.11528060189448297

cProfile.run('reverse_indexing(long_100)')
cProfile.run('reverse_indexing(long_200)')
cProfile.run('reverse_indexing(long_500)')
cProfile.run('reverse_indexing(long_1000)')
cProfile.run('reverse_indexing(long_5000)')

# Выводы - с небольшим отрывом выигрывает функция 3 - через создание пустого массива и объединения его потом
# в одно число через join
# затем функция 4
# у них обеих линейная зависимость (смотрел на графике построенном в коде ниже)
# Функция 2 показала квадратичную зависимость
# 1ая с рекурсией (которую сдал как домашку) оказалась самой ужасной, как я понял О = 2 ** n
# Как рекурсию тут оптимизировать не понял (не понятно можно ли что-то типа кешировать)

# Вывод - рекурсия в данной задаче зло, массивы - добро.


import pandas as pd
import matplotlib.pyplot as plt

timeit_records = []
for length in range(100, 1100, 100):
    num = get_number(length)
    func_1 = timeit.timeit(f'reverse_bad_recursion({num})', number=100, globals=globals())
    func_2 = timeit.timeit(f'reverse_correct({num})', number=100, globals=globals())
    func_3 = timeit.timeit(f'reverse_massive({num})', number=100, globals=globals())
    func_4 = timeit.timeit(f'reverse_indexing({num})', number=100, globals=globals())
    timeit_records.append({'n': length, 'func_1': func_1, 'func_2': func_2, 'func_3': func_3,'func_4': func_4,})


df = pd.DataFrame(timeit_records)
ax = df.plot(x='n', y='func_4', kind='line')
df.plot(x='n', y='func_3', ax=ax, kind='line')
plt.savefig('les_04/hw/func3-4.png')
df.plot(x='n', y='func_2', ax=ax, kind='line')
plt.savefig('les_04/hw/func2-3-4.png')
df.plot(x='n', y='func_1', ax=ax, kind='line')
plt.savefig('les_04/hw/func1-2-3-4.png')






