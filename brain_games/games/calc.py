#!/usr/bin/env python3
import random


def question():
    operator = random.choice(['+', '-', '*'])
    num_1 = random.randint(1, 40)
    num_2 = random.randint(1, 40)
    print(f'Question: {num_1} {operator} {num_2}')
    return operator, num_1, num_2


def result(operator, num_1, num_2):
    match operator:
        case '+':
            result = num_1 + num_2
        case '-':
            result = num_1 - num_2
        case '*':
            result = num_1 * num_2
    return result
