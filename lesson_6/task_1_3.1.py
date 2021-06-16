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
def fact(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
        yield num


if __name__ == '__main__':

    my_generator, mem_diff = fact(3000)
    for i in my_generator:
        print(i)

    print(f"Выполнение заняло {mem_diff} Mib")
