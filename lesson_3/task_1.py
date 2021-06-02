"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time


def memorize(func):
    def calculate_time():
        start_val = time.time()
        result = func()
        end_val = time.time()
        return result, end_val - start_val
    return calculate_time


@memorize
def my_list():
    new_list = [n for n in range(0, 1000000)]  # (n)
    return new_list


@memorize
def my_dict():
    new_dict = {n: n for n in range(0, 1000000)}  # (n)
    return new_dict

# в этой вариации у меня время генерации словаря в среднем в 1.5 - 2 раза дольше


print(my_list()[1])
print(my_dict()[1])


def list_func(new_list: list):
    start_val = time.time()
    a = len(new_list)  # (1)
    del new_list[0]  # (n)  в списке это линейная сложность, а в словарях константная? в таблице так
    new_list.pop(1)  # (1)
    i = 0  # (1)
    for n in new_list:  # (n)
        i = n  # (1)
    second_list = new_list.copy()  # (n)
    new_list.clear()  # (1)
    end_val = time.time()
    return end_val - start_val


def dict_func(new_dict: dict):
    start_val = time.time()
    a = len(new_dict)  # (1)
    del new_dict[0]  # (1)
    new_dict.pop(1)  # (1)
    i = 0  # (1)
    for key, value in new_dict.items():  # (n)
        i = value  # (1)
    second_dict = new_dict.copy()  # (n)
    new_dict.clear()  # (1)
    end_val = time.time()
    return end_val - start_val
# у меня операции со списком выполняются в 2.5 раза быстрее по сравнению с операциями для словаря
# полагаю все что связано со словарями выполняется дольше из-за наличия связки ключ: значение?

print(list_func(my_list()[0]))
print(dict_func(my_dict()[0]))
