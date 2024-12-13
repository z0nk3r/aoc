"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    for line in lines:
        print(line)

    # solve part 1 of the problem here
    # answer = <the answer to the problem>
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    for line in lines:
        print(line)

    # solve part 2 of the problem here
    # answer = <the answer to the problem>
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
