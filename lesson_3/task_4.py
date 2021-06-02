"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib

url_dict = {}


def ckeck_url(url_dict):
    print(f'Ссылки в кэше:')
    for one_url in url_dict.keys():
        print(one_url)
    url = input('Введите ссылку: ')
    if url in url_dict.keys():
        print(f'{url} уже в кэше. \n'
              f'Хеш - {url_dict[url]}')
        ckeck_url(url_dict)
    else:
        print(f'{url} не в кэше. Сейчас добавим.')
        hash_obj = hashlib.sha256('salt'.encode('utf-8') + url.encode('utf-8')).hexdigest()
        url_dict[url] = hash_obj
        print(f'{url} добавлен в кэш.')
        ckeck_url(url_dict)


ckeck_url(url_dict)
