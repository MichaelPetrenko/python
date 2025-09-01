from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# bfs = Breadth First Search, breadth first traversal
# Обход бинарного дерева в ширину
def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Обход бинарного дерева в глубину - три метода (Depth First Search)
def dfs_preorder(node):
    if node:
        print(node.value, end=' ')
        dfs_preorder(node.left)
        dfs_preorder(node.right)

def dfs_inorder(node):
    if node:
        dfs_inorder(node.left)
        print(node.value, end=' ')
        dfs_inorder(node.right)

def dfs_postorder(node):
    if node:
        dfs_postorder(node.left)
        dfs_postorder(node.right)
        print(node.value, end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.right.right = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# Пример использования:
bfs(root)
print("")
dfs_preorder(root)
print("")
dfs_inorder(root)
print("")
dfs_postorder(root)
print("")