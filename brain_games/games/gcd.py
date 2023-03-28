#!/usr/bin/env python3
import random


def question():
    num1 = random.randint(1, 40)
    num2 = random.randint(1, 40)
    print(f'Question: {num1} {num2}')
    return  num1, num2


def result(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1
