"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from heapq import heappush, heappop


def in_bounds(ridx, cidx, maze):
    row = 0 <= ridx < len(maze)
    col = 0 <= cidx < len(maze[0])
    return row and col


def valid_space(ridx, cidx, maze):
    return maze[ridx][cidx] != '#'


def dijkstras(coords, size, start_idx, start, end):
    '''dijkstras w/ no weights (BFS)'''

    # build and populate maze
    maze = [['.' for _ in range(size)] for _ in range(size)]
    for s_idx in range(start_idx):
        cidx, ridx = map(int, coords[s_idx].split(','))
        maze[ridx][cidx] = '#'

    pqueue = []
    visited = set()
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    start_q = (0, start, dirs['>'])
    pqueue.append(start_q)

    while pqueue:
        steps, c_loc, c_dir = heappop(pqueue)

        if c_loc == end:
            return steps

        if (c_loc, c_dir) in visited:
            continue
        visited.add((c_loc, c_dir))

        for new_dr, new_dc in dirs.values():
            new_r = c_loc[0] + new_dr
            new_c = c_loc[1] + new_dc

            if (new_dr, new_dc) == (-c_dir[0], -c_dir[1]):  # backwards
                continue
            if not in_bounds(new_r, new_c, maze):
                continue
            if not valid_space(new_r, new_c, maze):
                continue

            # apply weights here
            if (new_dr, new_dc) == c_dir:
                new_turns = steps
            else:
                new_turns = steps
            new_turns += 1

            heappush(pqueue, (new_turns, (new_r, new_c), (new_dr, new_dc)))

    return 0


def part1(coords):
    '''Function to solve part 1'''
    answer = 0
    if len(coords) <= 25:  # testcase
        stepsneeded = 12
        max_size = 7
    else:
        stepsneeded = 1024
        max_size = 71

    answer = dijkstras(coords, max_size, stepsneeded, (0, 0), (max_size - 1, max_size - 1))

    return answer


def part2(coords):
    '''Function to solve part 2'''
    answer = 0
    if len(coords) <= 25:  # testcase
        stepsneeded = 12
        max_size = 7
    else:
        stepsneeded = 1024
        max_size = 71

    bst_low = stepsneeded
    bst_high = len(coords)
    while bst_low != bst_high - 1:
        bst_mid = (bst_high + bst_low) // 2
        if dijkstras(coords, max_size, bst_mid, (0, 0), (max_size - 1, max_size - 1)):
            bst_low = bst_mid
        else:
            bst_high = bst_mid
    answer = coords[bst_low]

    print(f"{answer = }")
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
