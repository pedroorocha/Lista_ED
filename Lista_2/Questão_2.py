class ArrayBinaryTree:

    class Position:
        def __init__(self, container, index):
            self._container = container
            self._index = index

        def element(self):
            return self._container._data[self._index]

        def __eq__(self, other):
            return (
                type(other) is type(self) and
                other._index == self._index and
                other._container is self._container
            )

    def __init__(self, capacity=100):
        self._data = [None] * capacity
        self._size = 0
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p deve ser uma Position")
        if p._container is not self:
            raise ValueError("p não pertence a esta árvore")
        if p._index >= len(self._data):
            raise ValueError("posição inválida")
        return p._index

    def _make_position(self, index):
        if index is None or self._data[index] is None:
            return None
        return self.Position(self, index)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def root(self):
        return self._make_position(0)

    def parent(self, p):
        i = self._validate(p)
        if i == 0:
            return None
        return self._make_position((i - 1) // 2)

    def left(self, p):
        i = self._validate(p)
        return self._make_position(2 * i + 1)

    def right(self, p):
        i = self._validate(p)
        return self._make_position(2 * i + 2)

    def num_children(self, p):
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1
        return count
    def _add_root(self, e):
        if self._size != 0:
            raise ValueError("Raiz já existe")
        self._data[0] = e
        self._size = 1
        return self._make_position(0)

    def _add_left(self, p, e):
        i = self._validate(p)
        left = 2 * i + 1

        if left >= len(self._data):
            raise IndexError("Capacidade insuficiente")
        if self._data[left] is not None:
            raise ValueError("Filho esquerdo já existe")

        self._data[left] = e
        self._size += 1
        return self._make_position(left)

    def _add_right(self, p, e):
        i = self._validate(p)
        right = 2 * i + 2

        if right >= len(self._data):
            raise IndexError("Capacidade insuficiente")
        if self._data[right] is not None:
            raise ValueError("Filho direito já existe")

        self._data[right] = e
        self._size += 1
        return self._make_position(right)

    def replace(self, p, e):
        i = self._validate(p)
        old = self._data[i]
        self._data[i] = e
        return old

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

T = ArrayBinaryTree(capacity=50)

r = T._add_root("z")
b = T._add_left(r, "e")
c = T._add_right(r, "l")
d = T._add_left(b, "D")
e = T._add_right(b, "E")

print(T.root().element())     # A
print(T.left(r).element())    # B
print(T.right(r).element())   # C
print(T.left(b).element())    # D
print(T.right(b).element())   # E
