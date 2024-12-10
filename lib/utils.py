import os
import sys
import re
import time
import select
import datetime
from enum import Enum

from typing import Callable, List

# ported from https://github.com/morgoth1145/advent-of-code/blob/8c17e50b4067d00a5ccc0753b1a0a7289e3f20e5/lib/aoc.py

class CUE(Enum):
    '''Enum for displaying notification cue cards or other colorful bits in information.\
    \n\n\
    This includes:\n\n\
    cue cards: \n\t\tGOOD, \n\t\tINFO, \n\t\tWARN, \n\t\tPROMPT, and \n\t\tFAIL,\n\n\
    cue colors: \n\t\tGREEN, \n\t\tBLUE, \n\t\tCYAN, \n\t\tYELLOW, \n\t\tRED, and \n\t\tRESET
    '''
    
    def __str__(self):
        return str(self.value)

    GREEN = "\033[1;92m"
    BLUE = "\033[1;94m"
    CYAN = "\033[1;96m"
    YELLOW = "\033[1;93m"
    RED = "\033[1;91m"
    RESET = "\033[0m"

    GOOD = f"{GREEN}[✔]{RESET}"
    INFO = f"{CYAN}[*]{RESET}"
    WARN = f"{YELLOW}[!]{RESET}"
    PROMPT = f"{YELLOW}[>]{RESET}"
    FAIL = f"{RED}[X]{RESET}"


def print_countdown(to_wait_seconds: int, message: str) -> None:
    """Takes the time to release (to_wait_seconds) and prints the associated countdown to the terminal"""
    days = int(to_wait_seconds // 86400)
    hrs = int((to_wait_seconds - (days * 86400)) // 3600)
    mins = int((to_wait_seconds - (days * 86400) - (hrs * 3600)) // 60)
    secs = int((to_wait_seconds - (days * 86400) - (hrs * 3600) - mins * 60))
    print(
        f"\r  {CUE.INFO} {days:4}D, {hrs:02}H, {mins:02}M, {secs:02}S until {message}. Waiting... ",
        end="",
        flush=True,
    )


def aoc_timeout(answer_line: str) -> None:
    """When giving an incorrect answer, or answer too may times to quickly, a self-induced timeout occurs based on the returned message"""
    m = re.search("lease wait (.*) before trying again", answer_line)
    if m is None:
        print(
            "{WARN} Cannot detect timeout from answer line. Defaulting to 1 minute."
        )
        timeout = datetime.timedelta(minutes=1)
    else:
        timeout = {
            "one minute": datetime.timedelta(minutes=1),
            "5 minutes": datetime.timedelta(minutes=5),
            "10 minutes": datetime.timedelta(minutes=10),
        }.get(m.group(1))
        if timeout is None:
            print(
                f'{CUE.WARN} Cannot detect timeout from "{m.group(1)}". Defaulting to 1 minute.'
            )
            timeout = datetime.timedelta(minutes=1)
        else:
            print(f"{CUE.INFO} Timeout of {timeout} due to bad answer...")

    timeout_seconds = int(timeout.total_seconds())

    while timeout_seconds > 0:
        time.sleep(1)
        timeout_seconds -= 1
        print_countdown(timeout_seconds, "Timeout is Over")


def check_if_old_answer(part: int, answer: int) -> bool:
    """Checks old answers if current answer has already been attempted"""
    if not os.path.exists(f".part{part}tries"):
        return False

    given_answers = [
        int(line.replace("\n", "")) for line in open(f".part{part}tries").readlines()
    ]
    return answer in given_answers


def check_test_answer(answer: int) -> bool:
    """Checks test answers if current test answer is correct"""
    if not os.path.exists(f".test_answers"):
        return False

    test_answers = [
        int(line.replace("\n", "")) for line in open(f".test_answers").readlines()
    ]
    return answer in test_answers


def add_to_answers(part: int, answer: int) -> None:
    """Adds a bad answer to the local cache of bad answers"""
    with open(f".part{part}tries", "a") as given_answers:
        given_answers.write(f"{answer}\n")


def read_input(infile: str="input") ->List[str]:
    '''
    Gets the Puzzle input from the local "input" file. 
    Other filenames can be passed as param, "input" is the default.

    If a file is waiting on stdin, read that file instead.
    
    Returns: 
        List of line separated lines with '\\n' removed.
    '''
    if not os.path.exists(infile):
        return [""]

    if infile == "test":
        file = "test"
    else:
        file = infile if not select.select([sys.stdin, ], [], [], 0.0)[0] else 0
    return [line.replace("\n", "") for line in open(file).readlines()]


def puzzle_setup():
    '''Sets up a puzzle'''
    from .aocsession import AoCSession

    aoc = AoCSession(os.getcwd())
    
    if not os.path.exists(".part1tries"):
        os.system("touch .part1tries")
    if not os.path.exists(".part2tries"):
        os.system("touch .part2tries")
    
    return aoc


def puzzle_run(part1: Callable[[List[str]], int], part2: Callable[[List[str]], int]) -> None:
    '''Runs a puzzle'''
    aoc = puzzle_setup()

    if not os.path.exists(".part1solved"):
        aoc.eval_answer(part1, 1)

    elif not os.path.exists(".part2solved"):
        aoc.eval_answer(part2, 2)

    else:
        print(f"{CUE.INFO} You already have all of the stars for {aoc}!")