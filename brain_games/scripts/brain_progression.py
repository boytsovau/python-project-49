#!/usr/bin/env python3
from brain_games.common import welcome, game_count
from brain_games.games.progression import question, result


def main():
    name = welcome()
    print("What number is missing in the progression?")
    game_count(question, result, name)


if __name__ == '__main__':
    main()
