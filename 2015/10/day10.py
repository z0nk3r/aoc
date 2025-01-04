"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from itertools import groupby


def look_and_say(num):
    new_num = ''.join(str(len(list(g))) + k for k, g in groupby(num))
    return new_num


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    num = lines[0]
    for _ in range(40):
        num = look_and_say(num)

    answer = len(num)
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    answer = 0

    num = lines[0]
    for _ in range(50):
        num = look_and_say(num)

    answer = len(num)
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
