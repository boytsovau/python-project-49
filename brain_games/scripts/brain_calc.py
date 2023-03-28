#!/usr/bin/env python3
import prompt
from brain_games.games.calc import question, result
from brain_games.welcome import welcome
from brain_games.games.check import check_answer


def main():
    name = welcome()
    print("What is the result of the expression?")
    count = 0
    while count < 3:
        operator, num_1, num_2 = question()
        try:
            user_answer = int(prompt.string("Your answer: "))
            answer = result(operator, num_1, num_2)
            if check_answer(answer, user_answer, name) is True:
                count += 1
            else:
                break
        except ValueError:
            print("It is allowed to enter only numbers, start again")
            break
    if count == 3:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
