#!/usr/bin/env python3
import random
import prompt
from brain_games.welcome import welcome


def main():
    name = welcome()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    count = 0
    while count < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string("Your answer: ")
        if (answer == "yes" and not number % 2) or (answer == "no" and number % 2):
            print("Correct!")
            count += 1
        elif (answer == "no" and not number % 2):
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            break
        elif (answer == "yes" and number % 2):
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            break
        else:
            print("Is wrong answer ;(.")
            break
    if count == 3:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
