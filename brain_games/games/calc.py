#!/usr/bin/env python3
import random


def rule():
    return "What is the result of the expression?"


def question():
    operator = random.choice(['+', '-', '*'])
    num_1 = random.randint(1, 40)
    num_2 = random.randint(1, 40)
    game_question = f'Question: {num_1} {operator} {num_2}'
    match operator:
        case '+':
            result = num_1 + num_2
        case '-':
            result = num_1 - num_2
        case '*':
            result = num_1 * num_2
    return game_question, result


if __name__ == '__main__':
    question()
