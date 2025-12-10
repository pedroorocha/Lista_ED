from Questão_1 import ArrayStack
def remove_all(s : ArrayStack):
    if s.is_empty():
        return
    s.pop()
    remove_all(s)

S = ArrayStack()
S.push(1)
S.push(2)
S.push(3)
print(S.is_empty())
remove_all(S)

print(S.is_empty())