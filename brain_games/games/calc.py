import random


RULE = "What is the result of the expression?"


def get_question_and_answer():
    operator = random.choice(['+', '-', '*'])
    num_1 = random.randint(1, 40)
    num_2 = random.randint(1, 40)
    match operator:
        case '+':
            result = num_1 + num_2
        case '-':
            result = num_1 - num_2
        case '*':
            result = num_1 * num_2
    return f'Question: {num_1} {operator} {num_2}', str(result)
