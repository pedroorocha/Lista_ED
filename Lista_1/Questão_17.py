from Questão_12 import Node
def reverse_recursive(head):

    if head is None or head.next is None:
        return head

    new_head = reverse_recursive(head.next)

    head.next.next = head
    head.next = None

    return new_head

n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

new_head = reverse_recursive(n1)

cur = new_head
while cur:
    print(cur.value, end=" → ")
    cur = cur.next