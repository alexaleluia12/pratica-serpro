

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_left(self, node_left):
        self.left = node_left

    def set_right(self, node_right):
        self.right = node_right

    def is_leaf(self):
        return self.right is None and self.left is None

class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value)
        self.size = 1

    def add(self, value):
        current_node = self.root
        stop = False
        self.size += 1
        while not stop:
            vr = current_node.value
            if value > vr:
                if current_node.right is None:
                    current_node.set_right(Node(value))
                    stop = True
                else:
                    current_node = current_node.right
            else:
                if current_node.left is None:
                    current_node.set_left(Node(value))
                    stop = True
                else:
                    current_node = current_node.left

    def inner_pre_ordem(self, node):
        if node is None:
            return
        print(node.value, end=',')

        self.inner_pre_ordem(node.left)
        self.inner_pre_ordem(node.right)


    def print_pre_ordem(self):
        """Raiz, Esquerda, Direita (raiz primeiro)"""
        print('Pre Ordem: ', end='')
        curr = self.root
        if curr is not None:
            self.inner_pre_ordem(curr)
        print()


    def inner_pos_ordem(self, node):
        if node is None:
            return
        if node.is_leaf():
            print(node.value, end=',')
        else:
            self.inner_pos_ordem(node.left)
            self.inner_pos_ordem(node.right)
            print(node.value, end=',')


    def print_pos_ordem(self):
        """Esquerda, Direita, Raiz (raiz por ultimo)"""
        print('Pos Ordem: ', end='')
        self.inner_pos_ordem(self.root)
        print()

    def inner_em_ordem(self, node):
        if node is None:
            return None
        if node.is_leaf():
            print(node.value, end=',')
            return None
        else:
            self.inner_em_ordem(node.left)
            print(node.value, end=',')
            self.inner_em_ordem(node.right)


    def print_em_ordem(self):
        "Esquerda, Raiz, Direita (resultado em ordem crescente)"
        print('Em Ordem: ', end='')
        self.inner_em_ordem(self.root)
        print()

if __name__ == '__main__':
    """
                6
            3       7
         2     5         9
    1
    """
    myt = Tree(6)
    myt.add(3)
    myt.add(7)
    myt.add(2)
    myt.add(9)
    myt.add(5)
    myt.add(1)


    print('Tree size', myt.size)
    myt.print_pre_ordem()
    myt.print_em_ordem()
    myt.print_pos_ordem()
