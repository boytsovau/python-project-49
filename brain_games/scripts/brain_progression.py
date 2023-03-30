#!/usr/bin/env python3
import prompt
from brain_games.common import welcome, check_answer
from brain_games.games.progression import question


def main():
    name = welcome()
    print("What number is missing in the progression?")
    count = 0
    while count < 3:
        missing = question()
        try:
            user_answer = int(prompt.string("Your answer: "))
            if check_answer(int(missing), user_answer, name) is True:
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
