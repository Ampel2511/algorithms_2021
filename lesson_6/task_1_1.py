"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from pympler import asizeof


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname}\n"
              f"Должность: {self.position}")

    def get_total_income(self):
        print(f"Доход сотрудника: {self._income['wage'] + self._income['bonus']}")


worker_1 = Position("Иван", "Иванов", "дворник", 20000, 5000)
print(asizeof.asizeof(worker_1))


class Worker:
    __slots__ = ['name', 'surname', 'position', '_income']

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname}\n"
              f"Должность: {self.position}")

    def get_total_income(self):
        print(f"Доход сотрудника: {self._income['wage'] + self._income['bonus']}")


worker_2 = Position("Иван", "Иванов", "дворник", 20000, 5000)
print(asizeof.asizeof(worker_2))


# использование слотов для хранения атрибутов класса позволяет сэкономить память: у меня 608 против 488



