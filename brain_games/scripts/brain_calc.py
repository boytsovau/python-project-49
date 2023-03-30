#!/usr/bin/env python3
from brain_games.games.calc import question, result
from brain_games.common import welcome, game_count


def main():
    name = welcome()
    print("What is the result of the expression?")
    game_count(question, result, name)


if __name__ == '__main__':
    main()
