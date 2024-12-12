import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run


def calc_perimeter(coordlist):
    perimeter = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for coord in coordlist:
        for dir in dirs:
            new_r = coord[0] + dir[0]
            new_c = coord[1] + dir[1]
            neigh = (new_r, new_c)
            if neigh not in coordlist:
                perimeter += 1
    
    return perimeter


def calc_sides(coordlist):
    '''
    The number of sides is equal to the number of corners.
    '''
    sides = 0
    if len(coordlist) == 1:
        return 4

    for coord in coordlist:
        ridx, cidx = coord

        N = ((ridx - 1, cidx + 0) in coordlist)
        S = ((ridx + 1, cidx + 0) in coordlist)
        E = ((ridx + 0, cidx + 1) in coordlist)
        W = ((ridx + 0, cidx - 1) in coordlist)
        NW = ((ridx - 1, cidx - 1) in coordlist)
        NE = ((ridx - 1, cidx + 1) in coordlist)
        SW = ((ridx + 1, cidx - 1) in coordlist)
        SE = ((ridx + 1, cidx + 1) in coordlist)

        # outer corners
        if (not N and not W and (E or S)):
            sides += 1
        if (not N and not E and (W or S)):
            sides += 1
        if (not S and not W and (N or E)):
            sides += 1
        if (not S and not E and (N or W)):
            sides += 1

        # inner corners
        if (N and W and not NW):
            sides += 1
        if (N and E and not NE):
            sides += 1
        if (S and W and not SW):
            sides += 1
        if (S and E and not SE):
            sides += 1

    return sides


def in_bounds(ridx, cidx, maze):
    row = 0 <= ridx < len(maze)
    col = 0 <= cidx < len(maze[0])
    return row and col


def bfs(start, maze, cmp_func, diag=False):
    visited = set()
    neighs = []
    visited.add(start)
    neighs.append(start)
    if diag:
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    else:
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while neighs != []:
        curr = neighs.pop(0)
        for dir in dirs:
            new_r = curr[0] + dir[0]
            new_c = curr[1] + dir[1]
            if (new_r, new_c) in visited:
                continue

            if not in_bounds(new_r, new_c, maze):
                continue
            
            node1 = maze[curr[0]][curr[1]]
            node2 = maze[new_r][new_c]
            if cmp_func(node1, node2):
                neighs.append((new_r, new_c))
                visited.add((new_r, new_c))

    return sorted(list(visited))


def generate_plots(maze):
    pass_iter = False
    plot_ctr = 0
    plots = {}

    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            curr_letter = maze[ridx][cidx]
            plot_ctr += 1
            if curr_letter not in plots.keys():
                plots[curr_letter] = []

            if len(plots[curr_letter]) > 0:
                for reg in plots[curr_letter]:
                    if (ridx, cidx) in reg:
                        pass_iter = True

            if not pass_iter:
                visited = bfs((ridx, cidx), maze, equal_plots)
                if visited not in plots[curr_letter]:
                    plots[curr_letter].append(visited)

            pass_iter = False

    return plots


def equal_plots(plot1, plot2):
    return plot1 == plot2


def part1(maze):
    answer = 0
    plots = generate_plots(maze)

    for letter, regions in plots.items():
        for reg in regions:
            area = len(reg)
            perim = calc_perimeter(reg)
            answer += area * perim

    return answer


def part2(maze):
    answer = 0
    plots = generate_plots(maze)

    for letter, regions in plots.items():
        for reg in regions:
            area = len(reg)
            sides = calc_sides(reg)
            answer += area * sides

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
