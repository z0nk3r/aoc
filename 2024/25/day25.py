"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run


def check_key_lock(key, lock):
    for ridx in range(len(key)):
        for cidx in range(len(key[0])):
            if key[ridx][cidx] == '#' and lock[ridx][cidx] == '#':
                return False
    
    return True


def part1(lines):
    '''Function to solve part 1'''
    answer = 0
    keys = []
    locks = []
    
    for keylock in [kl.split('\n') for kl in '\n'.join(lines).split('\n\n')]:
        if keylock[0] == '#####':
            locks.append(keylock)
        else:
            keys.append(keylock)

    for key in keys:
        for lock in locks:
            if check_key_lock(key, lock):
                answer += 1

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 1
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
