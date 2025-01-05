"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from itertools import combinations


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    cont_combos = []
    for idx in range(2, len(lines)):
        cont_combos += list(combinations(lines, idx))
    
    for combo in cont_combos:
        combo = list(map(int, combo))
        if sum(combo) == 150:
            answer += 1

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    cont_combos = []
    for idx in range(2, len(lines)):
        cont_combos += list(combinations(lines, idx))
    
    good_combos = []
    for combo in cont_combos:
        combo = list(map(int, combo))
        if sum(combo) == 150:
            good_combos.append(combo)

    good_combos = sorted(good_combos, key=lambda x: len(x))
    for combo in good_combos:
        if len(combo) == len(good_combos[0]):
            answer += 1

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
