class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (4 * level) + prefix + str(node.key))
        print_tree(node.left, level + 1, "L--- ")
        print_tree(node.right, level + 1, "R--- ")

bst = BinarySearchTree()
keys = [30, 40, 24, 58, 48, 26, 11, 13]

for k in keys:
    print(f"\nInserindo {k}:")
    bst.insert(k)
    print_tree(bst.root)
