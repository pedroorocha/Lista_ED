from Questão_1 import ArrayStack
from Questão_1 import ArrayQueue
def is_palindrome(text):
    stack = ArrayStack()
    queue = ArrayQueue()

    text = text.replace(" ", "").lower()


    for char in text:
        stack.push(char)
        queue.enqueue(char)

    while not stack.is_empty():
        if stack.pop() != queue.dequeue():
            return False

    return True

s = "arara"
print(is_palindrome(s))

s = "radar"
print(is_palindrome(s))

s = "python"
print(is_palindrome(s))
