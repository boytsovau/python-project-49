#!/usr/bin/env python3
import prompt
from brain_games.welcome import welcome
from brain_games.games.even import question, result


def main():
    name = welcome()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    count = 0
    while count < 3:
        number = question()
        user_answer = prompt.string("Your answer: ")
        answer = result(number)
        if answer == user_answer:
            print("Correct!")
            count += 1
        elif answer != user_answer:
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{answer}\'.')
            break
        else:
            print("Is wrong answer ;(.")
            break
    if count == 3:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
