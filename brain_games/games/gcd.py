#!/usr/bin/env python3
import random


def question():
    num_1 = random.randint(1, 40)
    num_2 = random.randint(1, 40)
    print(f'Question: {num_1} {num_2}')
    return num_1, num_2


def result(question):
    num_1, num_2 = question()
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1


if __name__ == '__main__':
    question()
    result()
