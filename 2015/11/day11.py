"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
import string


def passwd_check(passwd):
    # must include one increasing straight of at least three letters
    chunks = []
    for p_idx in range(len(passwd) - 2):
        # print(f"{passwd[p_idx:p_idx + 3] = }")
        ch0, ch1, ch2 = passwd[p_idx:p_idx + 3]
        if (ord(ch0) == ord(ch1) - 1) and (ord(ch0) == ord(ch2) - 2):
            chunks.append(1)
        else:
            chunks.append(0)
    if chunks.count(1) == 0:
        return False

    # may not contain the letters i, o, or l
    if ('i' or 'o' or 'l') in passwd:
        return False

    # must contain at least two different, non-overlapping pairs of letters
    doubles = [1 if f'{let}{let}' in passwd else 0 for let in string.ascii_lowercase]
    if doubles.count(1) < 2:
        return False

    return True


def passwd_inc(passwd):
    passwd = list(passwd)
    p_idx = len(passwd) - 1
    while p_idx >= 0:
        if passwd[p_idx] != 'z':
            passwd[p_idx] = chr(ord(passwd[p_idx]) + 1)
            break
        else:
            passwd[p_idx] = 'a'
            if p_idx == 0:
                passwd.insert(0, 'a')
                break
            p_idx -= 1

    return ''.join(passwd)


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    passwd = lines[0]
    while not passwd_check(passwd):
        passwd = passwd_inc(passwd)

    answer = passwd
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    passwd = passwd_inc('cqjxxyzz')  # part1 solution
    while not passwd_check(passwd):
        passwd = passwd_inc(passwd)

    answer = passwd
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True, refactor=True)
    except KeyboardInterrupt:
        print("")
