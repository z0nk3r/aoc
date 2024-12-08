import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_setup, puzzle_run

from itertools import permutations, combinations, product

def part1(lines):
    answer = 0

    for line in lines:
        total, args = line.split(': ')
        args = args.split()
        math_combos = list(product(['+', '*'], repeat=len(args) - 1))

        for combo in math_combos:
            temp = int(args[0])
            for idx, sym in enumerate(combo):
                if sym == '+':
                    temp += int(args[idx + 1])
                elif sym == '*':
                    temp *= int(args[idx + 1])

            if temp == int(total):
                answer += temp
                break

    return answer


def part2(lines):
    answer = 0

    for line in lines:
        total, args = line.split(': ')
        args = args.split()
        math_combos = list(product(['+', '*', '|'], repeat=len(args) - 1))

        for combo in math_combos:
            temp = int(args[0])
            for s_idx, sym in enumerate(combo):
                if sym == '+':
                    temp += int(args[s_idx + 1])
                elif sym == '*':
                    temp *= int(args[s_idx + 1])
                elif sym == '|':
                    temp = int(f"{temp}{args[s_idx + 1]}")

            if temp == int(total):
                answer += temp
                break

    return answer


if __name__ == "__main__":
    year, day = puzzle_setup()

    try:
        puzzle_run(part1, part2, year, day)
    except KeyboardInterrupt:
        print("")
