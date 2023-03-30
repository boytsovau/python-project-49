#!/usr/bin/env python3
from brain_games.common import welcome, game_count
from brain_games.games.gcd import question, result


def main():
    name = welcome()
    print("Find the greatest common divisor of given numbers.")
    game_count(question, result, name)


if __name__ == '__main__':
    main()
