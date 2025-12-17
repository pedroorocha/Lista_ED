from Questão_12 import Node

class LinkedList:
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

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

def separar_lista(lista):
    positivos = LinkedList()
    negativos = LinkedList()

    current = lista.head

    while current:
        if current.value >= 0:
            positivos.append(current.value)
        else:
            negativos.append(current.value)

        current = current.next

    return positivos, negativos

lista = LinkedList()
lista.append(3)
lista.append(-2)
lista.append(10)
lista.append(-7)
lista.append(5)

print("Lista original:")
lista.print_list()

positivos, negativos = separar_lista(lista)

print("Lista de positivos:")
positivos.print_list()

print("Lista de negativos:")
negativos.print_list()
