#!/usr/bin/env python3
from brain_games.games.calc import question, result, rule
from brain_games.common import welcome, game_count


def main():
    game_count(question, result, welcome, rule)


if __name__ == '__main__':
    main()
