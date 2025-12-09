from Questão_12 import Node
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.next)

n3 = Node(30)
n2 = Node(20, n3)
n1 = Node(10, n2)

print(count_nodes(n1))