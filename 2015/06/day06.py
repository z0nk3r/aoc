"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
import re

def part1(lines):
    '''Function to solve part 1'''
    answer = 0
    size = 1000
    lights = [[0 for _ in range(size)] for _ in range(size)]

    for line in lines:
        lows, highs = re.findall(r"(\d+\,\d+)", line)
        r_low, c_low = map(int, lows.split(','))
        r_hi, c_hi = map(int, highs.split(','))
        for ridx in range(r_low, r_hi + 1):
            for cidx in range(c_low, c_hi + 1):
                if 'on' in line:
                    lights[ridx][cidx] = 1
                elif 'off' in line:
                    lights[ridx][cidx] = 0
                elif 'toggle' in line:
                    lights[ridx][cidx] = not lights[ridx][cidx]

    for row in lights:
        answer += row.count(1)
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0
    size = 1000
    lights = [[0 for _ in range(size)] for _ in range(size)]

    for line in lines:
        lows, highs = re.findall(r"(\d+\,\d+)", line)
        r_low, c_low = map(int, lows.split(','))
        r_hi, c_hi = map(int, highs.split(','))
        for ridx in range(r_low, r_hi + 1):
            for cidx in range(c_low, c_hi + 1):
                if 'on' in line:
                    lights[ridx][cidx] += 1
                elif 'off' in line:
                    lights[ridx][cidx] = max(lights[ridx][cidx] - 1, 0)
                elif 'toggle' in line:
                    lights[ridx][cidx] += 2

    for row in lights:
        answer += sum(row)
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
