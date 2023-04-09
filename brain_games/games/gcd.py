import random


RULE = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    num_1 = random.randint(1, 40)
    num_2 = random.randint(1, 40)
    gcd = get_gcd(num_1, num_2)
    return f'Question: {num_1} {num_2}', gcd


def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return str(a)
