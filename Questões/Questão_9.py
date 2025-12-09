def prefix_to_infix(prefix):
    stack = []
    operators = set("+-*/^")

    # ler da direita para esquerda
    for char in reversed(prefix.replace(" ", "")):
        if char not in operators:
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            nova_expr = f"({op1} {char} {op2})"
            stack.append(nova_expr)

    return stack[-1]


def prefix_to_postfix(prefix):
    stack = []
    operators = set("+-*/^")

    for char in reversed(prefix.replace(" ", "")):
        if char not in operators:
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            nova_expr = f"{op1}{op2}{char}"
            stack.append(nova_expr)

    return stack[-1]

expr = "*+AB-CD"

print("Prefixa:   ", expr)
print("Infixa:    ", prefix_to_infix(expr))
print("Pós-fixa:  ", prefix_to_postfix(expr))