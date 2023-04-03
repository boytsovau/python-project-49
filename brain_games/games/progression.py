#!/usr/bin/env python3
import random


def rule():
    return "What number is missing in the progression?"


def question():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    progression = [start]
    for i in range(1, 10):
        progression.append(start + i * step)
    index = random.randint(0, len(progression) - 1)
    progression[index] = '..'
    progression = ' '.join(map(str, progression))
    start, index, step = question()
    missing = start + index * step
    game_question = f'Question: {progression}'
    return game_question, missing


if __name__ == '__main__':
    question()
