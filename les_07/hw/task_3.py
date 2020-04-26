"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""

import random

m = 5
array = [random.randint(0, 100) for _ in range(2 * m + 1)]

# Для тестирования
import statistics
median_for_test = statistics.median(array)


def heapify(arr, length, initial_head_index):
    largest_number_index = initial_head_index
    left_child_index = 2 * initial_head_index + 1
    right_child_index = 2 * initial_head_index+ 2

    if left_child_index < length and arr[left_child_index] > arr[largest_number_index]:
        largest_number_index = left_child_index

    if right_child_index < length and arr[right_child_index] > arr[largest_number_index]:
        largest_number_index = right_child_index

    if initial_head_index != largest_number_index:
        arr[initial_head_index], arr[largest_number_index] = arr[largest_number_index], arr[initial_head_index]
        heapify(arr, length, largest_number_index)


def heap_sort(arr):
    length = len(arr)

    for i in range(length, -1, -1):
        heapify(arr, length, i)

    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


print(f'Исходный массив: {array}')
heap_sort(array)
print(f'Сортированный массив: {array}')


def heap_median(arr):
    heap_sort(arr)
    return arr[len(arr) // 2]


print(f'Медиана через модуль statistics: {median_for_test}')
print(f'Медиана через пирамидальную сортировку: {heap_median(array)}')
