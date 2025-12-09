from Questão_1 import ArrayStack

def transfer(S: ArrayStack, T: ArrayStack):
   
    while not S.is_empty():
        T.push(S.pop())

S = ArrayStack()
T = ArrayStack()

S.push(1)
S.push(2)
S.push(3)
print(S)
transfer(S, T)

print(T)
