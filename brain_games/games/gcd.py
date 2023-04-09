import random


RULE = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    num_1 = random.randint(1, 40)
    num_2 = random.randint(1, 40)
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    return f'Question: {num_1} {num_2}', str(num_1)
