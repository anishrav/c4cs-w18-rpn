#!/usr/bin/env python3

import operator
import logging
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
    '!': math.factorial
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            try: 
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
            except IndexError:
                result = function(arg2)
                stack.append(result)
            except ZeroDivisionError:
                print('Divide by zero error.')
                raise TypeError
            logger.debug(stack)
        print(stack)
    if len(stack) != 1:
        raise TypeError
    return stack.pop()
def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()