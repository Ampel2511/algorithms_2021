"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
import inspect


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # суть в том, чтобы в зависимости от того, больше ли новое значение текущего узла или нет, получать правого/левого потомка
        # и потом получать также потомка этого потомка и так до тех пор, пока в потомке не окажется None, затем просто
        # вставка в опредленную часть. А если запрос вставить влево, а значение больше, то просто вызывает метод вставки
        # вправо, и наоборот
        if new_node < self.root:
            if self.left_child == None:
                self.left_child = BinaryTree(new_node)
            else:
                child = self.get_left_child()
                root = None
                if new_node >= child.root:
                    second_child = child.get_right_child()
                    if second_child == None:
                        root = child
                    while second_child != None:
                        if new_node >= second_child.root:
                            root = second_child
                            second_child = second_child.get_right_child()
                        else:
                            root = second_child
                            second_child = second_child.get_left_child()
                    if new_node >= root.root:
                        root.right_child = BinaryTree(new_node)
                    else:
                        root.left_child = BinaryTree(new_node)
                else:
                    second_child = child.get_left_child()
                    while second_child != None:
                        if new_node < second_child.root:
                            root = second_child
                            second_child = second_child.get_left_child()
                        else:
                            root = second_child
                            second_child = second_child.get_right_child()
                    if new_node >= root.root:
                        root.right_child = BinaryTree(new_node)
                    else:
                        root.left_child = BinaryTree(new_node)
        else:
            self.insert_right(new_node)

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node >= self.root:
            if self.right_child == None:
                self.right_child = BinaryTree(new_node)
            else:
                child = self.get_right_child()
                root = None
                if new_node >= child.root:
                    second_child = child.get_right_child()
                    if second_child == None:
                        root = child
                    while second_child != None:
                        if new_node >= second_child.root:
                            root = second_child
                            second_child = second_child.get_right_child()
                        else:
                            root = second_child
                            second_child = second_child.get_left_child()
                    if new_node >= root.root:
                        root.right_child = BinaryTree(new_node)
                    else:
                        root.left_child = BinaryTree(new_node)
                else:
                    second_child = child.get_left_child()
                    while second_child != None:
                        if new_node < second_child.root:
                            root = second_child
                            second_child = second_child.get_left_child()
                        else:
                            root = second_child
                            second_child = second_child.get_right_child()
                    if new_node >= root.root:
                        root.right_child = BinaryTree(new_node)
                    else:
                        root.left_child = BinaryTree(new_node)
        else:
            self.insert_left(new_node)

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def get_nodes(self):
        try:
            for i in inspect.getmembers(self):
                if not i[0].startswith('_'):
                    if not inspect.ismethod(i[1]):
                        print(i[1].root)
        except:
            pass


r = BinaryTree(8)
r.insert_left(4)
r.insert_right(12)
print(f'Узел - {r.root}')
print('Потомки: левый и правый')
r.get_nodes()
print('-'*30)

r.get_left_child().insert_right(6)
r.get_left_child().insert_left(2)
print(f'Узел - {r.get_left_child().root}')
print('Потомки: левый и правый')
r.get_left_child().get_nodes()
print('-'*30)

r.get_right_child().insert_right(14)
r.get_right_child().insert_left(10)
print(f'Узел - {r.get_right_child().root}')
print('Потомки: левый и правый')
r.get_right_child().get_nodes()
print('-'*30)
# сначала я подумал, что можно просто отказать в вставке если новое значение не подходит под правила. Но потом я решил
# сделать так, чтобы скрипт вставлял в другую сторону, если не подходило по правилам. В итоге спустя кучу "а что если в дереве уже есть..."
# я написал так, чтобы скрипт сам искал удобное место для вставки, независимо от того, куда я указываю вставить значение.
r.get_left_child().get_right_child().insert_left(5)
r.insert_left(7)
print(f'Узел - {r.get_left_child().get_right_child().root}')
print('Потомки: левый и правый')
r.get_left_child().get_right_child().get_nodes()
print('-'*30)
# в итоге даже неважно какой метод использовать, он все равно отработает как надо
r.get_right_child().get_left_child().insert_left(9)
r.insert_right(11)
print(f'Узел - {r.get_right_child().get_left_child().root}')
print('Потомки: левый и правый')
r.get_right_child().get_left_child().get_nodes()
print('-'*30)
# и даже неважно, чтобы в том узле, куда должно попасть значение, был потомок, чтобы по нему найти место.
# Реализовал дерево из конспекта
r.insert_left(13)
r.insert_left(15)
print(f'Узел - {r.get_right_child().get_right_child().root}')
print('Потомки: левый и правый')
r.get_right_child().get_right_child().get_nodes()
print('-'*30)

r.insert_right(1)
r.insert_left(3)
print(f'Узел - {r.get_left_child().get_left_child().root}')
print('Потомки: левый и правый')
r.get_left_child().get_left_child().get_nodes()
print('-'*30)
# вроде все должно работать нормально
