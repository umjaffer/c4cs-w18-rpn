#!/usr/bin/env python3

import operator
import logging
import math

logging.basicConfig(level=logging.INFO)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    if len(myarg.split()) == 2 and myarg.split()[-1] == '!':
        for token in myarg.split():
            try:
                token = int(token)
                stack.append(token)
            except ValueError:
                arg1 = stack.pop()
                result = math.factorial(arg1)
                stack.append(result)
            logging.debug(stack)
    elif myarg.split()[-1] == 'rotate':
        for token in myarg.split():
            try:
                token = int(token)
                stack.append(token)
            except ValueError:
                result = stack[::-1]
            logging.debug(stack)
        return result
    elif myarg.split()[-1] == 'copy':
        for token in myarg.split():
            try:
                token = int(token)
                stack.append(token)
            except ValueError:
                stack = stack[::-1]
                stack.append(stack[-1])
                stack = stack[::-1]
            logging.debug(stack)
        return stack
    elif len(myarg.split()) == 3:
        for token in myarg.split():
            try:
                token = int(token)
                stack.append(token)
            except ValueError:
                function = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
            logging.debug(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()