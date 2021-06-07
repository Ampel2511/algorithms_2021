"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, n in enumerate(nums) if n % 2 == 0]


Numbers = [i for i in range(1000)]
print(timeit('func_1(Numbers)', globals=globals(), number=1000))
print(timeit('func_2(Numbers)', globals=globals(), number=1000))
print('-'*30)

Numbers = [i for i in range(10000)]
print(timeit('func_1(Numbers)', globals=globals(), number=1000))
print(timeit('func_2(Numbers)', globals=globals(), number=1000))
print('-'*30)

Numbers = [i for i in range(100000)]
print(timeit('func_1(Numbers)', globals=globals(), number=1000))
print(timeit('func_2(Numbers)', globals=globals(), number=1000))
print('-'*30)


#  списковые включения работают быстрее, чем итераторы
