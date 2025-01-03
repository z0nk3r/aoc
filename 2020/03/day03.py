import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import eval_answer, get_yearday


def part1(lines, year, day):
    answer = 0
    
    x_width = len(lines[0])
    currx = 0
    curry = 0

    while curry < len(lines):
        currx += 3
        curry += 1
        
        if currx > x_width - 1:
            currx -= x_width

        try:
            if lines[curry][currx] == '#':
                answer += 1
        except IndexError:
            # print(f"indexerrored on {currx}x{curry}")
            pass

    eval_answer(year, day, 1, answer)


def part2(lines, year, day):
    answer = 0
    
    moveset = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for xmove, ymove in moveset:
        x_width = len(lines[0])
        currx = 0
        curry = 0
        subanswer = 0

        while curry < len(lines):
            currx += xmove
            curry += ymove
            
            if currx > x_width - 1:
                currx -= x_width

            try:
                if lines[curry][currx] == '#':
                    subanswer += 1
            except IndexError:
                # print(f"indexerrored on {currx}x{curry}")
                pass
        
        if answer == 0:
            answer = subanswer
        else:
            answer *= subanswer

    eval_answer(year, day, 2, answer)


if __name__ == "__main__":
    year, day = get_yearday(os.getcwd())
    if year == -2 or day == -2:
        sys.exit(0)
    
    if not os.path.exists(".part1tries"):
        os.system("touch .part1tries")
    if not os.path.exists(".part2tries"):
        os.system("touch .part2tries")
    
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    if not os.path.exists(".part1solved"):
        print(f"[-] Solving Part 1 for {year} {day}")
        part1(lines, year, day)
    elif os.path.exists(".part1solved") and not os.path.exists(".part2solved"):
        print(f"[-] Solving Part 2 for {year} {day}")
        part2(lines, year, day)
    else:
        print(f"You already have all of the stars for {year} {day}!")
