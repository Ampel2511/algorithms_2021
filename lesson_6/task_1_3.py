import memory_profiler


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def fact(n, num=1):
     return num if n == 0 else fact(n-1, num*n)


if __name__ == '__main__':

    res, mem_diff = fact(100)
    print(f"Выполнение заняло {mem_diff} Mib")

# Выполнение заняло 0.1484375 Mib, использование yield значительно экономит память. У меня почему-то всегда выводится
# 0.0, даже когда запускаю код урока. Пробовал получить факториал от 3000, все равно 0.0 было. Вроде все правильно было,
# так и должно быть?
