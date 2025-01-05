"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from collections import defaultdict
from itertools import permutations

def brute_scores(ingredients, cal_filter=False):
    scores = []
    for i in range(100):
        for j in range(100 - i):
            for k in range(100 - i - j):
                l = 100 - i - j - k
                a = ingredients['Sprinkles']['capacity'] * i
                a += ingredients['Butterscotch']['capacity'] * j
                a += ingredients['Chocolate']['capacity'] * k
                a += ingredients['Candy']['capacity'] * l

                b = ingredients['Sprinkles']['durability'] * i
                b += ingredients['Butterscotch']['durability'] * j
                b += ingredients['Chocolate']['durability'] * k
                b += ingredients['Candy']['durability'] * l

                c = ingredients['Sprinkles']['flavor'] * i
                c += ingredients['Butterscotch']['flavor'] * j
                c += ingredients['Chocolate']['flavor'] * k
                c += ingredients['Candy']['flavor'] * l

                d = ingredients['Sprinkles']['texture'] * i
                d += ingredients['Butterscotch']['texture'] * j
                d += ingredients['Chocolate']['texture'] * k
                d += ingredients['Candy']['texture'] * l

                e = ingredients['Sprinkles']['calories'] * i
                e += ingredients['Butterscotch']['calories'] * j
                e += ingredients['Chocolate']['calories'] * k
                e += ingredients['Candy']['calories'] * l

                if cal_filter:
                    if e != 500:
                        continue

                if (a < 1 or b < 1 or c < 1 or d < 1):
                    scores.append(0)
                    continue

                scores.append(a * b * c * d)
                print(a * b * c * d, (i, j, k, l))

    return scores



def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    ingredients = defaultdict(dict)
    for line in lines:
        name, data = line.split(': ')
        datas = data.split(', ')
        for item in datas:
            key, val = item.split(' ')
            ingredients[name][key] = int(val)

    scores = brute_scores(ingredients)

    answer = max(scores)
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    ingredients = defaultdict(dict)
    for line in lines:
        name, data = line.split(': ')
        datas = data.split(', ')
        for item in datas:
            key, val = item.split(' ')
            ingredients[name][key] = int(val)

    scores = brute_scores(ingredients, cal_filter=True)

    answer = max(scores)
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True, refactor=True)
    except KeyboardInterrupt:
        print("")
