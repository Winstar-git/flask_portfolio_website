import re

_PREC = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
_RIGHT_ASSOC = {'^'}


def tokenize(expr: str):
    return re.findall(r"\d+\.\d+|\d+|[A-Za-z_]\w*|[+\-*/^()]", expr)


def infix_to_postfix(expression: str) -> str:
    tokens = tokenize(expression)
    out = []
    stack = []

    for t in tokens:
        # operand: number or identifier
        if re.fullmatch(r"\d+\.\d+|\d+|[A-Za-z_]\w*", t):
            out.append(t)
        elif t in _PREC:
            while stack and stack[-1] in _PREC:
                top = stack[-1]
                if ((t in _RIGHT_ASSOC and _PREC[top] > _PREC[t]) or
                        (t not in _RIGHT_ASSOC and _PREC[top] >= _PREC[t])):
                    out.append(stack.pop())
                else:
                    break
            stack.append(t)
        elif t == '(':
            stack.append(t)
        elif t == ')':
            while stack and stack[-1] != '(':
                out.append(stack.pop())
            if not stack or stack[-1] != '(':
                raise ValueError('Mismatched parentheses')
            stack.pop()
        else:
            raise ValueError(f'Unknown token: {t}')

    while stack:
        s = stack.pop()
        if s in '()':
            raise ValueError('Mismatched parentheses')
        out.append(s)

    return ' '.join(out)


if __name__ == '__main__':
    # quick CLI tests
    samples = [
        'a + b * c',
        '(a + b) * c',
        '3 + 4 * 2 / (1 - 5) ^ 2 ^ 3',
        'a ^ b ^ c',
        '12 + 34 * var1'
    ]
    for s in samples:
        print('infix:', s)
        print('postfix:', infix_to_postfix(s))
        print()


