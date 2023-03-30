#!/usr/bin/env python3
import prompt
from brain_games.common import welcome, check_answer
from brain_games.games.gcd import question, result


def main():
    name = welcome()
    print("Find the greatest common divisor of given numbers.")
    count = 0
    while count < 3:
        num_1, num_2 = question()
        answer = result(num_1, num_2)
        try:
            user_answer = int(prompt.string("Your answer: "))
            if check_answer(answer, user_answer, name) is True:
                count += 1
            else:
                break
        except ValueError:
            print("It is allowed to enter only numbers, start again")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
