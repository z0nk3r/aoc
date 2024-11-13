import os
import sys
import re
import time
import requests
import datetime
import traceback

from typing import Tuple, Union, Callable, List

import dateutil.tz

# ported from https://github.com/morgoth1145/advent-of-code/blob/8c17e50b4067d00a5ccc0753b1a0a7289e3f20e5/lib/aoc.py


def _forget_cookie(_s: requests.Session) -> None:
    """Delete the Cookie for the Session"""
    del _s.cookies["session"]


def _load_cookie(_s: requests.Session, bad: bool) -> None:
    """Load the Cookie from disk and add to session. If it doesn't exist, user is prompted."""
    stack = traceback.extract_stack()
    lib_dir = f"{os.path.dirname(stack[-2].filename)}"
    cookie_file = f"{lib_dir}/cookie.txt"
    if not os.path.exists(cookie_file) or bad == True:
        prompt = """
    Copy/Paste Cookie from the AoC Website
    After Logging into AoC:
    Chrome: Right-click Page > Inspect > Application > Storage > Cookies > https://adventofcode.com > Value
    (It's a SHA-512, 128 chars long) (Cookie will Cache locally, should only have to do this once per login)

    => """
        cookie = input(prompt)
        cfile = open(cookie_file, "w")
        cfile.write(cookie)
        cfile.close()

    with open(cookie_file) as cfile:
        rcookie = cfile.readline().rstrip("\n")
    _s.cookies["session"] = rcookie


def reload_cookie(_s: requests.Session) -> None:
    """Forget and reload the cookie for the Session"""
    _forget_cookie()
    _load_cookie(_s, True)
    time.sleep(2)  # avoid potential rate limit


def _load_username() -> str:
    """Load the Username for User-Agent strings from disk. If it doesn't exist, user is prompted."""
    stack = traceback.extract_stack()
    lib_dir = f"{os.path.dirname(stack[-2].filename)}"
    username_file = f"{lib_dir}/username.txt"
    if not os.path.exists(username_file):
        prompt = """
    Enter your username for the User-Agent string (Will cache locally, should only have to do this once)

    => """
        username = input(prompt)
        ufile = open(username_file, "w")
        ufile.write(username)
        ufile.close()

    with open(username_file) as ufile:
        rusername = ufile.readline().rstrip("\n")

    return rusername


def setup_session() -> requests.Session:
    _s = requests.Session()

    username = _load_username()
    _s.headers.update({"User-Agent": f"github.com/{username}"})

    _load_cookie(_s, False)

    return _s


def session_get_file(_s: requests.Session, dest_path: str, url: str) -> bool:
    """Using the associated Session, get the puzzle file. Returns True/False on success."""
    notLoggedInErr = (
        "Puzzle inputs differ by user.  Please log in to get your puzzle input."
    )
    tooEarlyErr = "Please don't repeatedly request this endpoint before it unlocks! The calendar countdown is synchronized with the server time; the link will be enabled on the calendar the instant this puzzle becomes available."

    r = _s.get(url)
    if r.status_code != 400:
        # There isn't a client error so we *should* be logged in?
        r.raise_for_status()
        contents = r.content
        if str(r.content) != notLoggedInErr and str(r.content) != tooEarlyErr:
            # The contents are good! (I think)
            destfile = open(dest_path, "wb")
            destfile.write(r.content)
            destfile.close()
            print("[-] Download Complete!")
            return True

    return False


def time_to_release(year: str, day: str) -> datetime.datetime:
    """Calculates the time to release of the requested puzzle on (year) and (day)"""

    # Puzzles release at midnight EST (UTC-5)
    release_time = datetime.datetime(
        year=year, month=12, day=day, hour=5, tzinfo=dateutil.tz.tzutc()
    )
    now = datetime.datetime.now(dateutil.tz.tzutc())
    return release_time - now


def print_countdown(to_wait_seconds: int, message: str) -> None:
    """Takes the time to release (to_wait_seconds) and prints the associated countdown to the terminal"""
    days = int(to_wait_seconds // 86400)
    hrs = int((to_wait_seconds - (days * 86400)) // 3600)
    mins = int((to_wait_seconds - (days * 86400) - (hrs * 3600)) // 60)
    secs = int((to_wait_seconds - (days * 86400) - (hrs * 3600) - mins * 60))
    print(
        f"\r [x] {days:4}D, {hrs:02}H, {mins:02}M, {secs:02}S until {message}. Waiting... ",
        end="",
        flush=True,
    )


def _submit_answer(year, day, part, answer) -> Tuple[bool, Union[str, None]]:
    """Submit an answer"""

    _s = setup_session()

    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    r = _s.post(url, data={"level": part, "answer": str(answer)})
    r.raise_for_status()

    if day == 25 and part == 2:
        return True, None

    TOO_RECENT_KEY = "You gave an answer too recently"
    BAD_ANSWER_KEYS = [
        "That's not the right answer",
        "You don't seem to be solving the right level",
    ]
    GOOD_ANSWER_KEY = "That's the right answer!"
    for line in r.text.splitlines():
        if GOOD_ANSWER_KEY in line:
            # print(line)
            return True, line  # Good answer
        if TOO_RECENT_KEY in line:
            # print(line)
            return False, line
        for k in BAD_ANSWER_KEYS:
            if k in line:
                # print(line)
                return False, line

    print("Bad request!")
    assert False


def _aoc_timeout(answer_line: str) -> None:
    """When giving an incorrect answer, or answer too may times to quickly, a self-induced timeout occurs based on the returned message"""
    m = re.search("lease wait (.*) before trying again", answer_line)
    if m is None:
        print(
            "Warning: Cannot detect timeout from answer line. Defaulting to 1 minute."
        )
        timeout = datetime.timedelta(minutes=1)
    else:
        timeout = {
            "one minute": datetime.timedelta(minutes=1),
            "5 minutes": datetime.timedelta(minutes=5),
        }.get(m.group(1))
        if timeout is None:
            print(
                f'Warning: Cannot detect timeout from "{m.group(1)}". Defaulting to 1 minute.'
            )
            timeout = datetime.timedelta(minutes=1)
        else:
            print(f"Timeout of {timeout} due to bad answer...")

    timeout_seconds = int(timeout.total_seconds())

    while timeout_seconds > 0:
        time.sleep(1)
        timeout_seconds -= 1
        print_countdown(timeout_seconds, "Timeout is Over")


def _check_if_old_answer(part: int, answer: int) -> bool:
    """Checks old answers if current answer has already been attempted"""
    given_answers = [
        int(line.replace("\n", "")) for line in open(f".part{part}tries").readlines()
    ]
    return answer in given_answers


def _add_to_answers(part: int, answer: int) -> None:
    """Adds a bad answer to the local cache of bad answers"""
    with open(f".part{part}tries", "a") as given_answers:
        given_answers.write(f"{answer}\n")


def eval_answer(year: int, day: int, part: int, answer: int) -> None:
    """Evaluates the provided answer. Auto submits answer, and evals if correct or incorrect"""
    print(f"[-] Attempting answer of {answer} for {year} {day:02} - part {part}")

    if _check_if_old_answer(part, answer):
        print("[!] You already tried this answer!")
        return

    _add_to_answers(part, answer)

    b_submit, response = _submit_answer(year, day, part, answer)
    if b_submit:
        os.system(f"touch .part{part}solved")
        print(f"[-] {part}. {answer} - Correct! {'⭐' * int(part)}")
    else:
        if "already complete it" in response:
            os.system(f"touch .part{part}solved")
            print(f"[!] You already have this star! {'⭐'*int(part)}")
        else:
            print(f"[x] {part} - {answer} was incorrect.")
            print(f"{response = }")
            _aoc_timeout(response)
            print("\n")


def get_yearday(path: str = "") -> Tuple[int, int]:
    """
    When used as part of a solution attempt (in the template), get_yearday will
    use current working directory to get the year and day.

    Alternatively, When using the '-a' cli opt, auto figure out year and day of next challenge.
    If its before Dec 1st , return current year, and 1.
    if its after dec 25th, return next year and 1.
    Otherwise, return current year, current day + 1.
    """
    year = -2
    day = -2

    if path != "":
        curr_path = path.split("/")
        try:
            year = int(curr_path[-2])
            day = int(curr_path[-1])
        except ValueError:
            print("[x] Bad year day values - are you in the right subdir?")

    else:
        now = datetime.datetime.now(dateutil.tz.tzutc()) + datetime.timedelta(hours=-5)
        if now.month < 12:
            year = now.year
            day = 1

        elif now.month == 12 and day >= 25:
            year = now.year + 1
            day = 1

        else:
            year = now.year
            day = now.day + 1

    return year, day

def puzzle_setup() -> Tuple[int, int]:
    '''Sets up a puzzle'''
    year, day = get_yearday(os.getcwd())
    if year == -2 or day == -2:
        sys.exit(0)
    
    if not os.path.exists(".part1tries"):
        os.system("touch .part1tries")
    if not os.path.exists(".part2tries"):
        os.system("touch .part2tries")
    
    return year, day

def puzzle_run(part1: Callable[[List[str], int, int], None], part2: Callable[[List[str], int, int], None], lines: List[str], year: int, day: int) -> None:
    '''Runs a puzzle'''
    if not os.path.exists(".part1solved"):
        print(f"[-] Solving Part 1 for {year} {day}")
        part1(lines, year, day)
    elif os.path.exists(".part1solved") and not os.path.exists(".part2solved"):
        print(f"[-] Solving Part 2 for {year} {day}")
        part2(lines, year, day)
    else:
        print(f"You already have all of the stars for {year} {day}!")