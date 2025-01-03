"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
PRUNE_NUM = 16777216

def get_secret_number(value):

    value = (value ^ (value * 64)) % PRUNE_NUM
    value = (value ^ (value // 32)) % PRUNE_NUM
    value = (value ^ (value * 2048)) % PRUNE_NUM
    
    return value



def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    for line in lines:
        num = int(line)
        for _ in range(2000):
            num = get_secret_number(num)
        answer += num

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    all_totals = {}

    for line in lines:
        num = int(line)
        bananas = [num % 10]
        for _ in range(2000):
            num = get_secret_number(num)
            bananas.append(num % 10)
        
        visited = set()
        for b_idx in range(len(bananas) - 4):
            a, b, c, d, e = bananas[b_idx:b_idx + 5]
            sequence = (b - a, c - b, d - c, e - d)
            if sequence in visited:
                continue
            visited.add(sequence)
            if sequence not in all_totals:
                all_totals[sequence] = 0
            all_totals[sequence] += e

    answer = max(all_totals.values())
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
