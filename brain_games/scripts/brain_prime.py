#!/usr/bin/env python3
from brain_games.common import welcome, game_count
from brain_games.games.prime import question, result


def main():
    name = welcome()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    game_count(question, result, name)


if __name__ == '__main__':
    main()
