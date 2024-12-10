import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run

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
    
    while neighs != []:
        curr = neighs.pop(0)
        visited.add(curr)
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


def part1(maze):
    answer = 0

    starts = []
    ends = []

    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == '0':
                starts.append((ridx, cidx))
            if maze[ridx][cidx] == '9':
                ends.append((ridx, cidx))

    for start in starts:
        for end in ends:
            answer += bfs(start, end, maze)

    return answer


def part2(maze):
    answer = 0

    starts = []
    ends = []

    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == '0':
                starts.append((ridx, cidx))
            if maze[ridx][cidx] == '9':
                ends.append((ridx, cidx))

    for start in starts:
        for end in ends:
            answer += bfs(start, end, maze, True)

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
