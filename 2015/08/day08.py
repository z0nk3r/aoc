"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run

def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    for line in lines:
        old_len = len(line)
        esc_len = len(line.encode("utf-8").decode("unicode_escape")[1:-1])
        answer += old_len - esc_len

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    for line in lines:
        old_len = len(line)
        esc_len = len(line) + line.count('\\') + line.count('"') + 2
        answer += esc_len - old_len
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
