#!/usr/bin/env python3

def check_answer(answer, user_answer, name):
    if answer != user_answer:
        print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{answer}\'.')
        print(f'Let\'s try again, {name}!')
        return False
    else:
        print('Correct!')
        return True
