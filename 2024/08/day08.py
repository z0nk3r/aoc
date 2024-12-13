import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run

import string
from math import sqrt

def dist_formula(node1, node2):
    return (node2[0] - node1[0]), (node2[1] - node1[1])


def in_bounds(grid, node):
    row = 0 <= node[0] < len(grid)
    col = 0 <= node[1] < len(grid[0])
    return row and col


def part1(lines):
    answer = 0
    anodes = set()

    poss_dishes = string.ascii_letters + string.digits
    for dish in poss_dishes:
        dish_locs = []
        for ridx, row in enumerate(lines):
            for cidx, col in enumerate(row):
                if lines[ridx][cidx] == dish:
                    dish_locs.append((ridx, cidx))

        if len(dish_locs) <= 1:
            continue

        while len(dish_locs) > 1:
            curr = dish_locs.pop()
            for node in dish_locs:
                r_dist, c_dist = dist_formula(curr, node)

                new_node_a = (curr[0] - r_dist, curr[1] - c_dist)
                if in_bounds(lines, new_node_a):
                    anodes.add(new_node_a)

                new_node_b = (node[0] + r_dist, node[1] + c_dist)
                if in_bounds(lines, new_node_b):
                    anodes.add(new_node_b)

    answer = len(anodes)
    return answer


def part2(lines):
    answer = 0
    anodes = set()

    poss_dishes = string.ascii_letters + string.digits
    for dish in poss_dishes:
        dish_locs = []
        for ridx, row in enumerate(lines):
            for cidx, col in enumerate(row):
                if lines[ridx][cidx] == dish:
                    dish_locs.append((ridx, cidx))

        if len(dish_locs) <= 1:
            continue

        while len(dish_locs) > 1:
            curr = dish_locs.pop()
            anodes.add(curr)
            for node in dish_locs:
                anodes.add(node)
                r_dist, c_dist = dist_formula(curr, node)

                new_node_a = (curr[0] - r_dist, curr[1] - c_dist)
                while in_bounds(lines, new_node_a):
                    anodes.add(new_node_a)
                    new_node_a = (new_node_a[0] - r_dist, new_node_a[1] - c_dist)

                new_node_b = (node[0] + r_dist, node[1] + c_dist)
                while in_bounds(lines, new_node_b):
                    anodes.add(new_node_b)
                    new_node_b = (new_node_b[0] + r_dist, new_node_b[1] + c_dist)

    answer = len(anodes)
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
