"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from functools import cache

@cache
def check_line(line, pats): #, rev=False):
    # curr_idx = 0
    # curr_len = 0
    # good_pats = True

    # if curr_idx >= len(line):
    #     return False
    # if curr_len >= len(line):
    #     return False

    # while curr_idx < len(line):
    #     if rev:
    #         while line[curr_idx:curr_idx + curr_len][::-1] not in pats:
    #             if curr_idx + curr_len >= len(line):
    #                 good_pats = False
    #                 break
    #             curr_len += 1
    #         # print(f"{line[curr_idx:curr_idx + curr_len][::-1]}: {curr_idx = }{curr_len = }")
    #     else:
    #         while line[curr_idx:curr_idx + curr_len] not in pats:
    #             if curr_idx + curr_len >= len(line):
    #                 good_pats = False
    #                 break
    #             curr_len += 1
    #         # print(f"{line[curr_idx:curr_idx + curr_len]}: {curr_idx = }{curr_len = }")
    #     curr_idx += curr_len
    #     curr_len = 0

    # if good_pats:
    #     if rev:
    #         print(f"   {line[::-1]:>60} PASS - Reversed")
    #     else:
    #         print(f"{line:>60} PASS - Forward")
    #     return True

    # if rev:
    #     print(f"   {line[::-1]:>60} IMPOSSIBLE - Reversed")
    # else:
    #     print(f"{line:>60} IMPOSSIBLE - Forward")
    # return False
    
    if len(line) == 0:
        return 1

    patss = pats.split(", ")
    for pat in patss:
        if line.startswith(pat):
            if check_line(line[len(pat):], pats):
                return 1
    
    return 0

def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    pats = lines[0]
    lines = lines[2:]
    # for lidx, line in enumerate(lines[2:]):
        # print(f"{lidx:<3} {line:>60}")
        # if check_line(pats, line):
        #     answer += 1
        # else:
        #     print(f"{line} was IMPOSSIBLE")
    results = [check_line(line, pats) for line in lines]
    answer = sum(results)

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    for line in lines:
        print(line)

    # solve part 2 of the problem here
    # answer = <the answer to the problem>
    return answer


if __name__ == "__main__":
    # try:
    puzzle_run(part1, part2)
    # except KeyboardInterrupt:
    #     print("")
