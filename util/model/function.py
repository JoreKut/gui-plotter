import re

from util.service.calculator import calculate


def function_wrapper(f: str) -> str:
    return re.sub(r'(\d)x', r'\1*x', f.replace(',', '.'))


class Function:

    def __init__(self, expression: str):
        self.expression = function_wrapper(expression)

    def value_at(self, value: float) -> float:
        return calculate(self.expression.replace('x', str(value)))
