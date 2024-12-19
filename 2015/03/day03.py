"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run


def part1(lines):
    '''Function to solve part 1'''
    answer = 0
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    c_loc = (0, 0)
    visited = set()
    visited.add(c_loc)

    for dir_ in lines[0]:
        new_dr, new_dc = dirs[dir_]
        new_r = c_loc[0] + new_dr
        new_c = c_loc[1] + new_dc
        visited.add((new_r, new_c))
        c_loc = (new_r, new_c)

    answer = len(visited)
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    s_loc = (0, 0)
    r_loc = (0, 0)
    visited = set()
    visited.add(s_loc)

    for dir_ in lines[0][0::2]:
        new_dr, new_dc = dirs[dir_]
        new_r = s_loc[0] + new_dr
        new_c = s_loc[1] + new_dc
        visited.add((new_r, new_c))
        s_loc = (new_r, new_c)

    for dir_ in lines[0][1::2]:
        new_dr, new_dc = dirs[dir_]
        new_r = r_loc[0] + new_dr
        new_c = r_loc[1] + new_dc
        visited.add((new_r, new_c))
        r_loc = (new_r, new_c)

    answer = len(visited)
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
