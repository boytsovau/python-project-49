#!/usr/bin/env python3
from brain_games.common import welcome, game_count
from brain_games.games.progression import question, rule


def main():
    game_count(question, welcome, rule)


if __name__ == '__main__':
    main()
