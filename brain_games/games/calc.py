#!/usr/bin/env python3
import random


def question():
    operator = random.choice(['+', '-', '*'])
    num_1 = random.randint(1, 40)
    num_2 = random.randint(1, 40)
    print(f'Question: {num_1} {operator} {num_2}')
    return operator,

def result(operator,num_1, num_2):
        if operator == '+':
            result = num_1 + num_2
        elif operator == '-':
            result = num_1 - num_2
        else:
            result = num_1 * num_2
        return result

def compare(user_answer):
    if int(user_answer) == result():
        return 'Correct!'
    else:
        return f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{result(operator,num_1, num_2)}\'.'
    
if __name__ == '__main__':
    question()
    result()
    compare()