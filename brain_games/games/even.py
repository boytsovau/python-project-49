import random


RULE = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_question_and_answer():
    random_number = random.randint(1, 100)
    if not random_number % 2:
        return f'Question: {random_number}', 'yes'
    return f'Question: {random_number}', 'no'
