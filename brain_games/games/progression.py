import random


RULE = "What number is missing in the progression?"


def get_question_and_answer():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    progression = [start]
    for i in range(1, 10):
        progression.append(start + i * step)
    random_index = random.randint(0, len(progression) - 1)
    missing_number = progression[random_index]
    progression[random_index] = '..'
    progression = ' '.join(map(str, progression))
    return progression, str(missing_number)
