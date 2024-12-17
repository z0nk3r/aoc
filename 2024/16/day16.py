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
    return maze[ridx][cidx] in ['.', 'S', 'E']


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
        turns, c_loc, c_dir = heappop(pqueue)
        if c_loc == end:
            return turns
        
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
                new_turns = turns
            else:
                new_turns = turns + 1000
            new_turns += 1  # path traveled

            heappush(pqueue, (new_turns, new_loc, (new_dr, new_dc)))


def dijkstras_2(start, end, maze):
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    start_q = (0, start, dirs['>'])
    best_answer = {(start, dirs['>']): 0}
    paths = {}
    best_turns = 1 << 32
    end_routes = set()

    pqueue = []
    pqueue.append(start_q)

    while pqueue:
        turns, c_loc, c_dir = heappop(pqueue)

        if turns > best_answer.get((c_loc, c_dir), 1 << 32):
            continue

        if c_loc == end:
            if turns > best_turns:
                break
            best_turns = turns
            end_routes.add((c_loc, c_dir))

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
                new_turns = turns + 1
            else:
                new_turns = turns + 1000

            best = best_answer.get(((new_r, new_c), (new_dr, new_dc)), 1 << 32)
            if new_turns > best:
                continue

            if new_turns < best:
                paths[((new_r, new_c), (new_dr, new_dc))] = set()
                best_answer[((new_r, new_c), (new_dr, new_dc))] = new_turns

            paths[((new_r, new_c), (new_dr, new_dc))].add((c_loc, c_dir))
            heappush(pqueue, (new_turns, new_loc, (new_dr, new_dc)))

    all_states = list(end_routes)
    visited = set(end_routes)

    while all_states:
        curr = all_states.pop(0)
        for loc in paths.get(curr, []):
            if loc in visited:
                continue
            visited.add(loc)
            all_states.append(loc)

    uniq_visited = set(loc for loc, _ in visited)
    return len(uniq_visited)


def part1(maze):
    '''Function to solve part 1'''
    answer = 0

    start, end = get_start_end(maze)
    answer = dijkstras(start, end, maze)
    return answer


def part2(maze):
    '''Function to solve part 2'''
    answer = 0

    start, end = get_start_end(maze)
    answer = dijkstras_2(start, end, maze)
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
