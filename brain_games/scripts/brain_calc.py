#!/usr/bin/env python3
import prompt
from brain_games.games.calc import question,compare,result
from brain_games.welcome import welcome


def main():
    name = welcome()
    print("What is the result of the expression?")
    count = 0
    while count < 3:
        operator, num_1, num_2 = question()
        user_answer = prompt.string("Your answer: ")
        answer = compare(user_answer, operator, num_1, num_2)
        if answer == False:
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{result(operator,num_1, num_2)}\'.')
            print(f'Let\'s try again,{name}!')
            break
        else:
            print(answer)
        count += 1
    if count == 3:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
    