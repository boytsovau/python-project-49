#!/usr/bin/env python3
from brain_games.games.calc import question, RULE
from brain_games.common import welcome, game_count


def main():
    game_count(question, welcome, RULE)


if __name__ == '__main__':
    main()
