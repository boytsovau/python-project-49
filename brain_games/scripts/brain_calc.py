#!/usr/bin/env python3
import prompt
import random

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print("What is the result of the expression?")
    n = random.choice(['+', '-', '*'])
    count = 0
    while count < 3:
        number_1 = random.randint(1, 40)
        number_2 = random.randint(1, 40)
        print(f'Question: {number_1} {n} {number_2}')
        answer = prompt.string("Your answer: ")
        if n == '+':
                result = number_1 + number_2
        elif n == '-':
                result = number_1 - number_2
        else:
                result = number_1 * number_2
        if int(answer) == result:
              print('Correct!')
        else:
              print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{result}\'.')
              print(f'Let\'s try again, {name}!')
              break
        count += 1
    if count == 3:
        print(f'Congratulations, {name}')
















if __name__ == '__main__':
    main()