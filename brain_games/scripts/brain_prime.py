#!/usr/bin/env python3
from brain_games.common import welcome, check_answer
from brain_games.games.prime import question, result


def main():
    name = welcome()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    count = 0
    while count < 3:
        number, user_answer = question()
        answer = result(number)
        if check_answer(answer, user_answer, name) is True:
            count += 1
        else:
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
