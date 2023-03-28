#!/usr/bin/env python3
import random
import prompt


def question():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    user_answer = prompt.string("Your answer: ")
    return number, user_answer


def result(number):
    if not number % 2:
        return 'yes'
    else:
        return 'no'
