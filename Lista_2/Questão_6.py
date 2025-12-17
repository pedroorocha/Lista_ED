from Questão_1 import LinkedBinaryTree

def print_root_to_leaf_paths(T):

    path = []

    def dfs(p):
        if p is None:
            return

        path.append(p.element())

        # nó folha
        if T.left(p) is None and T.right(p) is None:
            print(" → ".join(map(str, path)))
        else:
            dfs(T.left(p))
            dfs(T.right(p))

        path.pop() 

    dfs(T.root())

T = LinkedBinaryTree()

r = T._add_root(1)

n2 = T._add_left(r, 2)
n3 = T._add_right(r, 3)

n4 = T._add_left(n2, 4)
n5 = T._add_right(n2, 5)
n6 = T._add_left(n3, 6)
n7 = T._add_right(n3, 7)
n8 = T._add_left(n6, 8)
n8 = T._add_right(n7, 9)

print_root_to_leaf_paths(T)
