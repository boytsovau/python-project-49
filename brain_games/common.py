#!/usr/bin/env python3
import prompt


def game_engine(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.RULE)
    count = 0
    while count < 3:
        question, answer = game.get_question()
        print(question)
        user_answer = prompt.string("Your answer: ")
        if str(answer) != str(user_answer):
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')
            count += 1
    if count == 3:
        print(f'Congratulations, {name}!')
