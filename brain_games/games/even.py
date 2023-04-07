#!/usr/bin/env python3
import random


RULE = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_question_and_answer():
    random_number = random.randint(1, 100)
    game_question = f'Question: {random_number}'
    if not random_number % 2:
        return game_question, 'yes'
    else:
        return game_question, 'no'
