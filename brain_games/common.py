#!/usr/bin/env python3
import prompt


def welcome():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def check_answer(answer, user_answer, name):
    if str(answer) != str(user_answer):
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was' {answer}'.")
        print(f'Let\'s try again, {name}!')
        return False
    else:
        print('Correct!')
        return True


def game_count(question, result, name):
    count = 0
    while count < 3:
        answer = result(question)
        user_answer = prompt.string("Your answer: ")
        if check_answer(answer, user_answer, name) is True:
            count += 1
        else:
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    welcome()
