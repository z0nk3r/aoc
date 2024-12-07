from os import get_terminal_size
from time import sleep

# Shamelessly stolen and tweaked from:
# https://old.reddit.com/r/adventofcode/comments/1h8g546/2024_day_06_part_1python_guard_running_around_my/
# https://github.com/skytwosea/advent_of_code/blob/main/2024/06_2024/solution.py#L159

SUPER_GREEN = "\033[30;42m"
RESET = "\033[0m"

CLEAR_TERM = "\033[2J\033[;H"
SHOW_CURS = "\033[?25h"
HIDE_CURS = "\033[?25l"

WIN_H, WIN_W = get_terminal_size()
WIN_SIZE = int((WIN_W // 2) * 0.75)

FPS = 30


def in_bounds(maze, row, col):
    min_row = 0
    max_row = len(maze)
    min_col = 0
    max_col = len(maze[0])
    
    return min_row <= row < max_row and min_col <= col < max_col


def create_display_window(maze, char, row, col, size=5):
    gmark = char
    window = []

    for r in range(row-size, row + size + 1):
        window_row = [maze[r][c] if in_bounds(maze, r, c) else ' ' for c in range(col-size, col+size+1)]
        window.append(window_row)
    window[size][size] = f"{SUPER_GREEN}{gmark}{RESET}"

    return ('\n'.join([' '.join(line) for line in window]), len(window))


def print_display_window(maze, char, row, col, us, size=WIN_SIZE, delay=1/FPS):
    _window, _side = create_display_window(maze, char, row, col, size)
    if us > 0:
        print("\033[A"*(_side+4))
    print(_window)
    print("\033[B")
    print(f"[-] Steps Taken: {us}")
    sleep(delay)


def get_dir_char(g_dir):
    g_char_d = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}
    return g_char_d[g_dir]


def turn_right(g_dir):
    new_dir = (-1, -1)

    if g_dir == (-1, 0):
        new_dir = (0, 1)

    elif g_dir == (0, 1):
        new_dir = (1, 0)

    elif g_dir == (1, 0):
        new_dir = (0, -1)

    elif g_dir == (0, -1):
        new_dir = (-1, 0)

    return new_dir


def get_path(maze, guard):
    g_dir = (-1, 0)
    visited = set()
    vis_w_dir = set()
    left_maze = False

    while ((guard, g_dir)) not in vis_w_dir:
        visited.add(guard)
        vis_w_dir.add((guard, g_dir))
        print_display_window(maze, get_dir_char(g_dir), guard[0], guard[1], len(visited))

        g_next = (guard[0] + g_dir[0], guard[1] + g_dir[1])
        
        if (g_next[0] == -1 or g_next[1] == -1 or
            g_next[0] == len(maze) or g_next[1] == len(maze[0])):
            left_maze = True
            break

        if (maze[g_next[0]][g_next[1]] == '#'):
            g_dir = turn_right(g_dir)
        else:
            guard = g_next

    return len(visited), left_maze


def main():
    lines = [line.replace("\n", "") for line in open(0).readlines()]
    maze = [list(line) for line in lines]

    guard = (0, 0)

    print(CLEAR_TERM, end="", flush=True)
    print(HIDE_CURS, end="", flush=True)

    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == '^':
                guard = (ridx, cidx)

    get_path(maze, guard)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(CLEAR_TERM, end="", flush=True)

    print(SHOW_CURS, end="", flush=True)