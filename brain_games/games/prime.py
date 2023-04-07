import random


RULE = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def get_question_and_answer():
    random_number = random.randint(1, 100)
    game_question = f'Question: {random_number}'
    answer = 'yes' if is_prime(random_number) else 'no'
    return game_question, answer


def is_prime(random_number) -> bool:
    if random_number == 1:
        return False
    elif random_number == 2:
        return True
    else:
        for i in range(2, random_number):
            if random_number % i == 0:
                return False
        return True
