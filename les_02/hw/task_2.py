"""
Ссылка на диаграммы: https://drive.google.com/file/d/1B2q2n9RmcxcWxFLvkmxZ2j_YyMJxMWdZ/view?usp=sharing

Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

n = input('Введите натуральное число')

odd_count = 0
even_count = 0
for i in n:
    i = int(i)
    rem = i % 2
    if rem == 0:
        even_count += 1
    else:
        odd_count += 1

print(f'Четных чисел: {even_count}, Нечетных числе: {odd_count}')