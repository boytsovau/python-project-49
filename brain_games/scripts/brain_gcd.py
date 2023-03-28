#!/usr/bin/env python3
from brain_games.welcome import welcome
from brain_games.games.check import check_answer


def main():
    name = welcome()
    print("Find the greatest common divisor of given numbers.")
    count = 0
    while count < 3:
        