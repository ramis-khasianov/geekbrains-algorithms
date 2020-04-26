"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
"""
import random

SIZE = 10
LOWER_BOUND = -100
UPPER_BOUND = 100
array = [random.randint(LOWER_BOUND, UPPER_BOUND-1) for _ in range(10)]


def bubble_reversed_sort(arr):
    n = 1
    needs_sorting = True
    while n < len(arr) and needs_sorting:
        needs_sorting = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                needs_sorting = True
        print(arr)
        n += 1


print(f'Исходный целочисленный массив: {array}')
bubble_reversed_sort(array)
print(f'Сортированный по убыванию массив: {array}')
