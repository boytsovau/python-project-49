#!/usr/bin/env python3
import prompt
from brain_games.games.calc import question, result
from brain_games.welcome import welcome


def main():
    name = welcome()
    print("What is the result of the expression?")
    count = 0
    while count < 3:
        operator, num_1, num_2 = question()
        user_answer = prompt.string("Your answer: ")
        answer = result(operator, num_1, num_2)
        try:
            if answer != int(user_answer):
                print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{answer}\'.')
                print(f'Let\'s try again, {name}!')
                break
            else:
                print('Correct!')
        except ValueError:
            print("It is allowed to enter only numbers, start again")
            break
        count += 1
    if count == 3:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
