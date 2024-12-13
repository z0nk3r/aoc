import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run

import re

def part1(lines):
    answer = 0
    
    for line in lines:
        muls = re.findall("mul\(\d+,\d+\)", line)
        for mul in muls:
            nums = re.findall('\d+', mul)
            answer += int(nums[0]) * int(nums[1])

    return answer


def part2(lines):
    answer = 0
    do = True
    
    for line in lines:
        founds = re.findall("mul\(\d+,\d+\)|do\(\)|don\'t\(\)", line)
        for res in founds:
            if res == "don't()":
                do = False
            elif res == "do()":
                do = True
            else:
                if do:
                    nums = re.findall('\d+', res)
                    answer += int(nums[0]) * int(nums[1])

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")