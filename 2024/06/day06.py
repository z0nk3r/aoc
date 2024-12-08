import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_setup, puzzle_run


def turn_right(g_dir):
    right_dir_table = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    return right_dir_table[g_dir]


def get_path(maze, guard):
    g_dir = (-1, 0)
    visited = set()
    vis_w_dir = set()
    left_maze = False
    
    while ((guard, g_dir)) not in vis_w_dir:
        visited.add(guard)
        vis_w_dir.add((guard, g_dir))

        g_next = (guard[0] + g_dir[0], guard[1] + g_dir[1])
        
        if (g_next[0] == -1 or g_next[1] == -1 or
            g_next[0] == len(maze) or g_next[1] == len(maze[0])):
            left_maze = True
            break

        if (maze[g_next[0]][g_next[1]] == '#'):
            g_dir = turn_right(g_dir)
        else:
            guard = g_next
    
    return len(visited), left_maze, [item for item in visited]


def print_status(curr, end):
    BAR_WIDTH = 100

    curr_pct = round((curr/end)*100, 2)
    bar = f"\r[{'=' * int(curr_pct / (100 / BAR_WIDTH))}{' ' * int((100 - curr_pct) / (100 / BAR_WIDTH))}] ({curr_pct:6.2f}/100.00)          "
    print(bar, end = "")


def part1(lines):
    answer = 0
    guard = (0, 0)

    maze = [list(line) for line in lines]
    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == '^':
                guard = (ridx, cidx)

    answer, _, _ = get_path(maze, guard)
    return answer


def part2(lines):
    answer = 0

    guard = (0, 0)
    guard_start = (0, 0)

    poss_obstruct = []
    loop_obstruct = []

    maze = [list(line) for line in lines]
    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == '^':
                guard = (ridx, cidx)
                guard_start = (ridx, cidx)
            else:
                pass

    _, _, poss_obstruct = get_path(maze, guard)
    guard = guard_start

    o_idx = 0
    total_len = len(poss_obstruct)

    while poss_obstruct != []:
        obstacle = poss_obstruct.pop()
        maze[obstacle[0]][obstacle[1]] = '#'
        _, left_maze, _ = get_path(maze, guard)
        if not left_maze:
            loop_obstruct.append(obstacle)
        guard = guard_start
        maze[obstacle[0]][obstacle[1]] = '.'

        o_idx += 1
        if o_idx % 100 == 0:
            print_status(o_idx, total_len)

    print("\n")
    answer = len(loop_obstruct)
    return answer


if __name__ == "__main__":
    year, day = puzzle_setup()

    lines = [line.replace("\n", "") for line in open(0).readlines()]

    puzzle_run(part1, part2, lines, year, day)
