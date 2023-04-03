#!/usr/bin/env python3
import random


def rule():
    return "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def question():
    number = random.randint(1, 100)
    game_question = f'Question: {number}'
    if number == 1:
        return game_question, 'no'
    elif number == 2:
        return game_question, 'yes'
    else:
        for i in range(2, number):
            if number % i == 0:
                return game_question, 'no'
        return game_question, 'yes'


if __name__ == '__main__':
    question()
