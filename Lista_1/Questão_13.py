from Questão_12 import Node
def find_penultimate(head):
    if head is None or head.next is None:
        return None

    current = head
    while current.next.next is not None:
        current = current.next

    return current

n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

pen = find_penultimate(n1)
print(pen.value)