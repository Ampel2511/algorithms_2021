"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import random

for j in (50, 500, 1000, 5000, 10000):
    lst = random.sample(range(-100000, 100000), j)

print('min func')
print(min(lst))


def min_1(list_obj):
    min_obj = list_obj[0]  # (2)
    for n in list_obj:  # (n)
        if min_obj > n:  # (1)
            min_obj = n  # (1)
    return min_obj  # (1)
# T(n)= 3 + 2n
# O(n)


def min_2(list_obj):
    min_obj = 0  # (1)
    for n in list_obj:  # (n)
        for i in list_obj:  # (n)
            if i <= n <= min_obj:  # (2)
                min_obj = n  # (1)
    return min_obj  # (1)
# T(n)= 2 + 3n**2
# O(n**2)


print('my func')
print(min_1(lst))
print(min_2(lst))

