"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run


def build_lans(lines):
    lans = {}
    for line in lines:
        first, second = line.split('-')
        if first not in lans:
            lans[first] = set()
        lans[first].add(second)
        if second not in lans:
            lans[second] = set()
        lans[second].add(first)
    return lans


def bron_kerbosch(curr_set: set, poss_set: set, excluded_set: set, graph):
    '''
    https://en.wikipedia.org/wiki/Bron–Kerbosch_algorithm

    The Bron–Kerbosch algorithm is an enumeration algorithm for finding all maximal cliques in an undirected graph.
    That is, it lists all subsets of vertices with the two properties that each pair of vertices in one of the listed subsets is connected by an edge,
    and no listed subset can have any additional vertices added to it while preserving its complete connectivity.
    '''
    if not poss_set and not excluded_set:
        return curr_set

    max_group = set()
    for node in poss_set.copy():
        group = bron_kerbosch(curr_set.union({node}), poss_set.intersection(graph[node]), excluded_set.intersection(graph[node]), graph)
        max_group = max(max_group, group, key=len)
        poss_set.remove(node)
        excluded_set.add(node)

    return max_group


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    lans = build_lans(lines)

    trips = set()
    for first in lans.keys():
        for second in lans[first]:
            for third in lans[second]:
                if first != third and first in lans[third]:
                    trips.add(tuple(sorted([first, second, third])))

    t_trips = [sets for sets in trips if any(comp.startswith('t') for comp in sets)]

    answer = len(t_trips)
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = ''

    lans = build_lans(lines)
    max_group = bron_kerbosch(set(), set(lans), set(), lans)
    answer = ','.join(sorted(max_group))
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
