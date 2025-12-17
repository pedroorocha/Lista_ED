from Questão_1 import LinkedBinaryTree

def are_identical(T1, T2):

    def check(p1, p2):
        if p1 is None and p2 is None:
            return True
        if p1 is None or p2 is None:
            return False
        if p1.element() != p2.element():
            return False

        return (check(T1.left(p1), T2.left(p2)) and
                check(T1.right(p1), T2.right(p2)))

    return check(T1.root(), T2.root())

T1 = LinkedBinaryTree()
r1 = T1._add_root(1)
T1._add_left(r1, 2)
T1._add_right(r1, 3)

T2 = LinkedBinaryTree()
r2 = T2._add_root(1)
T2._add_left(r2, 2)
T2._add_right(r2, 3)

print(are_identical(T1, T2))  # True
