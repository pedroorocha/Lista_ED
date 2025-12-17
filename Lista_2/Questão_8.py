class Node:
    def __init__(self, e, left=None, right=None):
        self.element = e
        self.left = left
        self.right = right

def substituir_por_soma(node):
    if node is None:
        return 0

    L = substituir_por_soma(node.left)
    R = substituir_por_soma(node.right)

    old = node.element
    node.element = L + R
    return old + node.element

n7 = Node(7)
n8 = Node(8)
n4 = Node(4)

n2 = Node(2, right=n4)

n5 = Node(5, left=n7, right=n8)
n6 = Node(6)
n3 = Node(3, left=n5, right=n6)

root = Node(1, left=n2, right=n3)

substituir_por_soma(root)
print("Raiz agora vale:", root.element)