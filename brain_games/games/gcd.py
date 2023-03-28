#!/usr/bin/env python3
import random


def question():
    num_1 = random.randint(1, 40)
    num_2 = random.randint(1, 40)
    print(f'Question: {num_1} {num_2}')
    return num_1, num_2


def result(num_1, num_2):
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1
