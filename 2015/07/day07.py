"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from functools import cache

signals = {}

@cache
def get_value(key):
    try:
        return int(key)
    except ValueError:
        pass

    cmds = signals[key].split(' ')
    if "NOT" in cmds:
        return ~get_value(cmds[1])

    if "AND" in cmds:
        return get_value(cmds[0]) & get_value(cmds[2])

    if "OR" in cmds:
        return get_value(cmds[0]) | get_value(cmds[2])

    if "LSHIFT" in cmds:
        return get_value(cmds[0]) << get_value(cmds[2])

    if "RSHIFT" in cmds:
        return get_value(cmds[0]) >> get_value(cmds[2])

    return get_value(cmds[0])


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    for line in lines:
        oper, tgt = line.split(' -> ')
        signals[tgt] = oper

    answer = get_value("a")
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    for line in lines:
        oper, tgt = line.split(' -> ')
        signals[tgt] = oper

    signals["b"] = '3176'
    answer = get_value("a")
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True, refactor=True)
    except KeyboardInterrupt:
        print("")
