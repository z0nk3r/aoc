"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    for line in lines:
        l, w, h = map(int, line.split('x'))
        small_side = min(l * w, l * h, w * h)
        answer += (2 * l * w + 2 * w * h + 2 * h * l) + small_side
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    for line in lines:
        l, w, h = map(int, line.split('x'))
        small_perim = min(2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h)
        answer += (l * w * h) + small_perim
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
