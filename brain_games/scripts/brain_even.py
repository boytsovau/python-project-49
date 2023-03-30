#!/usr/bin/env python3
from brain_games.common import welcome, game_count
from brain_games.games.even import question, result


def main():
    name = welcome()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    game_count(question, result, name)


if __name__ == '__main__':
    main()
