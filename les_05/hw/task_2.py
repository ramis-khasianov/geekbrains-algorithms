"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их
как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
"""

from collections import deque

input_1 = deque(input('Введите первое шеснадцатиричное число').upper())
input_2 = deque(input('Введите второе шеснадцатиричное число').upper())

hex_str = '0123456789ABCDEF'
hex_val = {item: i for i, item in enumerate(hex_str)}


def sum_hex(n1, n2):
    rem = 0
    result = deque()
    while True:
        if n1:
            v1 = n1.pop()
        else:
            v1 = '0'
        if n2:
            v2 = n2.pop()
        else:
            v2 = '0'

        if (hex_val[v1] + hex_val[v2] + rem) == 0:
            break
        val = (hex_val[v1] + hex_val[v2] + rem) % 16
        rem = (hex_val[v1] + hex_val[v2] + rem) // 16
        result.appendleft(hex_str[val])
    return result


print(sum_hex(input_1, input_2))

