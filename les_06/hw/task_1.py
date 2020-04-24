"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

Урок 3 Задача 4: Определить, какое число в массиве встречается чаще всего.
"""
import sys
from collections import Counter
import random

# Сделал функцию которую потом накидывал на locals() внутри функции
def count_memory(locals):
    total_memory = 0
    # print('*' * 50)
    for var in locals:
        # print(f'type: {type(locals[var])} - var: {locals[var]} - size: {sys.getsizeof(locals[var])}')
        var_memory = sys.getsizeof(locals[var])
        if hasattr(locals[var], '__iter__'):
            if hasattr(locals[var], 'items'):
                for key, value in locals[var].items():
                    # print(f'dict elements - {key}: {sys.getsizeof(key)}, {value}: {sys.getsizeof(value)}')
                    var_memory = var_memory + sys.getsizeof(key) + sys.getsizeof(value)
            elif not isinstance(locals[var], str):
                for item in locals[var]:
                    # print(f'massive items - {item}: {sys.getsizeof(item)}')
                    var_memory = var_memory + sys.getsizeof(item)
        total_memory += var_memory
    # print(f'Total memory: {total_memory}')
    return total_memory


def max_count_1(array):
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    print(f'Объем памяти переменных функции: {count_memory(locals())}')
    return num


def max_count_2(array):
    my_counter = Counter(array)
    print(f'Объем памяти переменных функции: {count_memory(locals())}')
    return my_counter.most_common(1)[0][0]


def max_count_3(array):
    max_count = 0
    most_common_item = array[0]
    array_tupple = tuple(array)

    for i in array_tupple:
        if array.count(i) > max_count:
            most_common_item = i
            max_count = array.count(most_common_item)
    print(f'Объем памяти переменных функции: {count_memory(locals())}')
    return most_common_item

# у меня 64-битная macOS Catalina

SIZE = 10
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE // 1.5) for _ in range(SIZE)]
print(f'Изначальный массив : {array}')

# array = [5, 5, 6, 4, 0, 5, 6, 6, 1, 0]

print(f'Результат: {max_count_1(array)}')  # 612
print(f'Результат: {max_count_2(array)}')  # 1012
print(f'Результат: {max_count_3(array)}')  # 960

SIZE = 100
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE // 1.5) for _ in range(SIZE)]
print(f'Изначальный массив : {array}')

print(f'Результат: {max_count_1(array)}')  # 3860
print(f'Результат: {max_count_2(array)}')  # 8768
print(f'Результат: {max_count_3(array)}')  # 7460

"""
Выводы:
Алгоритм Вашего решения самый эффективный по памяти (но по асимптотике хуже чем Counter или Tuple)
На размер памяти влияют верхний и нижний пороги (чем больше 0 в массиве тем меньше памяти например)
Коллекция Counter ест больше всего памяти но зато по быстродействию и асимптотике чемпион


"""

"""
# Ниже замерял асимптотику (на момент замера print убирал из функции) График тоже в рипозитории

import pandas as pd
import matplotlib.pyplot as plt
import timeit

timeit_records = []
for size in range(100, 1001, 100):
    array = [random.randint(MIN_ITEM, size // 1.5) for _ in range(size)]
    func_1 = timeit.timeit(f'max_count_1({array})', number=100, globals=globals())
    func_2 = timeit.timeit(f'max_count_2({array})', number=100, globals=globals())
    func_3 = timeit.timeit(f'max_count_3({array})', number=100, globals=globals())
    timeit_records.append({'n': len(array), 'func_1': func_1, 'func_2': func_2, 'func_3': func_3})


df = pd.DataFrame(timeit_records)
ax = df.plot(x='n', y='func_1', kind='line')
df.plot(x='n', y='func_2', ax=ax, kind='line')
df.plot(x='n', y='func_3', ax=ax, kind='line')
plt.savefig('les_06/hw/func_comp.png')
"""






