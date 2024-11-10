import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import submit_answer, aoc_timeout


def check_if_old_answer(part: int, answer: int) -> bool:
    ''' Checks old answers if current answer has already been attempted '''
    given_answers = [int(line.replace("\n", "")) for line in open(f".part{part}tries").readlines()]
    return answer in given_answers


def add_to_answers(part: int, answer: int) -> None:
    ''' Adds a bad answer to the local cache of bad answers '''
    with open(f".part{part}tries", "a") as given_answers:
        given_answers.write(f"{answer}\n")


def eval_answer(year: int, day: int, part: int, answer: int) -> None:
    ''' Evaluates the provided answer. Auto submits answer, and evals if correct or incorrect'''
    if check_if_old_answer(part, answer):
        print("[!] You already tried this answer!")
        return
    b_submit, response = submit_answer(year, day, part, answer)
    if b_submit:
        os.system(f"touch .part{part}solved")
        print(f"{part}. {answer} - {response}")
    else:
        if "already complete it" in response:
            os.system(f"touch .part{part}solved")
            print("[x] You already have this star!")
            return
        print(f"{part} - {answer} was incorrect.")
        aoc_timeout(response)
        print("\n")

    add_to_answers(part, answer)


def part1(lines, year, day):
    answer = 0
    
    for line1 in lines:
        for line2 in lines:
            if int(line1) + int(line2) == 2020:
                answer = int(line1) * int(line2)

    if answer != 0:
        eval_answer(year, day, 1, answer)


def part2(lines, year, day):
    answer = 0
    
    for line1 in lines:
        for line2 in lines:
            for line3 in lines:
                if int(line1) + int(line2) + int(line3) == 2020:
                    answer = int(line1) * int(line2) * int(line3)
    
    if answer != 0:
        eval_answer(year, day, 2, answer)


if __name__ == "__main__":
    curr_path = os.getcwd().split("/")
    try:
        year = int(curr_path[-2])
        day = int(curr_path[-1])
    except ValueError:
        print("[x] Bad year day values - are you in the right subdir?")
        sys.exit(0)

    if not os.path.exists(".part1tries"):
        os.system("touch .part1tries")
    if not os.path.exists(".part2tries"):
        os.system("touch .part2tries")
    
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    if not os.path.exists(".part1solved"):
        print("[-] Solving Part 1")
        part1(lines, year, day)
    elif os.path.exists(".part1solved") and not os.path.exists(".part2solved"):
        print("[-] Solving Part 2")
        part2(lines, year, day)
    else:
        print("You already have these stars!")
