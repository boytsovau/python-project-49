#!/usr/bin/env python3
import random


def question():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    return number

def result(number):
    if not number % 2:
        return 'yes'
    else:
        return 'no'



