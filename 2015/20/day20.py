"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from math import sqrt


def sumof_presents(num):
    sum = 0
    end = int(sqrt(num) + 1)
    for idx in range(1, end + 1):
        if num % idx == 0:
            sum += idx
            sum += num/idx
    
    return sum * 10


def sumof_presents11(num):
    sum = 0
    end = int(sqrt(num) + 1)
    for idx in range(1, end + 1):
        if num % idx == 0:
            if (num/idx <= 50):
                sum += idx
            if (idx <= 50):
                sum += num/idx
    
    return sum * 11


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    min_count = int(lines[0])
    num = 1
    while sumof_presents(num) < min_count:
        num += 1
    
    answer = num
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    min_count = int(lines[0])
    num = 1
    while sumof_presents11(num) < min_count:
        num += 1
    
    answer = num
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
