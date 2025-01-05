"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from collections import defaultdict
from itertools import permutations


def happiness(combo, people):
    score = 0
    for p_idx, person in enumerate(combo):
        p_idx_p = p_idx - 1
        p_idx_n = 0 if p_idx + 1 == len(combo) else p_idx + 1
        score += people[person][combo[p_idx_p]]
        score += people[person][combo[p_idx_n]]

    return score


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    people = defaultdict(dict)

    for line in lines:
        p1, _, _, val, _, _, _, _, _, _, p2 = line.split(' ')
        p2 = p2.replace('.', '')
        val = -int(val) if 'lose' in line else int(val)
        people[p1][p2] = val
    
    person_combos = permutations(people.keys(), len(people))
    scores = [happiness(combo, people) for combo in person_combos]
    answer = max(scores)
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    people = defaultdict(dict)

    for line in lines:
        p1, _, _, val, _, _, _, _, _, _, p2 = line.split(' ')
        p2 = p2.replace('.', '')
        val = -int(val) if 'lose' in line else int(val)
        people[p1][p2] = val
        people[p1]['You'] = 0
        people['You'][p1] = 0

    person_combos = permutations(people.keys(), len(people))
    scores = [happiness(combo, people) for combo in person_combos]
    answer = max(scores)
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
