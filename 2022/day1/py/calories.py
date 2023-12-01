#!/usr/bin/env python3

import os
import sys


def main():

    elves = {}

    with open("../input.txt") as input:
        nums = [x.replace("\n", "") for x in input.readlines()]
    total_elves = nums.count("")
    # print(total_elves)

    # init the dict
    for i in range(total_elves+1):
        elves.setdefault(i, 0)

    elf = 0
    for num in nums:
        if num == '':
            elf = elf+1
        else:
            elves[elf] += int(num)

    max = sorted(elves.values(), reverse=True)[0]
    max_2 = sorted(elves.values(), reverse=True)[1]
    max_3 = sorted(elves.values(), reverse=True)[2]
    print(f"Part 1 - Top: {max}")
    print(f"Part 2 - Top 3: {max+max_2+max_3}")

if __name__ == "__main__":
    main()
