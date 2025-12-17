from Questão_1 import LinkedBinaryTree

def is_sum_tree(T):

    def check(p):
        if p is None:
            return True, 0

        left = T.left(p)
        right = T.right(p)

        # Nó folha
        if left is None and right is None:
            return True, p.element()

        left_ok, left_sum = check(left)
        right_ok, right_sum = check(right)

        if not left_ok or not right_ok:
            return False, 0

        if p.element() != left_sum + right_sum:
            return False, 0

        return True, p.element() + left_sum + right_sum

    ok, _ = check(T.root())
    return ok

T = LinkedBinaryTree()

r = T._add_root(44)
l = T._add_left(r, 9)
r2 = T._add_right(r, 13)

T._add_left(l, 4)
T._add_right(l, 5)
T._add_left(r2, 6)
T._add_right(r2, 7)

print(is_sum_tree(T))  # True
