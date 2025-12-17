class _Node:
    __slots__ = '_element', '_parent', '_left', '_right'

    def __init__(self, element, parent=None, left=None, right=None):
        self._element = element
        self._parent = parent
        self._left = left
        self._right = right

class LinkedBinaryTree:
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p deve ser um objeto Position")
        if p._container is not self:
            raise ValueError("p não pertence a esta árvore")
        if p._node._parent is p._node:
            raise ValueError("posição inválida")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    def _add_root(self, e):
        if self._root is not None:
            raise ValueError("Raiz já existe")
        self._size = 1
        self._root = _Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Filho esquerdo já existe")
        self._size += 1
        node._left = _Node(e, parent=node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Filho direito já existe")
        self._size += 1
        node._right = _Node(e, parent=node)
        return self._make_position(node._right)

    def replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def attach(self, p, t1, t2):
        node = self._validate(p)

        if not self.is_empty():
            raise ValueError("Árvore não vazia")
        if not isinstance(t1, LinkedBinaryTree) or not isinstance(t2, LinkedBinaryTree):
            raise TypeError("t1 e t2 devem ser LinkedBinaryTree")

        self._size = t1._size + t2._size + 1
        self._root = node

        if t1._root is not None:
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0

        if t2._root is not None:
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    def preorder(self):
        
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def inorder(self):
        """Gera as posições da árvore em percurso inorder."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def postorder(self):
        """Gera as posições da árvore em percurso postorder."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        if self.left(p) is not None:
            for other in self._subtree_preorder(self.left(p)):
                yield other
        if self.right(p) is not None:
            for other in self._subtree_preorder(self.right(p)):
                yield other
    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def _subtree_postorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_postorder(self.left(p)):
                yield other
        if self.right(p) is not None:
            for other in self._subtree_postorder(self.right(p)):
                yield other
        yield p

T = LinkedBinaryTree()

r = T._add_root("A")
b = T._add_left(r, "B")
c = T._add_right(r, "C")
d = T._add_left(b, "D")
e = T._add_right(b, "E")

print("Preorder:")
for p in T.preorder():
    print(p.element(), end=" ")
# A B D E C

print("\nInorder:")
for p in T.inorder():
    print(p.element(), end=" ")
# D B E A C

print("\nPostorder:")
for p in T.postorder():
    print(p.element(), end=" ")
# D E B C A
