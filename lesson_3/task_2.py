"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
import hashlib


def check_password(password, login):
    check_hash_obj = hashlib.sha256('salt'.encode('utf-8') + password.encode('utf-8')).hexdigest()
    with open("passwords.txt") as file:
        for data in file.readlines():
            if data.split()[0] == login:
                if check_hash_obj == data.split()[1]:
                    return print("Пароль верный")
                else:
                    return print("Пароль неверный")
        print(f'Пользователь {login} не найден.')

# user_1 login
# 1111 password


def reg():
    n = input('Для регистрации нажмите 1. Для авторизации нажмите 2. ')
    try:
        if int(n) == 1:
            print(f'{"-"*15} Регистрация {"-"*15}')
            user_name = input('Введите логин: ')
            user_password = input('Введите пароль: ')
            hash_obj = hashlib.sha256('salt'.encode('utf-8') + user_password.encode('utf-8')).hexdigest()
            file = open("passwords.txt", "r")
            lines = file.readlines()
            file.close()
            file = open("passwords.txt", "w")
            for line in lines:
                if line.split()[0] != user_name:
                    file.write(line)
            file.write(f"{user_name} {hash_obj}\n")
            file.close()
            reg()
        elif int(n) == 2:
            print(f'{"-"*15} Авторизация {"-"*15}')
            user_login = input('Введите логин: ')
            password = input('Введите пароль: ')
            check_password(password, user_login)
        else:
            print('Ошибка.')
            reg()
    except ValueError:
        print('Ошибка.')
        reg()


reg()
