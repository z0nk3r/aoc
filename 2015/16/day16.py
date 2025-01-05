"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run

db = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 
        'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    for line in lines:
        sue, data = line.split(': ', 1)
        comp1, comp2, comp3 = data.split(', ')
        comp1_k, comp1_v = comp1.split(': ')
        comp2_k, comp2_v = comp2.split(': ')
        comp3_k, comp3_v = comp3.split(': ')

        if all([db[comp1_k] == int(comp1_v), db[comp2_k] == int(comp2_v), db[comp3_k] == int(comp3_v)]):
            answer = sue.split(' ')[1]
            break

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    for line in lines:
        sue, data = line.split(': ', 1)
        comp1, comp2, comp3 = data.split(', ')
        comp1_k, comp1_v = comp1.split(': ')
        comp2_k, comp2_v = comp2.split(': ')
        comp3_k, comp3_v = comp3.split(': ')

        results = []
        for key, value in ((comp1_k, comp1_v), (comp2_k, comp2_v), (comp3_k, comp3_v)):
            if key in ('cats', 'trees'):
                results.append(db[key] < int(value))
            elif key in ('pomeranians', 'goldfish'):
                results.append(db[key] > int(value))
            else:
                results.append(db[key] == int(value))

        if all(results):
            answer = sue.split(' ')[1]
            break

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True, refactor=True)
    except KeyboardInterrupt:
        print("")
