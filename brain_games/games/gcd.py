#!/usr/bin/env python3
import random


RULE = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    num_1 = random.randint(1, 40)
    num_2 = random.randint(1, 40)
    game_question = f'Question: {num_1} {num_2}'
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    return game_question, str(num_1)
