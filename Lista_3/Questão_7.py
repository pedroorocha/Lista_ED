RED = True
BLACK = False

class RBTree2:
    class Node:
        def __init__(self, key, value=None, color=RED):
            self.key = key; self.value = value
            self.left = None; self.right = None; self.color = color

    def __init__(self):
        self.root = None

    def _is_red(self,node): return node is not None and node.color==RED

    def _rotate_left(self,h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        return x

    def _rotate_right(self,h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x

    def _flip_colors(self,h):
        h.color = RED
        if h.left: h.left.color = BLACK
        if h.right: h.right.color = BLACK

    def insert(self,key,value=None):
        def _ins(h,key,value):
            if h is None: return RBTree2.Node(key,value,RED)
            if key < h.key: h.left = _ins(h.left,key,value)
            elif key > h.key: h.right = _ins(h.right,key,value)
            else: h.value = value

            if self._is_red(h.right) and not self._is_red(h.left): h = self._rotate_left(h)
            if self._is_red(h.left) and self._is_red(h.left.left): h = self._rotate_right(h)
            if self._is_red(h.left) and self._is_red(h.right): self._flip_colors(h)
            return h
        self.root = _ins(self.root,key,value)
        if self.root: self.root.color = BLACK

    def _print(self,node,level=0):
        if not node: return
        self._print(node.right,level+1)
        c = "R" if node.color==RED else "B"
        print("   "*level + f"{node.key}({c})")
        self._print(node.left,level+1)

    def print_tree(self): self._print(self.root)

keys = [5,16,22,45,2,10,18,30,50,12,1]
T = RBTree2()
for k in keys:
    T.insert(k,k)
    print(f"\nApós inserir {k}:")
    T.print_tree()
print("\nÁrvore final:")
T.print_tree()