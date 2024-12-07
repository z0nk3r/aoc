from time import sleep

RED = "\033[1;31m"
FAINT = "\033[2m"
RESET = "\033[0m"

SUPER_GREEN = "\033[30;42m"
SUPER_RED = "\033[30;41m"

CLEAR_TERM = "\033[2J\033[;H"
SHOW_CURS = "\033[?25h"
HIDE_CURS = "\033[?25l"

Y_OFFSET = 2
X_OFFSET = 1

FPS = 30


def print_char(char, y, x, color="", time=1/FPS):
    print(f"\033[{y + Y_OFFSET};{x * 2 + X_OFFSET}H{color}{char}{RESET}", end="", flush=True)
    sleep(time)


def print_maze(maze):
    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == "#":
                print_char('#', ridx, cidx, RED, 0)
            else:
                print_char('.', ridx, cidx, FAINT, 0)
        print("")


def get_dir_char(g_dir):
    g_char_d = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}
    return g_char_d[g_dir]


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
        print_char(f"[-] Steps Taken: {len(visited)}", len(maze) + 1, 0)

        g_next = (guard[0] + g_dir[0], guard[1] + g_dir[1])
        
        if (g_next[0] == -1 or g_next[1] == -1 or
            g_next[0] == len(maze) or g_next[1] == len(maze[0])):
            left_maze = True
            print_char(get_dir_char(g_dir), guard[0], guard[1], SUPER_RED, 0)
            break

        if (maze[g_next[0]][g_next[1]] == '#'):
            g_dir = turn_right(g_dir)
        else:
            guard = g_next
            if len(visited) == 1:
                pass
            else:
                print_char(get_dir_char(g_dir), guard[0], guard[1], SUPER_GREEN, 0)
                print_char('.', guard[0] - g_dir[0], guard[1] - g_dir[1], FAINT, 0)


    print_char(f"[-] Steps Taken: {len(visited)}", len(maze) + 1, 0)
    print_char('', len(maze) + 2, 0)
    return len(visited), left_maze


def main():
    lines = [line.replace("\n", "") for line in open(0).readlines()]
    maze = [list(line) for line in lines]

    guard = (0, 0)

    print(CLEAR_TERM, end="", flush=True)
    print(HIDE_CURS, end="", flush=True)
    print_maze(lines)

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