"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from functools import cache

@cache
def check_line(line, pats): #, rev=False):
    if len(line) == 0:
        return 1

    total = 0
    patss = pats.split(", ")
    for pat in patss:
        if line.startswith(pat):
            total += check_line(line[len(pat):], pats)

    return total

def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    pats = lines[0]
    lines = lines[2:]
    results = [check_line(line, pats) > 0 for line in lines]
    answer = sum(results)

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    pats = lines[0]
    lines = lines[2:]
    results = [check_line(line, pats) for line in lines]
    answer = sum(results)

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
