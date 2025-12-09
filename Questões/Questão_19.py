from Questão_12 import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value, end=" <-> ")
            curr = curr.next
        print("None")

    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev

    def remove_duplicates(self):
        seen = set()
        curr = self.head

        while curr:
            if curr.value in seen:
                nxt = curr.next
                self.remove_node(curr)
                curr = nxt
            else:
                seen.add(curr.value)
                curr = curr.next

lista = DoublyLinkedList()

valores = [5, 2, 8, 5, 2, 9, 8, 1]
for v in valores:
    lista.append(v)

print("Lista original:")
lista.print_list()

lista.remove_duplicates()

print("Lista sem duplicados:")
lista.print_list()
