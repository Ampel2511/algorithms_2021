"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
from timeit import timeit
import cProfile


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    enter_num = list(str(enter_num))
    enter_num.reverse()
    return ''.join(enter_num)


i = 123456789

print(timeit('revers_1(i)', globals=globals()))
print('-'*30)
print(timeit('revers_2(i)', globals=globals()))
print('-'*30)
print(timeit('revers_3(i)', globals=globals()))
print('-'*30)
print(timeit('revers_4(i)', globals=globals()))
print('-'*30)

cProfile.run('revers_1(i)')
cProfile.run('revers_2(i)')
cProfile.run('revers_3(i)')
cProfile.run('revers_4(i)')
# срез и join гораздо быстрее, чем рекурсия и цикл т.к арифметические операции замедляют работу и встроенные функции
# отрабатывают быстрее
# и не совсем понял как здесь сравнить результаты cprofile, если он только 1 раз вызывает, а 1 вызов выполняется мгновенно.