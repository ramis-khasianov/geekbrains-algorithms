import timeit
import cProfile

# 1 решето
# не понял как сделать без верхнего порога/
def prime_sieve(n, limit_step):
    res_sieve = []
    limit = 0
    while len(res_sieve) < n:
        limit += limit_step
        sieve = [x for x in range(limit)]
        sieve[1] = 0
        for i in range(2, limit):
            if sieve[i] != 0:
                num = i + i
                while num < limit:
                    sieve[num] = 0
                    num += i
        res_sieve = [i for i in sieve if i != 0]
    return res_sieve[n-1]


print(timeit.timeit('prime_sieve(50, 1000)', number=100, globals=globals()))  # 0.026702046001446433
print(timeit.timeit('prime_sieve(100, 1000)', number=100, globals=globals()))  # 0.025399086000106763
print(timeit.timeit('prime_sieve(200, 1000)', number=100, globals=globals()))  # 0.07286456699875998
print(timeit.timeit('prime_sieve(500, 1000)', number=100, globals=globals()))  # 0.25438061600107176
print(timeit.timeit('prime_sieve(1000, 1000)', number=100, globals=globals()))  # 0.93187038600081

print(timeit.timeit('prime_sieve(50, 10000)', number=100, globals=globals()))  # 0.25552500000048894
print(timeit.timeit('prime_sieve(100, 10000)', number=100, globals=globals()))  # 0.26001208900015627
print(timeit.timeit('prime_sieve(200, 10000)', number=100, globals=globals()))  # 0.2534102170011465
print(timeit.timeit('prime_sieve(500, 10000)', number=100, globals=globals()))  # 0.259647725000832
print(timeit.timeit('prime_sieve(1000, 10000)', number=100, globals=globals()))  # 0.25480066100135446



# Ниже кол-во проверок на стоке 9, свидетельство того в какое тысяче нашлось n-ое простое число
cProfile.run('prime_sieve(50)')  # 2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('prime_sieve(100)')  # 2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('prime_sieve(200)')  # 3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('prime_sieve(500)')  # 5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('prime_sieve(1000)')  # 9    0.000    0.000    0.000    0.000 {built-in method builtins.len}


# 2 цикла без решета
def prime(n):
    lst=[]
    i = 1
    while len(lst) < n:
        i += 1
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[n-1]


print(timeit.timeit('prime(50)', number=100, globals=globals()))  # 0.009835660999669926
print(timeit.timeit('prime(100)', number=100, globals=globals()))  # 0.0310674080010358
print(timeit.timeit('prime(200)', number=100, globals=globals()))  # 0.09480422599881422
print(timeit.timeit('prime(500)', number=100, globals=globals()))  # 0.5534500520006986
print(timeit.timeit('prime(1000)', number=100, globals=globals()))  # 2.176128692999555

cProfile.run('prime(50)')  # 229    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('prime(100)')  # 541    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('prime(200)')  # 1223    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('prime(500)')  # 3571    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('prime(1000)')  # 7919    0.000    0.000    0.000    0.000 {built-in method builtins.len}

# 3 регулярка которую нашел на stackoverflow
# получился совсем кошмар

import re

def prime_reg(n):
    lst = []
    i = 1
    while len(lst) < n:
        i += 1
        if re.match(r'^1?$|^(11+?)\1+$', '1' * i) == None:
            lst.append(i)
    return lst[n-1]


print(timeit.timeit('prime_reg(50)', number=100, globals=globals()))  # 0.16464726099911786
print(timeit.timeit('prime_reg(100)', number=100, globals=globals()))  # 0.9524522160008928
print(timeit.timeit('prime_reg(200)', number=100, globals=globals()))  # 6.382174356998803

# Дальше лучше не пробовать, 1000 я не дождался
# print(timeit.timeit('prime_reg(500)', number=100, globals=globals()))  # 99.62938594000116
# print(timeit.timeit('prime_reg(1000)', number=100, globals=globals()))  #

cProfile.run('prime_reg(50)')  # 229    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('prime_reg(100)')  # 541    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('prime_reg(200)')  # 1223    0.000    0.000    0.000    0.000 {built-in method builtins.len}




"""
Выводы:
Не все решения на stack overflow нормальные
Видимо поскольку расстояние между простыми числами становится все больше и больше их поиск через перебор будет
всегда иметь близкую к квадратичной зависимости

У решета будет константная сложность если простое число находится в пределах порога указанного для функции

"""