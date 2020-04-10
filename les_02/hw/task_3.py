"""
с Рекурсией
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.

"""


# Без квадртных скобок и num_str[0] ересь какая то получилась :)
def reverse(num_str):
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
    return reverse(last) + first


n = input('Введите натуральное число')
rev = reverse(n)
print(f'Обратное число: {rev}')
