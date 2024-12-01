import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import eval_answer, get_yearday


def part1(lines):
    answer = 0
    
    for line in lines:
        pass
    
    '''
    solve part 1 of the problem here
    # answer = <the answer to the problem>
    '''
    return answer


def part2(lines):
    answer = 0
    
    for line in lines:
        pass
    
    '''
    solve part 2 of the problem here
    # answer = <the answer to the problem>
    '''
    return answer


if __name__ == "__main__":
    year, day = get_yearday(os.getcwd())
    if year == -2 or day == -2:
        print("[!] Get of current year/day failed.")
        sys.exit(0)
    
    if not os.path.exists(".part1tries"):
        os.system("touch .part1tries")
    if not os.path.exists(".part2tries"):
        os.system("touch .part2tries")
    
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    if not os.path.exists(".part1solved"):
        print(f"[-] Solving Part 1 for {year} {day}")
        answer = part1(lines)
        eval_answer(year, day, 1, answer)
    elif os.path.exists(".part1solved") and not os.path.exists(".part2solved"):
        print(f"[-] Solving Part 2 for {year} {day}")
        answer = part2(lines)
        eval_answer(year, day, 2, answer)
    else:
        print(f"You already have all of the stars for {year} {day}!")
