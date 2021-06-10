"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""
from collections import deque
from timeit import timeit


my_list = [i for i in range(10000)]
my_deque = deque([i for i in range(10000)])


def append_list():
    my_list = []
    for i in range(10000):
        my_list.insert(0, i)
    return my_list


def append_deque():
    my_deque = deque()
    for i in range(10000):
        my_deque.appendleft(i)
    return my_deque


def pop_list(my_list):
    for i in range(1000):
        my_list.pop(i)
    return my_list


def pop_deque(my_deque):
    for i in range(1000):
        my_deque.pop()
    return my_deque


print(timeit('append_list()', globals=globals(), number=50))
print(timeit('append_deque()', globals=globals(), number=50))
print(timeit('pop_list(my_list)', globals=globals(), number=9))
print(timeit('pop_deque(my_deque)', globals=globals(), number=9))

# Заполнение очереди гораздо быстрее т.к сложность заполнения списка О(n) против О(1)
# В данном случае операции с очередью немного быстрее, чем со списком
