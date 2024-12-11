import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from functools import cache

@cache
def blinker(stone, blink):
    # fucking lanternfish
    if blink == 0:
        return 1
    if stone == '0':
        return blinker('1', blink - 1)
    s_len = len(stone)
    delim = s_len // 2
    if s_len % 2 == 0:
        return blinker(str(int(stone[:delim])), blink - 1) + blinker(str(int(stone[delim:])), blink - 1)
    return blinker(str(int(stone) * 2024), blink - 1)


def part1(lines):
    answer = 0
    
    blinks = 25
    stones = lines[0].split()
    results = [blinker(stone, blinks) for stone in stones]

    for res in results:
        answer += res
    return answer


def part2(lines):
    answer = 0
    
    blinks = 75
    stones = lines[0].split()
    results = [blinker(stone, blinks) for stone in stones]

    for res in results:
        answer += res
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
