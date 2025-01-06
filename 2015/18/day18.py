"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from time import sleep
import copy
TOTAL_STEPS = 100


def print_maze(move, max_moves, maze):
    fps = 10
    print("\033[2J\033[;H")
    for row in maze:
        print(''.join(row))
    print(f"{move + 1} of {max_moves} - {score_maze(maze)}")
    sleep(1/fps)


def in_bounds(ridx, cidx, maze):
    row = 0 <= ridx < len(maze)
    col = 0 <= cidx < len(maze[0])
    return row and col


def calc_neighs(ridx, cidx, maze):
    num_neighs = 0

    dirs = [(-1, -1), (-1,  0), (-1,  1), 
            ( 0, -1),           ( 0,  1), 
            ( 1, -1), ( 1,  0), ( 1,  1)]

    for dir_r, dir_c in dirs:
        new_r = ridx + dir_r
        new_c = cidx + dir_c
        if not in_bounds(new_r, new_c, maze):
            continue
        if maze[new_r][new_c] == '#':
            num_neighs += 1

    return num_neighs


def update_corners(maze):
    corners = [(0, 0), (0, len(maze[0]) - 1), (len(maze) - 1, 0), (len(maze) - 1, len(maze[0]) - 1)]
    for cr_idx, cc_idx in corners:
        maze[cr_idx][cc_idx] = '#'


def update_maze(maze, corners_broke=False):
    new_maze = copy.deepcopy(maze)
    
    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            on = (col == '#')
            neighs = calc_neighs(ridx, cidx, maze)
            if on and neighs in [2, 3]:
                continue
            if not on and neighs == 3:
                new_maze[ridx][cidx] = '#'
                continue

            new_maze[ridx][cidx] = '.'

    if corners_broke:
        update_corners(new_maze)

    return new_maze


def score_maze(maze):
    score = 0
    for row in maze:
        score += row.count('#')
    return score


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    maze = [list(line) for line in lines]
    for idx in range(TOTAL_STEPS):
        maze = update_maze(maze)
        print_maze(idx, TOTAL_STEPS, maze)

    answer = score_maze(maze)
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    maze = [list(line) for line in lines]
    update_corners(maze)
    
    for idx in range(TOTAL_STEPS):
        maze = update_maze(maze, corners_broke=True)
        print_maze(idx, TOTAL_STEPS, maze)

    answer = score_maze(maze)
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True, refactor=True)
    except KeyboardInterrupt:
        print("")
