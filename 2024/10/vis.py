
from time import sleep

RED = "\033[1;31m"
BLUE = "\033[1;94m"
GREEN = "\033[1;92m"
FAINT = "\033[2m"
RESET = "\033[0m"

SUPER_GREEN = "\033[30;42m"
SUPER_RED = "\033[30;41m"
SUPER_BLUE = "\033[30;44m"

CLEAR_TERM = "\033[2J\033[;H"
SHOW_CURS = "\033[?25h"
HIDE_CURS = "\033[?25l"

Y_OFFSET = 2
X_OFFSET = 1

FPS = 1800


def print_char(char, y, x, color="", time=1/FPS):
    print(f"\033[{y + Y_OFFSET};{x * 2 + X_OFFSET}H{color}{char}{RESET}", end="", flush=True)
    sleep(time)


def print_maze(maze):
    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            print_char(maze[ridx][cidx], ridx, cidx, FAINT, 0)
        print("")

def in_bounds(ridx, cidx, maze):
    row = 0 <= ridx < len(maze)
    col = 0 <= cidx < len(maze[0])
    return row and col

def bfs(start, end, maze, get_rating = False):
    visited = set()
    neighs = []
    visited.add(start)
    neighs.append(start)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    num_paths = 0
    
    start_r = start[0]
    start_c = start[1]
    print_char(maze[start_r][start_c], start_r, start_c, SUPER_BLUE, 0)
    
    end_r = end[0]
    end_c = end[1]
    print_char(maze[end_r][end_c], end_r, end_c, RED, 0)
    
    while neighs != []:
        curr = neighs.pop(0)
        visited.add(curr)

        if (curr != start and curr != end):
            print_char(maze[curr[0]][curr[1]], curr[0], curr[1], GREEN, 0)
        
        if (maze[curr[0]][curr[1]] == '9'):
            print_char(maze[curr[0]][curr[1]], curr[0], curr[1], SUPER_RED, 0)

        if curr == end:
            num_paths += 1
        for dir in dirs:
            new_r = curr[0] + dir[0]
            new_c = curr[1] + dir[1]
            if in_bounds(new_r, new_c, maze):
                if (int(maze[new_r][new_c]) - int(maze[curr[0]][curr[1]])) == 1:
                    neighs.append((new_r, new_c))

    if get_rating:
        return num_paths

    if start in visited and end in visited:
        return 1
    return 0


def main(maze):
    answer = 0

    starts = []
    ends = []

    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == '0':
                starts.append((ridx, cidx))
            if maze[ridx][cidx] == '9':
                ends.append((ridx, cidx))

    print(CLEAR_TERM, end="", flush=True)
    print(HIDE_CURS, end="", flush=True)
    print_maze(maze)

    for start in starts:
        for end in ends:
            answer += bfs(start, end, maze)
            print_char(f"[-] Answer: {answer}", len(maze) + 1, 0, RESET, 0)

        print_maze(maze)

    print_char('', len(maze) + 2, 0)

if __name__ == "__main__":
    try:
        main([line.replace("\n", "") for line in open(0).readlines()])
    except KeyboardInterrupt:
        print(CLEAR_TERM, end="", flush=True)

    print(SHOW_CURS, end="", flush=True)