"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from hashlib import md5

def part1(lines):
    '''Function to solve part 1'''
    answer = 0
    key = lines[0]
    key_idx = 0
    while True:
        new_key = f"{key}{key_idx}"
        md5hash = md5(new_key.encode()).hexdigest()
        if md5hash.startswith('00000'):
            answer = key_idx
            break
        key_idx += 1

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    answer = 0
    key = lines[0]
    key_idx = 0
    while True:
        new_key = f"{key}{key_idx}"
        md5hash = md5(new_key.encode()).hexdigest()
        if md5hash.startswith('000000'):
            answer = key_idx
            break
        key_idx += 1

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
