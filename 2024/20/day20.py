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


def get_dists_bfs(start, end, maze):
    '''BFS of distance traveled'''
    distances = [[-1] * len(maze[0]) for _ in range(len(maze))]
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    neighs = []
    neighs.append(start)
    start_r, start_c = start
    distances[start_r][start_c] = 0

    while neighs:
        curr_r, curr_c = neighs.pop(0)
        if (curr_r, curr_c) == end:
            break

        for new_dr, new_dc in dirs.values():
            new_r = curr_r + new_dr
            new_c = curr_c + new_dc
            if not in_bounds(new_r, new_c, maze):
                continue
            if not valid_space(new_r, new_c, maze):
                continue
            if distances[new_r][new_c] != -1:
                continue

            distances[new_r][new_c] = distances[curr_r][curr_c] + 1
            neighs.append((new_r, new_c))

    return distances


def check_dists(maze, dists, radial):
    count = 0

    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            if not valid_space(ridx, cidx, maze):
                continue

            for radius in range(2, radial + 1):
                for dir_r in range(radius + 1):
                    dir_c = radius - dir_r
                    all_dirs = {(ridx + dir_r, cidx + dir_c), (ridx + dir_r, cidx - dir_c), (ridx - dir_r, cidx + dir_c), (ridx - dir_r, cidx - dir_c)}
                    for new_r, new_c in all_dirs:
                        if not in_bounds(new_r, new_c, maze):
                            continue

                        if not valid_space(new_r, new_c, maze):
                            continue

                        if (dists[ridx][cidx] - dists[new_r][new_c]) >= (100 + radius):
                            count += 1

    return count

def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    maze = [list(line) for line in lines]
    start, end = get_start_end(maze)
    distances = get_dists_bfs(start, end, maze)
    answer = check_dists(maze, distances, 2)

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    maze = [list(line) for line in lines]
    start, end = get_start_end(maze)
    distances = get_dists_bfs(start, end, maze)
    answer = check_dists(maze, distances, 20)

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
