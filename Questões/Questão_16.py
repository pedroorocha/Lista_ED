from Questão_12 import Node
def count_circular(head):
    if head is None:
        return 0

    count = 1
    current = head.next

    while current is not None and current != head:
        count += 1
        current = current.next

    return count

n3 = Node(3)
n2 = Node(2, n3)
n1 = Node(1, n2)
n3.next = n1  # FECHANDO O CICLO

print(count_circular(n1))