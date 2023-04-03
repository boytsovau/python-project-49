#!/usr/bin/env python3
from brain_games.common import welcome, game_count
from brain_games.games.gcd import question, result, rule


def main():
    game_count(question, result, welcome, rule)


if __name__ == '__main__':
    main()
