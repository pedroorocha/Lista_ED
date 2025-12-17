class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, value):
        new_node = Node(value, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._top.value

    def size(self):
        return self._size

    def __str__(self):
        temp = self._top
        result = []
        while temp:
            result.append(temp.value)
            temp = temp.next
        return str(result)

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedQueue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self._front = new_node
        else:
            self._rear.next = new_node
        self._rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self._front.value
        self._front = self._front.next
        self._size -= 1
        if self.is_empty():
            self._rear = None
        return value

    def first(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._front.value

    def size(self):
        return self._size

    def __str__(self):
        temp = self._front
        result = []
        while temp:
            result.append(temp.value)
            temp = temp.next
        return str(result)


class CircularQueue:
    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._size = 0
        self._front = 0
        self._capacity = capacity

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        avail = (self._front + self._size) % self._capacity
        self._data[avail] = value
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return value

    def first(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[self._front]

    def size(self):
        return self._size

    def __str__(self):
        result = []
        idx = self._front
        for _ in range(self._size):
            result.append(self._data[idx])
            idx = (idx + 1) % self._capacity
        return str(result)

class DNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedDeque:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, value, predecessor, successor):
        """Insere um nó entre predecessor e successor"""
        new_node = DNode(value, predecessor, successor)
        if predecessor is None:          # Inserindo no início
            self._front = new_node
        else:
            predecessor.next = new_node
        
        if successor is None:            # Inserindo no final
            self._rear = new_node
        else:
            successor.prev = new_node

        self._size += 1
        return new_node

    def add_first(self, value):
        self._insert_between(value, None, self._front)

    def add_last(self, value):
        self._insert_between(value, self._rear, None)

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        value = self._front.value
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        else:
            self._front.prev = None
        self._size -= 1
        return value

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        value = self._rear.value
        self._rear = self._rear.prev
        if self._rear is None:
            self._front = None
        else:
            self._rear.next = None
        self._size -= 1
        return value

    def first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._front.value

    def last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._rear.value

    def size(self):
        return self._size

    def __str__(self):
        temp = self._front
        result = []
        while temp:
            result.append(temp.value)
            temp = temp.next
        return str(result)
