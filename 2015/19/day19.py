"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from collections import defaultdict


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    subs = []
    meds = ''
    found = set()
    for line in lines:
        if '=>' in line:
            src, dest = line.split(' => ')
            subs.append((src, dest))
        elif line == '':
            continue
        else:
            meds = line

    for src, dest in subs:
        l_idx = -1
        idx = 0
        indexes = []
        while True:
            idx += 1
            l_idx = meds.find(src, l_idx + 1)
            if l_idx != -1:
                indexes.append(l_idx)
            else:
                break
        for curr in indexes:
            found.add(meds[0:curr] + dest + meds[curr + len(src):])
    
    answer = len(found)
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    subs = []
    meds = ''
    for line in lines:
        if '=>' in line:
            src, dest = line.split(' => ')
            subs.append((src, dest))
        elif line == '':
            continue
        else:
            meds = line

    subscopy = subs.copy()

    count = 0
    curr = meds
    while curr != 'e':
        try:
            f = max(subs, key=lambda x: len(x[1]))
        except ValueError:
            subs = subscopy.copy()
            f = max(subs, key=lambda x: len(x[1]))
        before, after = f
        new = curr.replace(after, before, 1)
        if curr != new:
            count += 1
        else:
            subs.remove(f)
        curr = new

    answer = count
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
