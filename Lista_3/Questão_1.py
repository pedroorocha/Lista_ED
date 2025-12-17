class _Node:
    __slots__ = '_key', '_value', '_parent', '_left', '_right', 'height'

    def __init__(self, key, value, parent=None):
            self._key = key
            self._value = value
            self._parent = parent
            self._left = None
            self._right = None
            self._height = 0

class TreeMap:

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def key(self):
            return self._node._key

        def value(self):
            return self._node._value

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def root(self):
        return self.Position(self, self._root) if self._root else None
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("Posição inválida")
        if p._container is not self:
            raise ValueError("Posição não pertence a esta árvore")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node else None

    def _subtree_search(self, node, key):
        if node is None or key == node._key:
            return node
        elif key < node._key:
            return self._subtree_search(node._left, key)
        else:
            return self._subtree_search(node._right, key)

    def get(self, key):
        node = self._subtree_search(self._root, key)
        if node is None:
            return None
        return node._value

    def put(self, key, value):
        if self._root is None:
            self._root = _Node(key, value)
            self._size = 1
            return

        node = self._root
        parent = None

        while node:
            parent = node
            if key == node._key:
                node._value = value
                return
            elif key < node._key:
                node = node._left
            else:
                node = node._right

        new_node = _Node(key, value, parent)
        if key < parent._key:
            parent._left = new_node
        else:
            parent._right = new_node

        self._size += 1

    def _subtree_minimum(self, node):
        while node._left:
            node = node._left
        return node

    def _subtree_maximum(self, node):
        while node._right:
            node = node._right
        return node

    def first(self):
        if self._root is None:
            return None
        return self._make_position(self._subtree_minimum(self._root))

    def last(self):
        if self._root is None:
            return None
        return self._make_position(self._subtree_maximum(self._root))

    def _successor(self, node):
        if node._right:
            return self._subtree_minimum(node._right)

        parent = node._parent
        while parent and node == parent._right:
            node = parent
            parent = parent._parent
        return parent

    def delete(self, key):
        node = self._subtree_search(self._root, key)
        if node is None:
            return None

        removed_value = node._value

        # Caso 1: dois filhos
        if node._left and node._right:
            successor = self._subtree_minimum(node._right)
            node._key, node._value = successor._key, successor._value
            node = successor

        # Caso 2 e 3: zero ou um filho
        child = node._left if node._left else node._right

        if child:
            child._parent = node._parent

        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node == parent._left:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        return removed_value

    def inorder(self):
        def subtree_inorder(node):
            if node:
                yield from subtree_inorder(node._left)
                yield (node._key, node._value)
                yield from subtree_inorder(node._right)

        yield from subtree_inorder(self._root)

