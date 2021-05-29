"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def count_numbers(n, even=0, odd=0):
    try:
        if type(n) == int or int(n):
            n = int(n)
            if n == 0:
                return print(f'Четные: {even}, Нечетные: {odd}')
            numb = n % 10
            if numb % 2 == 0:
                even += 1
            else:
                odd += 1
            count_numbers(n//10, even, odd)
    except:
        print("Вы ввели строку. Введите число")


count_numbers('634634234')
count_numbers('esa64s')
count_numbers(6478769)
