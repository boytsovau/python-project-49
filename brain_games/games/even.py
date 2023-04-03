#!/usr/bin/env python3
import random


def rule():
    return "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def question():
    number = random.randint(1, 100)
    game_question = f'Question: {number}'
    if not number % 2:
        return game_question, 'yes'
    else:
        return game_question, 'no'


if __name__ == '__main__':
    question()
