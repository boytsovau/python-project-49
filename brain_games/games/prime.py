#!/usr/bin/env python3
import random


def question():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    return number


def result(question):
    number = question()
    for i in range(2, number):
        if number % i != 0 and number % 1 == 0:
            i += 1
        else:
            return 'no'
    return 'yes'


if __name__ == '__main__':
    question()
    result()
