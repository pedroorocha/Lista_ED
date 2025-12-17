class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Pilha vazia")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None


# Função para definir precedência dos operadores
def precedence(op):
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0


# Aplica um operador a dois operandos
def apply_op(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        # divisão inteira como pedido na maioria dos exercícios
        return a // b
    raise Exception("Operador inválido")


# Avalia uma expressão aritmética
def evaluate(expression):
    values = Stack()      # pilha de números
    ops = Stack()         # pilha de operadores
    i = 0

    while i < len(expression):

        # Ignorar espaços
        if expression[i] == ' ':
            i += 1
            continue

        # Número
        if expression[i].isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.push(num)
            continue

        # Abre parênteses
        elif expression[i] == '(':
            ops.push(expression[i])

        # Fecha parênteses → resolve até encontrar '('
        elif expression[i] == ')':
            while not ops.is_empty() and ops.peek() != '(':
                right = values.pop()
                left = values.pop()
                op = ops.pop()
                values.push(apply_op(left, right, op))
            ops.pop()  # remove '('

        # Operador
        else:
            # Resolver operadores com maior ou igual precedência
            while (not ops.is_empty()
                   and precedence(ops.peek()) >= precedence(expression[i])):
                right = values.pop()
                left = values.pop()
                op = ops.pop()
                values.push(apply_op(left, right, op))

            ops.push(expression[i])

        i += 1

    # Resolver operadores restantes
    while not ops.is_empty():
        right = values.pop()
        left = values.pop()
        op = ops.pop()
        values.push(apply_op(left, right, op))

    return values.pop()

print(evaluate("3 + 4 * 2"))
print(evaluate("(1 + 2) * (3 + 4)"))
print(evaluate("10 + 2 * 6"))
print(evaluate("100 * (2 + 12) / 14"))