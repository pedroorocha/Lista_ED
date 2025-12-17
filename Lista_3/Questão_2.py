class AVLTreeMap:

    class _Node:
        __slots__ = '_key', '_value', '_parent', '_left', '_right', '_height'

        def __init__(self, key, value, parent=None):
            self._key = key
            self._value = value
            self._parent = parent
            self._left = None
            self._right = None
            self._height = 0

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
    
    def _height(self, node):
        return node._height if node else -1

    def _recompute_height(self, node):
        node._height = 1 + max(self._height(node._left),
                                self._height(node._right))

    def _balance_factor(self, node):
        return self._height(node._left) - self._height(node._right)

    def _is_balanced(self, node):
        return abs(self._balance_factor(node)) <= 1

    def _rotate_left(self, z):
        y = z._right
        z._right = y._left
        if y._left:
            y._left._parent = z

        y._parent = z._parent
        if z._parent is None:
            self._root = y
        elif z == z._parent._left:
            z._parent._left = y
        else:
            z._parent._right = y

        y._left = z
        z._parent = y

        self._recompute_height(z)
        self._recompute_height(y)

    def _rotate_right(self, z):
        y = z._left
        z._left = y._right
        if y._right:
            y._right._parent = z

        y._parent = z._parent
        if z._parent is None:
            self._root = y
        elif z == z._parent._right:
            z._parent._right = y
        else:
            z._parent._left = y

        y._right = z
        z._parent = y

        self._recompute_height(z)
        self._recompute_height(y)

    def _rebalance(self, node):
        while node:
            old_height = node._height
            self._recompute_height(node)

            if not self._is_balanced(node):
                if self._balance_factor(node) > 0:
                    if self._balance_factor(node._left) < 0:
                        self._rotate_left(node._left)
                    self._rotate_right(node)
                else:
                    if self._balance_factor(node._right) > 0:
                        self._rotate_right(node._right)
                    self._rotate_left(node)

            if node._height == old_height:
                node = node._parent
            else:
                node = node._parent

    def _subtree_search(self, node, key):
        if node is None or key == node._key:
            return node
        elif key < node._key:
            return self._subtree_search(node._left, key)
        else:
            return self._subtree_search(node._right, key)

    def put(self, key, value):
        if self._root is None:
            self._root = self._Node(key, value)
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

        new_node = self._Node(key, value, parent)
        if key < parent._key:
            parent._left = new_node
        else:
            parent._right = new_node

        self._size += 1
        self._rebalance(parent)

    def _subtree_minimum(self, node):
        while node._left:
            node = node._left
        return node

    def delete(self, key):
        node = self._subtree_search(self._root, key)
        if node is None:
            return None

        removed_value = node._value

        if node._left and node._right:
            successor = self._subtree_minimum(node._right)
            node._key, node._value = successor._key, successor._value
            node = successor

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
            self._rebalance(parent)

        self._size -= 1
        return removed_value

    def inorder(self):
        def subtree_inorder(node):
            if node:
                yield from subtree_inorder(node._left)
                yield (node._key, node._value)
                yield from subtree_inorder(node._right)

        yield from subtree_inorder(self._root)

T = AVLTreeMap()

for k in [50, 30, 70, 20, 40, 60, 80]:
    T.put(k, str(k))

print("Inorder (AVL):")
for k, v in T.inorder():
    print(k, end=" ")
