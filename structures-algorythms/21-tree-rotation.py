class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 1

    def right_rotate(y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(get_height(y.left), get_height(y.right)) + 1
        x.height = max(get_height(x.left), get_height(x.right)) + 1
        return x

    def left_rotate(x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(get_height(x.left), get_height(x.right)) + 1
        y.height = max(get_height(y.left), get_height(y.right)) + 1
        return y

    def get_height(node):
        if not node:
            return 0
        return node.height

