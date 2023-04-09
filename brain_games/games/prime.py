import random


RULE = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def get_question_and_answer():
    random_number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return f'Question: {random_number}', correct_answer


def is_prime(number) -> bool:
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True
