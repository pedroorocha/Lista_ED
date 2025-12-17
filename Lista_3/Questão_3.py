class RedBlackTreeMap:

    class _Node:
        __slots__ = '_key', '_value', '_parent', '_left', '_right', '_color'

        RED = 0
        BLACK = 1

        def __init__(self, key, value, parent=None, color=RED):
            self._key = key
            self._value = value
            self._parent = parent
            self._left = None
            self._right = None
            self._color = color
            
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _is_red(self, node):
        return node is not None and node._color == self._Node.RED

    def _is_black(self, node):
        return node is None or node._color == self._Node.BLACK

    def _set_red(self, node):
        if node:
            node._color = self._Node.RED

    def _set_black(self, node):
        if node:
            node._color = self._Node.BLACK

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

    def _fix_insert(self, node):
        while node != self._root and self._is_red(node._parent):
            parent = node._parent
            grandparent = parent._parent

            if parent == grandparent._left:
                uncle = grandparent._right

                if self._is_red(uncle):
                    self._set_black(parent)
                    self._set_black(uncle)
                    self._set_red(grandparent)
                    node = grandparent
                else:
                    if node == parent._right:
                        node = parent
                        self._rotate_left(node)
                    self._set_black(parent)
                    self._set_red(grandparent)
                    self._rotate_right(grandparent)
            else:
                uncle = grandparent._left

                if self._is_red(uncle):
                    self._set_black(parent)
                    self._set_black(uncle)
                    self._set_red(grandparent)
                    node = grandparent
                else:
                    if node == parent._left:
                        node = parent
                        self._rotate_right(node)
                    self._set_black(parent)
                    self._set_red(grandparent)
                    self._rotate_left(grandparent)

        self._set_black(self._root)

    def _subtree_search(self, node, key):
        if node is None or key == node._key:
            return node
        elif key < node._key:
            return self._subtree_search(node._left, key)
        else:
            return self._subtree_search(node._right, key)

    def put(self, key, value):
        if self._root is None:
            self._root = self._Node(key, value, color=self._Node.BLACK)
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
        self._fix_insert(new_node)

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

        self._size -= 1
        if self._root:
            self._set_black(self._root)

        return removed_value

    def inorder(self):
        def subtree_inorder(node):
            if node:
                yield from subtree_inorder(node._left)
                yield (node._key, node._value)
                yield from subtree_inorder(node._right)

        yield from subtree_inorder(self._root)


T = RedBlackTreeMap()

for k in [50, 30, 70, 20, 40, 60, 80]:
    T.put(k, str(k))

print("Inorder (Red-Black):")
for k, v in T.inorder():
    print(k, end=" ")
