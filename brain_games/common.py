#!/usr/bin/env python3
import prompt


def welcome():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def check_answer(answer, user_answer, name):
    if answer != user_answer:
        print(f"{user_answer}' is wrong answer ;(."
              f"Correct answer was'{answer}'.")
        print(f'Let\'s try again, {name}!')
        return False
    else:
        print('Correct!')
        return True


if __name__ == '__main__':
    welcome()
    check_answer()
