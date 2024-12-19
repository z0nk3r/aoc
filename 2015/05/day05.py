"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
import re
import string


def part1(lines):
    '''Function to solve part 1'''
    answer = 0
    bad_strs = ['ab', 'cd', 'pq', 'xy']

    good_line = True
    for line in lines:
        
        for bad in bad_strs:
            if bad in line:
                good_line = False

        if len(re.findall('[aeiou]', line)) < 3:
            good_line = False

        doubles = [1 if f'{let}{let}' in line else 0 for let in string.ascii_lowercase]
        if 1 not in doubles:
            good_line = False

        if good_line:
            answer += 1
        good_line = True

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    good_line = True
    for line in lines:

        doubles = [line.count(f'{let_a}{let_b}')
                   for let_a in string.ascii_lowercase
                   for let_b in string.ascii_lowercase]
        if doubles.count(1) + doubles.count(0) == len(doubles):
            good_line = False

        doubles = [line.count(f'{let_a}{let_b}{let_a}')
                   for let_a in string.ascii_lowercase
                   for let_b in string.ascii_lowercase]
        if doubles.count(0) == len(doubles):
            good_line = False

        if good_line:
            answer += 1
        good_line = True
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
