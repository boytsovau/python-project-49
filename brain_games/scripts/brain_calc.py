#!/usr/bin/env python3
import prompt
from brain_games.games.calc import question,compare,result


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print("What is the result of the expression?")
    count = 0
    while count < 3:
        operator,num_1, num_2 = question()
        user_answer = prompt.string("Your answer: ")
        answer = compare(user_answer,operator,num_1, num_2)
        print(answer)
        count += 1
    if count == 3:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
    