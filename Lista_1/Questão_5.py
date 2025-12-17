from Questão_1 import ArrayStack
def reverse_list(L):
    S = ArrayStack()

    for item in L:
        S.push(item)

    idx = 0
    while not S.is_empty():
        L[idx] = S.pop()
        idx += 1

lista = [10, 20, 30, 40]
reverse_list(lista)
print(lista)