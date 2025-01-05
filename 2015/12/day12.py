"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
import re
import json

def get_valid_nums(data, red_filter=False):
    if isinstance(data, (int, float)):
        return data

    if isinstance(data, (list, tuple)):
        return sum(get_valid_nums(item, red_filter) for item in data)

    if isinstance(data, dict):
        if red_filter:
            if any(isinstance(v, str) and v == 'red' for v in data.values()):
                return 0

        return sum(get_valid_nums(value, red_filter) for value in data.values())

    return 0


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    answer = get_valid_nums(json.loads(lines[0]))

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    answer = get_valid_nums(json.loads(lines[0]), red_filter=True)

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
