import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import eval_answer, get_yearday

from collections import Counter

def part1(lines, year, day):
    answer = 0
    answers = []
    answered = set()
    
    for line in lines:
        if line == '':
            # reset
            answers.append(len(answered))
            answered = set()
        else:
            for char in line:
                answered.add(char)
    
    # get the last one
    answers.append(len(answered))
    
    answer = sum(answers)
    print(f"{answer = }\n{answers = }")
    eval_answer(year, day, 1, answer)


def part2(lines, year, day):
    answer = 0
    answers = []
    answered_s = set()
    answered_c = Counter()
    answered_ctr = 0
    num_people = 0
    
    for line in lines:
        if line == '':
            for char in answered_s:
                if answered_c[char] == num_people:
                    answered_ctr += 1
            answers.append(answered_ctr)
            
            # reset
            num_people = 0
            answered_s - set()
            answered_c = Counter()
            answered_ctr = 0
            
        else:
            answered_c += Counter(line)
            for char in line:
                answered_s.add(char)
            num_people += 1
    
    # get the last one
    for char in answered_s:
        if answered_c[char] == num_people:
            answered_ctr += 1
    answers.append(answered_ctr)
    
    answer = sum(answers)
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
