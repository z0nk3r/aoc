"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from collections import defaultdict
from heapq import heappush, heappop


def dijkstras(start, routes):
    pqueue = []
    start_q = (0, start, [start])
    pqueue.append(start_q)

    while pqueue:
        dist, c_loc, route = heappop(pqueue)
        if len(route) == len(routes):
            shortest = (dist, route)
            break

        for new_loc, new_dist in routes[c_loc]:
            if new_loc in route:
                continue
            heappush(pqueue, (dist + int(new_dist), new_loc, route + [new_loc]))

    return (shortest)


def long_dijkstras(start, routes):
    pqueue = []
    start_q = (0, start, [start])
    pqueue.append(start_q)

    while pqueue:
        dist, c_loc, route = heappop(pqueue)
        if len(route) == len(routes):
            longest = (dist, route)
            break

        for new_loc, new_dist in routes[c_loc]:
            if new_loc in route:
                continue
            heappush(pqueue, (dist - int(new_dist), new_loc, route + [new_loc]))

    return (longest)


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    routes = defaultdict(list)

    for line in lines:
        loc1, _, loc2, _, dist = line.split(' ')
        routes[loc1].append((loc2, dist))
        routes[loc2].append((loc1, dist))

    all_dists = []
    for location in routes:
        all_dists.append(dijkstras(location, routes))

    dists = sorted(all_dists, key=lambda x: x[0])
    for node in dists:
        print(node)
    answer, shortest_route = dists[0]
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    routes = defaultdict(list)

    for line in lines:
        loc1, _, loc2, _, dist = line.split(' ')
        routes[loc1].append((loc2, dist))
        routes[loc2].append((loc1, dist))

    all_dists = []
    for location in routes:
        all_dists.append(long_dijkstras(location, routes))

    dists = sorted(all_dists, key=lambda x: x[0])
    for node in dists:
        print(node)
    answer, shortest_route = dists[0]
    return -answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
