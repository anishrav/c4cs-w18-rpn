#!/usr/bin/env python3

import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
    '^': operator.pow
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            try: 
                result = function(arg1, arg2)
                stack.append(result)
            except ZeroDivisionError:
                print('Divide by zero error.')
                raise TypeError
        print(stack)
    if len(stack) != 1:
        raise TypeError
    return stack.pop()
def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()