#Arraystack
class ArrayStack:
    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._top = -1
        self._capacity = capacity

    def is_empty(self):
        return self._top == -1

    def is_full(self):
        return self._top == self._capacity - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow")
        self._top += 1
        self._data[self._top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        value = self._data[self._top]
        self._data[self._top] = None
        self._top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[self._top]

    def size(self):
        return self._top + 1

    def __str__(self):
        return str(self._data[:self._top + 1])

#ArrayQueue
class ArrayQueue:
    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._capacity = capacity
        self._size = 0
        self._front = 0
        self._rear = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")

        self._data[self._rear] = value
        self._rear = (self._rear + 1) % self._capacity
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
        items = []
        index = self._front
        for _ in range(self._size):
            items.append(self._data[index])
            index = (index + 1) % self._capacity
        return str(items)

#ArrayDeque
class ArrayDeque:
    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._capacity = capacity
        self._size = 0
        self._front = 0
        self._rear = -1

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def add_first(self, value):
        if self.is_full():
            raise OverflowError("Deque is full")

        self._front = (self._front - 1) % self._capacity
        self._data[self._front] = value
        self._size += 1

    def add_last(self, value):
        if self.is_full():
            raise OverflowError("Deque is full")

        self._rear = (self._rear + 1) % self._capacity
        self._data[self._rear] = value
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")

        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return value

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")

        value = self._data[self._rear]
        self._data[self._rear] = None
        self._rear = (self._rear - 1) % self._capacity
        self._size -= 1
        return value

    def first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._data[self._rear]

    def size(self):
        return self._size

    def __str__(self):
        items = []
        index = self._front
        for _ in range(self._size):
            items.append(self._data[index])
            index = (index + 1) % self._capacity
        return str(items)
