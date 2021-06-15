"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_1(lst_obj):
    n = 1
    reverse = True
    for i in range(len(lst_obj)-n):
        if lst_obj[-i-1] < lst_obj[-i-2]:
            reverse = False
            break
    if reverse:
        lst_obj.reverse()
        return lst_obj
    n = len(lst_obj)
    already_sorted = True
    for i in range(n):
        for j in range(n - i - 1):
            if lst_obj[j] < lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
                already_sorted = False
        if already_sorted:
            break
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
# замеры 10
print(orig_list)
print(bubble_sort_1(orig_list[:]))
print('До оптимизации:')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print('После оптимизации:')
print(
    timeit.timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(orig_list)
print(bubble_sort_1(orig_list[:]))
print('До оптимизации:')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print('После оптимизации:')
print(
    timeit.timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(orig_list)
print(bubble_sort_1(orig_list[:]))
# print('До оптимизации:')
# print(
#     timeit.timeit(
#         "bubble_sort(orig_list[:])",
#         globals=globals(),
#         number=1000))
print('После оптимизации:')
print(
    timeit.timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

# здесь я добавил возможность определить, если в списке значения находятся в отсортированном или
# обратном порядке и заменил while на итерацию, т.к наскоько я знаю, вложенная итерация быстрее чем while.
# после оптимизации скорость возросла, особенно ощутимо при 1000 элементах в массиве (320 против 150-200) 
