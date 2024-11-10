import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import eval_answer, get_yearday


def part1(lines, year, day):
    answer = 0
    answers = []
    
    row = 0
    col = 0
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    for line in lines:
        for idx, char in enumerate(line):
            print(f"{idx}: {char}")
            mid_row = int((min_row + max_row) / 2)
            mid_col = int((min_col + max_col) / 2)
            if char == 'F':
                max_row = mid_row

            elif char == 'B':
                min_row = mid_row + 1

            elif char == 'L':
                max_col = mid_col

            elif char == 'R':
                min_col = mid_col + 1

            print(f"{min_row}-{max_row} {min_col}-{max_col}")
            if idx == (len(line) - 3 - 1):
                if line[idx] == 'F':
                    row = min_row
                else:
                    row = max_row

            if idx == len(line) - 1:
                if line[idx] == 'L':
                    col = min_col
                else:
                    col = max_col

        answers.append((row * 8) + col)
        
        # reset
        min_row = 0
        max_row = 127
        min_col = 0
        max_col = 7

    answers = sorted(answers)
    answer = max(answers)
    # print(f"1. {answer = } {answers = }")
    eval_answer(year, day, 1, answer)


def part2(lines, year, day):
    answer = 0
    answers = []
    
    row = 0
    col = 0
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    for line in lines:
        for idx, char in enumerate(line):
            # print(f"{idx}: {char}")
            mid_row = int((min_row + max_row) / 2)
            mid_col = int((min_col + max_col) / 2)
            if char == 'F':
                max_row = mid_row

            elif char == 'B':
                min_row = mid_row + 1

            elif char == 'L':
                max_col = mid_col

            elif char == 'R':
                min_col = mid_col + 1

            # print(f"{min_row}-{max_row} {min_col}-{max_col}")
            if idx == (len(line) - 3 - 1):
                if line[idx] == 'F':
                    row = min_row
                else:
                    row = max_row

            if idx == len(line) - 1:
                if line[idx] == 'L':
                    col = min_col
                else:
                    col = max_col

        answers.append((row * 8) + col)
        
        # reset
        min_row = 0
        max_row = 127
        min_col = 0
        max_col = 7

    answers = sorted(answers)
    # print(f"{answers = }")
    for i in range(min(answers), max(answers)):
        if i not in answers:
            answer = i
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
