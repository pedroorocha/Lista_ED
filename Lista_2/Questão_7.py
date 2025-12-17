from Questão_1 import LinkedBinaryTree

def print_ancestors(T, target):
    def dfs(p):
        if p is None:
            return False

        if p.element() == target:
            return True

        if dfs(T.left(p)) or dfs(T.right(p)):
            print(p.element(), end=" ")
            return True

        return False

    dfs(T.root())
    print()

T = LinkedBinaryTree()

r = T._add_root(1)
n2 = T._add_left(r, 2)
n3 = T._add_right(r, 3)

T._add_left(n2, 4)
T._add_right(n2, 5)

n6 = T._add_left(n3, 6)
n7 = T._add_right(n3, 7)

T._add_left(n7, 8)
T._add_right(n7, 9)

print("Ancestrais do nó 9:")
print_ancestors(T, 9)

print("Ancestrais do nó 6:")
print_ancestors(T, 6)

print("Ancestrais do nó 5:")
print_ancestors(T, 5)
