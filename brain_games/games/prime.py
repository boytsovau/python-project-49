#!/usr/bin/env python3
import random
import prompt


def question():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    user_answer = prompt.string("Your answer: ")
    return number, user_answer


def result(number):
    for i in range(2, number):
        if number % i != 0 and number % 1 == 0:
            i += 1
        else:
            return 'no'
    return 'yes'


if __name__ == '__main__':
    question()
