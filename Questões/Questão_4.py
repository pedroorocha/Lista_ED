import sys

from Questão_1 import ArrayStack
def remove_all(S):
    if S.is_empty():
        return
    else:
        S.pop()
    remove_all(S)

S = ArrayStack()
S.push(1)
S.push(2)
S.push(3)
print(S.is_empty())
remove_all(S)

print(S.is_empty())