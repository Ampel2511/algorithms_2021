"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib


def sub_string(s):
    my_set = []
    n = len(s)
    step_cut = 1
    while n > 1:
        cut = step_cut
        for i in range(0, n):
            my_set.append(s[i:cut])
            cut += 1
        step_cut += 1
        n -= 1
    my_set = set(my_set)
    my_dict = dict()
    for string in my_set:
        hash_obj = hashlib.md5((string).encode('utf-8'))
        hash = hash_obj.hexdigest()
        my_dict[string] = hash
    for key, hash in my_dict.items():
        print(key, hash)


user_str = input('Введите строку: ')
sub_string(user_str)
