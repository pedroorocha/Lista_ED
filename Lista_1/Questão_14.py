from Questão_12 import Node

def concatenate(L, M):
    if L is None:
        return M

    current = L

    while current.next is not None:
        current = current.next

    current.next = M

    return L

n3 = Node(3)
n2 = Node(2, n3)
n1 = Node(1, n2)
L = n1

m2 = Node(5)
m1 = Node(4, m2)
M = m1

L = concatenate(L, M)

cur = L
while cur:
    print(cur.value, end=" → ")
    cur = cur.next
