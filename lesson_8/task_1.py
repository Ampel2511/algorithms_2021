"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""
# саму работу алгоритма я понял, но механику кода не полностью. Поискал в интернете и нашел такой вариант.
# Результаты разные выводятся, по сравнению с реализацией с урока, но я так и не понял почему
import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(words):
    new_list = []
    for symbol, frequency in Counter(words).items():
        new_list.append((frequency, len(new_list), Leaf(symbol)))
    heapq.heapify(new_list)
    count = len(new_list)
    while len(new_list) > 1:
        frequency1, _count1, left = heapq.heappop(new_list)
        frequency2, _count2, right = heapq.heappop(new_list)
        heapq.heappush(new_list, (frequency1 + frequency2, count, Node(left, right)))
        count += 1
    code = {}
    if new_list:
        [(_freq, _count, root)] = new_list
        root.walk(code, "")
    return code


s = "beep boop beer!"
print(' '.join(huffman_encode(s)[n] for n in s))
