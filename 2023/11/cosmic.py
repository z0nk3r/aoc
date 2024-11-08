from math import ceil, dist
from collections import Counter
from itertools import combinations

def man_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def main(lines):
    ans1 = ans2 = 0
    
    blank_rows = set()
    blank_cols = set()
    for ridx, rows in enumerate(lines):
        if (rows.count('.') == len(rows)):
            blank_rows.add(ridx)
        for cidx, cols in enumerate(rows):
            pass

    for cidx, col in enumerate(lines[0]):
        col_list = [line[cidx] for line in lines]
        if col_list.count(':') == len(col_list):
            continue
        if col_list.count('#') == 0:
            for ridx, row in enumerate(lines):
                blank_cols.add(cidx)

    blank_rows = sorted(list(blank_rows))
    blank_cols = sorted(list(blank_cols))

    g_coords1 = set()
    for ridx, rows in enumerate(lines):
        for cidx, cols in enumerate(rows):
            if cols == '#':
                x = ridx
                y = cidx
                for br in blank_rows:
                    if br < ridx:
                        x += 1
                for bc in blank_cols:
                    if bc < cidx:
                        y += 1
                g_coords1.add((x, y))

    g_coords2 = set()
    for ridx, rows in enumerate(lines):
        for cidx, cols in enumerate(rows):
            if cols == '#':
                x = ridx
                y = cidx
                for br in blank_rows:
                    if br < ridx:
                        x += 1000000-1
                for bc in blank_cols:
                    if bc < cidx:
                        y += 1000000-1
                g_coords2.add((x, y))

    g_pairs1 = [(p[0], p[1]) for p in combinations(g_coords1, 2)]
    g_pairs2 = [(p[0], p[1]) for p in combinations(g_coords2, 2)]

    for g_pair in g_pairs1:
        ans1 += man_distance(g_pair[0], g_pair[1])
    for g_pair in g_pairs2:
        ans2 += man_distance(g_pair[0], g_pair[1])

    print(f"1: {ans1}")
    print(f"2: {ans2}")

if __name__ == "__main__":
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    main(lines)
