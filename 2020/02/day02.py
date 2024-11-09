import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import eval_answer, get_yearday


def part1(lines, year, day):
    answer = 0
    
    for line in lines:
        reqs, password = line.split(":")
        minmax, char = reqs.split(" ")
        start, end  = minmax.split("-")

        if int(start) <= password.count(char) <= int(end):
            answer += 1
    
    eval_answer(year, day, 1, answer)


def part2(lines, year, day):
    answer = 0
    
    for line in lines:
        reqs, password = line.split(":")
        minmax, char = reqs.split(" ")
        start, end = minmax.split("-")
        
        password = password.strip()

        try:
            if password[int(start) - 1] == char and password[int(end) - 1] != char:
                answer += 1
            elif password[int(start) - 1] != char and password[int(end) - 1] == char:
                answer += 1
            else:
                pass
        except IndexError:
            pass

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
        print(f"You already have the stars for {year} {day}!")

