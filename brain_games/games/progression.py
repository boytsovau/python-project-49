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
    progression = ' '.join(map(str, progression))
    print(f'Question: {progression}')
    return start, index, step


def result(question):
    start, index, step = question()
    missing = start + index * step
    return missing


if __name__ == '__main__':
    question()
    result()
