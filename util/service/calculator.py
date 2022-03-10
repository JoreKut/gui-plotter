import math

operations = {
    '(': -1,
    ')': 1,
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
    '^': 4
}


def is_sign(ch: chr) -> bool:
    return ch in operations.keys()


def is_bracket(ch: chr) -> bool:
    return ch == '(' or ch == ')'


def is_num(ch: chr) -> bool:
    return ch in '0123456789.'


def priority_of(ch: chr) -> int:
    return operations.get(ch)


def is_priority_reduction(sequence: list, next_char: chr) -> bool:
    return len(sequence) > 0 and priority_of(sequence[-1]) >= priority_of(next_char)


def is_empty(num: str) -> bool:
    return num == ''


def is_trigonometrical_function(ch: chr) -> bool:
    return ch in 'sincostgctg'


def separate_trigonometrical_function(sequence: str, cursor: int) -> (str, int):
    trigonometrical_function = ''
    bracket_count = 0
    while is_trigonometrical_function(sequence[cursor]):
        trigonometrical_function += sequence[cursor]
        cursor += 1

    inner_expression = ''
    while cursor < len(sequence) and (bracket_count > 0 or inner_expression == ''):
        if sequence[cursor] == '(':
            bracket_count += 1
        elif sequence[cursor] == ')':
            bracket_count -= 1

        inner_expression += sequence[cursor]

        cursor += 1

    cursor -= 1

    value_param = calculate(inner_expression)
    return str(calc_trigonometrical_function(trigonometrical_function, value_param)), cursor


def calc_trigonometrical_function(function: str, param: float) -> float:
    if function == 'tg':
        return math.tan(param)
    if function == 'ctg':
        return 1 / math.tan(param)
    if function == 'sin':
        return math.sin(param)
    if function == 'cos':
        return math.cos(param)


def calculate(expression: str) -> float:
    nums_stack = []
    operation_stack = []
    cur_num = ''

    i = -1
    size = len(expression) - 1
    while i < size:
        i += 1
        el = expression[i]

        if is_sign(el):
            # case when '-' stay at the start of a sequence
            if el == '-' and (i == 0 or is_sign(expression[i - 1])):
                cur_num += el
                continue
            # case when opening bracket stay at the start of an expression  Exp:(a+b)*c...
            if not is_empty(cur_num):
                nums_stack.append(float(cur_num))

            cur_num = ''
            while el != '(' and is_priority_reduction(operation_stack, el):
                fusion(nums_stack, operation_stack)

            if el == ')':
                operation_stack.pop()
            else:
                operation_stack.append(el)

        elif is_num(el):
            cur_num += el
        elif is_trigonometrical_function(el):
            cur_num, i = separate_trigonometrical_function(expression, i)

    if not is_empty(cur_num):
        nums_stack.append(float(cur_num))

    while len(operation_stack) > 0:
        fusion(nums_stack, operation_stack)

    return nums_stack.pop()


def fusion(nums_stack: list, operation_stack: list):
    n2 = nums_stack.pop()
    n1 = nums_stack.pop()
    operation = operation_stack.pop()

    if operation == '+':
        nums_stack.append(n1 + n2)
    if operation == '-':
        nums_stack.append(n1 - n2)
    if operation == '*':
        nums_stack.append(n1 * n2)
    if operation == '/':
        try:
            nums_stack.append(n1 / n2)
        except ZeroDivisionError:
            if n1 > 0:
                nums_stack.append(float('inf'))
            else:
                nums_stack.append(float('-inf'))
    if operation == '^':
        nums_stack.append(pow(n1, n2))
