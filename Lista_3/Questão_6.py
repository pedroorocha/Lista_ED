class AVLRemove:
    class Node:
        def __init__(self, key):
            self.key = key; self.left = None; self.right = None; self.height = 1

    def __init__(self):
        self.root = None

    def _height(self,n): return n.height if n else 0
    def _update(self,n): n.height = 1 + max(self._height(n.left), self._height(n.right))
    def _bf(self,n): return self._height(n.left) - self._height(n.right)

    def _rot_right(self,y):
        x=y.left; T2=x.right
        x.right=y; y.left=T2
        self._update(y); self._update(x)
        return x

    def _rot_left(self,x):
        y=x.right; T2=y.left
        y.left=x; x.right=T2
        self._update(x); self._update(y)
        return y

    def _rebalance_node(self,node):
        self._update(node); b=self._bf(node)
        if b>1:
            if self._bf(node.left) < 0:
                node.left = self._rot_left(node.left)
            return self._rot_right(node)
        if b<-1:
            if self._bf(node.right) > 0:
                node.right = self._rot_right(node.right)
            return self._rot_left(node)
        return node

    def insert(self,key):
        def _ins(n,key):
            if n is None: return AVLRemove.Node(key)
            if key < n.key: n.left = _ins(n.left, key)
            elif key > n.key: n.right = _ins(n.right, key)
            else: return n
            return self._rebalance_node(n)
        self.root = _ins(self.root,key)

    def _min_value_node(self,node):
        current=node
        while current.left: current=current.left
        return current

    def remove(self,key):
        def _remove(n,key):
            if not n: return n
            if key < n.key:
                n.left = _remove(n.left,key)
            elif key > n.key:
                n.right = _remove(n.right,key)
            else:
                if not n.left:
                    return n.right
                elif not n.right:
                    return n.left
                temp = self._min_value_node(n.right)
                n.key = temp.key
                n.right = _remove(n.right, temp.key)
            return self._rebalance_node(n) if n else None
        self.root = _remove(self.root,key)

    def _print(self,n,level=0):
        if not n: return
        self._print(n.right,level+1)
        print("   "*level + str(n.key))
        self._print(n.left,level+1)
    def print_tree(self): self._print(self.root)

keys = [44,17,78,32,50,88,48,62,54]
T = AVLRemove()
for k in keys: T.insert(k)
print("Árvore antes da remoção de 62:")
T.print_tree()
T.remove(62)
print("\nÁrvore depois de remover 62:")
T.print_tree()