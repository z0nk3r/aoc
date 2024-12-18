"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run


def print_graph(robots, factor, sec):
    fps = 1/60
    graph = []
    tile_w = 101
    tile_h = 103

    for row in range(tile_h):
        graph.append([])
        for col in range(tile_w):
            graph[row].append(" ")

    coordlist = [robot[0] for robot in robots]

    for ridx, row in enumerate(graph):
        for cidx, col in enumerate(row):
            if (ridx, cidx) in coordlist:
                graph[cidx][ridx] = "#"

    with open("graph.txt", "a", encoding="utf-8") as g_file:
        g_file.write(f"{'='*40} {factor} @ {sec} {'='*40}\n")
        for row in graph:
            g_file.write("".join(row))
            g_file.write("\n")
        g_file.write("\n")


def part1(lines):
    '''Function to solve part 1'''
    answer = 0
    seconds = 100
    if len(lines) == 12: # the test case
        tile_w = 11
        tile_h = 7
    else:
        tile_w = 101
        tile_h = 103

    tile_mid_w = tile_w // 2
    tile_mid_h = tile_h // 2

    tl_fact = 0
    tr_fact = 0
    bl_fact = 0
    br_fact = 0

    for line in lines:
        pos, vel = line.split(' ')
        pos_x, pos_y = list(map(int, pos.split('=')[1].split(',')))
        vel_x, vel_y = list(map(int, vel.split('=')[1].split(',')))

        new_posx = (pos_x + (vel_x * seconds)) % tile_w
        new_posy = (pos_y + (vel_y * seconds)) % tile_h

        if (0 <= new_posx < tile_mid_w) and (0 <= new_posy < tile_mid_h):
            tl_fact += 1 
        elif (tile_mid_w + 1 <= new_posx <= tile_w) and (0 <= new_posy < tile_mid_h):
            tr_fact += 1
        elif (0 <= new_posx < tile_mid_w) and (tile_mid_h + 1 <= new_posy <= tile_h):
            bl_fact += 1
        elif (tile_mid_w + 1 <= new_posx <= tile_w) and (tile_mid_h + 1 <= new_posy <= tile_h):
            br_fact += 1

    answer = tl_fact * tr_fact * bl_fact * br_fact
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0
    tile_w = 101
    tile_h = 103
    seconds = tile_w * tile_h  # cyclic pattern
    min_sec_found = 0
    min_factor = 230436441 * 230436441 # borrowing from pt 1 (answer^2)

    tile_mid_w = tile_w // 2
    tile_mid_h = tile_h // 2

    robots = []
    for line in lines:
        pos, vel = line.split(' ')
        pos_x, pos_y = list(map(int, pos.split('=')[1].split(',')))
        vel_x, vel_y = list(map(int, vel.split('=')[1].split(',')))
        robots.append(((pos_x, pos_y), (vel_x, vel_y)))
    
    for sec in range(seconds + 1):
        tl_fact = 0
        tr_fact = 0
        bl_fact = 0
        br_fact = 0

        for _ in range(len(robots)):
            robot = robots.pop(0)
            pos_x = robot[0][0]
            pos_y = robot[0][1]
            vel_x = robot[1][0]
            vel_y = robot[1][1]
            new_posx = (pos_x + vel_x) % tile_w
            new_posy = (pos_y + vel_y) % tile_h

            if (0 <= new_posx < tile_mid_w) and (0 <= new_posy < tile_mid_h):
                tl_fact += 1 
            elif (tile_mid_w + 1 <= new_posx <= tile_w) and (0 <= new_posy < tile_mid_h):
                tr_fact += 1
            elif (0 <= new_posx < tile_mid_w) and (tile_mid_h + 1 <= new_posy <= tile_h):
                bl_fact += 1
            elif (tile_mid_w + 1 <= new_posx <= tile_w) and (tile_mid_h + 1 <= new_posy <= tile_h):
                br_fact += 1

            robots.append(((new_posx, new_posy), (vel_x, vel_y)))

        factor = tl_fact * tr_fact * bl_fact * br_fact

        if factor < min_factor:
            min_factor = factor
            min_sec_found = sec + 1
            print_graph(robots, factor, sec + 1)

    answer = min_sec_found
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, True)
    except KeyboardInterrupt:
        print("")
