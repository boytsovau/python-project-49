#!/usr/bin/env python3
import random


def rule():
    return "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def question():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    return number


def result(question):
    number = question()
    if not number % 2:
        return 'yes'
    else:
        return 'no'


if __name__ == '__main__':
    question()
    result()
