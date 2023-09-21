'''
1. Реализуем структуру бинарного дерева.
2. Для бинарного дерева характерно наличии двух потомков, где левый меньше родителя, а правый – больше.
3. Для реализации можно использовать как и простое числовое дерево, так и обобщенный тип.
Учитывая, что мы строим именно бинарное дерево, то при использовании обобщенных типов убедитесь,
что значение поддерживает сравнение (интерфейс Comparable)

4. Реализуем алгоритм поиска элементов по дереву (поиск в глубину).
5. Для работы с бинарным деревом необходимо как минимум организовать метод поиска.

6. Добавить подсчет количества элементов, вывод всего дерева на экран, удаление элемента.
'''

class Node:
    # класс узел бинарного дерева
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        res = f'значение нашего узла: {self.value}'
        if self.left:
            res += f' значение левого: {self.left.value}'
        if self.right:
            res += f' значение правого: {self.right.value}'
        return res

class BinaryTree:
    # класс Бинарное дерево
    def __init__(self, root_value):
        self.root = Node(root_value)

    def add(self, value):
        """Функция add используется для добавления узла в дерево
        Attributes
        ----------
        value : 
            значение добавляемого узла
        parent :
            родительский узел
        """
        res = self.search(self.root, value)

        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print("Хорош")

    def search(self, node, value, parent=None):
        """Функция search используется для поиска узла в дереве по значению
        Attributes
        ----------
        node : Node
            головной узел дерева
        value : 
            значение искомого узла
        parent :
            родительский узел
        """
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)

    def counting_node(self, node, count=0):
        """Функция counting_node используется для подсчета количества узлов в дереве
        Attributes
        ----------
        node : Node
            головной узел дерева
        count : int
            счетчик узлов
        """
        if node is None:
            return count
        return self.counting_node(node.left, self.counting_node(node.right, count + 1))

    def delete_node(self, node, value):
        ''' Функция delete_node используется для удаления узла из дерева
        Attributes
        ----------
        node : Node
            головной узел дерева
        value : int
            значение узла дерева, которого необходимо удалить
        '''
        if not node: 
            return node
        if node.value > value: 
            node.left = self.delete_node(node.left, value)
        elif node.value < value: 
            node.right= self.delete_node(node.right, value)
        else: 
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            temp_value = node.right
            min_value = temp_value.value
            while temp_value.left:
                temp_value = temp_value.left
                min_value = temp_value.value
            node.value = min_value 
            node.right = self.delete_node(node.right,node.value)
        return node
    
    def print_bt(self, node):
        """Функция print_bt используется для вывода всего дерева на экран
        Attributes
        ----------
        node : Node
            головной узел дерева
        """
        if node:
            print(node)
            self.print_bt(node.left)
            self.print_bt(node.right)

bt = BinaryTree(5)
bt.add(10)
bt.add(15)
bt.add(3)
bt.add(4)
bt.add(6)

print("Количество записей в дереве = ",bt.counting_node(bt.root))
bt.print_bt(bt.root)

val_searche_node = int(input('Введите значение узла, который надо найти: '))
print(bt.search(bt.root, val_searche_node)[1])

val_del_node = int(input('Введите значение узла, который надо удалить: '))
result = bt.delete_node(bt.root, val_del_node)
print(f"После удаления узла {val_del_node}:")
bt.print_bt(result)
