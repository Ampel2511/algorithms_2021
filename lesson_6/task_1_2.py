from memory_profiler import profile


@profile
def func_1():
    my_list = []
    for i in range(50000):
        my_list.append(i)
    i = 0
    if len(my_list) % 2 == 0:
        while i < len(my_list):
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            i += 2
    else:
        while i < len(my_list) - 1:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            i += 2
    print(my_list)


func_1()


@profile
def func_1():
    my_list = [i for i in range(50000)]
    i = 0
    if len(my_list) % 2 == 0:
        while i < len(my_list):
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            i += 2
    else:
        while i < len(my_list) - 1:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            i += 2
    print(my_list)
    del my_list


func_1()


# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      4     14.6 MiB     14.6 MiB           1   @profile
#      5                                         def func_1():
#      6     14.6 MiB      0.0 MiB           1       my_list = []
#      7     15.6 MiB      0.0 MiB       50001       for i in range(50000):
#      8     15.6 MiB      1.0 MiB       50000           my_list.append(i)
#      9     15.6 MiB      0.0 MiB           1       i = 0
#     10     15.6 MiB      0.0 MiB           1       if len(my_list) % 2 == 0:
#     11     15.6 MiB      0.0 MiB       25001           while i < len(my_list):
#     12     15.6 MiB      0.0 MiB       25000               my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#     13     15.6 MiB      0.0 MiB       25000               i += 2
#     14                                             else:
#     15                                                 while i < len(my_list) - 1:
#     16                                                     my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#     17                                                     i += 2
#     18     15.7 MiB      0.2 MiB           1       print(my_list)
#
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     24     15.3 MiB     15.3 MiB           1   @profile
#     25                                         def func_1():
#     26     15.8 MiB      0.5 MiB       50003       my_list = [i for i in range(50000)]
#     27     15.8 MiB      0.0 MiB           1       i = 0
#     28     15.8 MiB      0.0 MiB           1       if len(my_list) % 2 == 0:
#     29     15.8 MiB      0.0 MiB       25001           while i < len(my_list):
#     30     15.8 MiB      0.0 MiB       25000               my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#     31     15.8 MiB      0.0 MiB       25000               i += 2
#     32                                             else:
#     33                                                 while i < len(my_list) - 1:
#     34                                                     my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#     35                                                     i += 2
#     36     16.2 MiB      0.5 MiB           1       print(my_list)
#     37     16.0 MiB     -0.2 MiB           1       del my_list

# применение здесь генератора и удаление лишнего массива позволяют сэкономить память

