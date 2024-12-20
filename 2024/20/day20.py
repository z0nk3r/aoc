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


def get_start_end(maze):
    start = (-1, -1)
    end = (-1, -1)
    
    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == 'S':
                start = (ridx, cidx)
            if maze[ridx][cidx] == 'E':
                end = (ridx, cidx)
    
    return start, end


def dijkstras(start, end, maze):
    pqueue = []
    visited = set()
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    start_q = (0, start, dirs['>'])
    pqueue.append(start_q)

    while pqueue:
        dist, c_loc, c_dir = heappop(pqueue)
        if c_loc == end:
            return dist
        
        if (c_loc, c_dir) in visited:
            continue
        visited.add((c_loc, c_dir))

        for new_dr, new_dc in dirs.values():
            new_r = c_loc[0] + new_dr
            new_c = c_loc[1] + new_dc
            new_loc = (new_r, new_c)
            backwards = (-c_dir[0], -c_dir[1])

            if (new_dr, new_dc) == backwards:
                continue
            if not in_bounds(new_r, new_c, maze):
                continue
            if not valid_space(new_r, new_c, maze):
                continue

            if (new_dr, new_dc) == c_dir:
                new_turns = dist
            else:
                new_turns = dist
            new_turns += 1  # path traveled

            heappush(pqueue, (new_turns, new_loc, (new_dr, new_dc)))



def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    maze = [list(line) for line in lines]
    start, end = get_start_end(maze)
    def_steps = dijkstras(start, end, maze)
    for ridx, row in enumerate(maze):
        for cidx, row in enumerate(row):
            if (ridx == 0 or ridx == len(maze) or cidx == 0 or cidx == len(maze[0])):
                continue
            if maze[ridx][cidx] != '#':
                continue

            maze[ridx][cidx] = '.'
            new_steps = dijkstras(start, end, maze)
            if (def_steps - new_steps) >= 100:
                print(f"\r({def_steps}>{new_steps}) {ridx * len(maze[0]) + cidx:>5}/{len(maze)*len(maze[0])} ", end="", flush=True)
                answer += 1
            maze[ridx][cidx] = '#'

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    maze = [list(line) for line in lines]
    start, end = get_start_end(maze)
    def_steps = dijkstras(start, end, maze)


    # solve part 2 of the problem here
    # answer = <the answer to the problem>
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
