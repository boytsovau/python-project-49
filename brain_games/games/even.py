import random


RULE = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_question_and_answer():
    random_number = random.randint(1, 100)
    if not random_number % 2:
        return random_number, 'yes'
    return random_number, 'no'
