#!/usr/bin/env python3
import random


def question():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    progression = [start]
    for i in range(1, 10):
        progression.append(start + i * step)
    index = random.randint(0, len(progression) - 1)
    progression[index] = '..'
    missing = start + index * step
    progression = ' '.join(map(str, progression))
    print(f'Question: {progression}')
    return missing
