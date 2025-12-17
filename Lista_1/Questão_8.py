def bem_formada(expr):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}

    for char in expr:
        if char in '([{':
            pilha.append(char)

        elif char in ')]}':
            if not pilha:
                return False
            topo = pilha.pop()
            if topo != pares[char]:
                return False

    return len(pilha) == 0

print(bem_formada("(2 + 3) * (5 - 1)"))
print(bem_formada("((2 + 3) * (5 - 1)"))
print(bem_formada("(a + b]"))
print(bem_formada("([2 + 3] * {5 - 1})"))