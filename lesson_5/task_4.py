"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


from timeit import timeit
from collections import OrderedDict

my_dict = {}
my_ordered_dict = OrderedDict()


def fill_dict(my_dict):
    for i in range(100000):
        my_dict[i] = i


def fill_ordered_dict(my_ordered_dict):
    for i in range(100000):
        my_ordered_dict[i] = i


def get_value_dict(my_dict):
    n = 0
    for key, value in my_dict.items():
        n = value


def get_value_ordered_dict(my_ordered_dict):
    n = 0
    for key, value in my_ordered_dict.items():
        n = value


print(timeit('fill_dict(my_dict)', globals=globals(), number=50))
print(timeit('fill_ordered_dict(my_ordered_dict)', globals=globals(), number=50))
print(timeit('get_value_dict(my_dict)', globals=globals(), number=50))
print(timeit('get_value_ordered_dict(my_ordered_dict)', globals=globals(), number=50))

# Все операции с обычными словарями выполняются быстрее, чем с OrderedDict и в Python 3.6 обычный словарь
# стал поддерживать запоминание порядка добавления, поэтому использовать OrderedDict вместо
# обычного словаря смысла нет. Если только в специфических случаях необходимы его функции
