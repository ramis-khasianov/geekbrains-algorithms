"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random
import math

SIZE = 10
LOWER_BOUND = 0
UPPER_BOUND = 50
DECIMALS = 2
array = [math.floor(random.uniform(LOWER_BOUND, UPPER_BOUND) * 10**DECIMALS) / 10**DECIMALS for _ in range(10)]
# чтобы 49.99 включилось а 50 нет :(

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    center = len(arr) // 2
    left_arr = merge_sort(arr[:center])
    right_arr = merge_sort(arr[center:])
    return merge_arrays(left_arr, right_arr)


def merge_arrays(left_arr, right_arr):
    left_index = 0
    right_index = 0
    merged_arr = []
    for i in range(len(left_arr) + len(right_arr)):
        if left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] <= right_arr[right_index]:
                merged_arr.append(left_arr[left_index])
                left_index += 1
            else:
                merged_arr.append(right_arr[right_index])
                right_index += 1
        elif left_index == len(left_arr):
            merged_arr.append(right_arr[right_index])
            right_index += 1
        elif right_index == len(right_arr):
            merged_arr.append(left_arr[left_index])
            left_index += 1
    return merged_arr


print(f'Исходный массив: {array}')
print(f'Сортированный массив: {merge_sort(array)}')
