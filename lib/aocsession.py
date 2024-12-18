'''Module that contains the AoCSession Class and YeardayError Exception'''

import datetime
import os
import re
import shutil
import time
import traceback
import webbrowser
from typing import Callable, List, Tuple, Union

import dateutil.tz
import requests

from .utils import (CUE, add_to_answers, aoc_timeout, check_if_old_answer,
                    check_test_answer, print_countdown, read_input)

# ported from:
# https://github.com/morgoth1145/advent-of-code/blob/8c17e50b4067d00a5ccc0753b1a0a7289e3f20e5/lib/aoc.py


class YeardayError(Exception):
    """Raise for yearday Exceptions in AocSession._get_yearday()"""
    def __init__(self, message):
        super().__init__()
        self.message = message
    def __str__(self):
        return str(self.message)


class AoCSession:
    '''The Advent of Code Session'''

    def __init__(self, yearday_path: str = ""):
        '''Instantiation of the Advent of Code Session'''
        self.username = ""
        self.year = 0
        self.day = 0
        self.session = self._setup_session()
        self.time_padding = 1

        self._load_username()
        self._get_yearday(yearday_path)


    def _load_username(self) -> str:
        """
        Load the Username for User-Agent strings from disk.

        If it doesn't exist, user is prompted.
        """
        stack = traceback.extract_stack()
        lib_dir = f"{os.path.dirname(stack[-2].filename)}"
        username_file = f"{lib_dir}/username.txt"
        if not os.path.exists(username_file):
            prompt = f"""
        Enter your username for the User-Agent string (Will cache locally, should only have to do this once)

        {CUE.PROMPT} """
            username = input(prompt)
            with open(username_file, "w", encoding="utf-8") as ufile:
                ufile.write(username)
                ufile.close()

        with open(username_file, "r", encoding="utf-8") as ufile:
            rusername = ufile.readline().rstrip("\n")

        self.username = rusername


    def _get_yearday(self, path: str = "") -> None:
        """
        When used as part of a solution attempt, get_yearday will
        use current working directory to get the year and day.

        Alternatively, When using the '-a' cli opt, auto figure out year and day of next challenge.
        If its before Dec 1st , return current year, and 1.
        if its after Dec 25th, return next year and 1.
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
                print(f"{CUE.FAIL} Bad year day values - are you in the right subdir?")

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

        if not 2014 < year <= 2035:
            raise YeardayError(f"Year '{year}' out of standard range (between 2015 and 2035)")
        if not 0 < day <= 25:
            raise YeardayError(f"Day '{day}' out of standard range (between 1 and 25)")

        self.year = year
        self.day = day


    def _setup_session(self) -> requests.Session:
        '''Setup the internal session with requests module and establish cookies'''
        _s = requests.Session()
        _s.headers.update({"User-Agent": f"github.com/{self.username}"})
        self._load_cookie(False, _s)
        return _s


    def _forget_cookie(self) -> None:
        """Delete the Cookie for the Session"""
        del self.session.cookies["session"]


    def _load_cookie(self, bad: bool, _s: requests.Session = None) -> None:
        """Load the Cookie from disk and add to session. If it doesn't exist, user is prompted."""
        stack = traceback.extract_stack()
        lib_dir = f"{os.path.dirname(stack[-2].filename)}"
        cookie_file = f"{lib_dir}/cookie.txt"

        if not os.path.exists(cookie_file) or bad is True:
            prompt = f"""
        Copy/Paste Cookie from the AoC Website
        After Logging into AoC:
        Chrome: Right-click Page > Inspect > Application > Storage > Cookies > https://adventofcode.com > Value
        (It's a SHA-512, 128 chars long) (Cookie will Cache locally, should only have to do this once per login)

        {CUE.PROMPT} """
            cookie = input(prompt)
            with open(cookie_file, "w", encoding="utf-8") as cfile:
                cfile.write(cookie)

        with open(cookie_file, "r", encoding="utf-8") as cfile:
            rcookie = cfile.readline().rstrip("\n")

        if _s is None:
            self.session.cookies["session"] = rcookie
        else:
            _s.cookies["session"] = rcookie


    def _reload_cookie(self) -> None:
        """Forget and reload the cookie for the Session"""
        self._forget_cookie()
        self._load_cookie(True)
        time.sleep(self.time_padding)  # avoid potential rate limit


    def _get_request(self, url: str) -> Union[bytes, None]:
        not_loggedin_err = "differ by user.  Please log in"
        too_early_err = "repeatedly request this endpoint before it unlocks! The calendar countdown"

        res = self.session.get(url)
        if res.status_code != 400:
            # There isn't a client error so we *should* be logged in?
            res.raise_for_status()
            if not_loggedin_err not in str(res.content) and too_early_err not in str(res.content):
                # The contents are good! (I think)
                return res.content

        return ""


    def get_input(self, dest_path: str, url: str) -> bool:
        """Using the associated Session, get the puzzle file. Returns True/False on success."""

        puzzle_input = self._get_request(url)
        if puzzle_input is not None:
            with open(dest_path, "wb") as destfile:
                destfile.write(puzzle_input)
                destfile.close()
                print(f"{CUE.GOOD} Download Complete!")
                return True

        return False

    def get_puzzle(self) -> bool:
        """Get the puzzle file from the advent of code website. Returns True/False on success."""
        url = f"https://adventofcode.com/{self.year}/day/{self.day}/input"
        dest_path = f"{self.year}/{self.day:02}/input"

        print(f"{CUE.INFO} Downloading Puzzle Input for {self.year} Day {self.day} to ", end="")
        print(f'"./{self.year}/{self.day:02}/input"')

        if not os.path.exists(f"{self.year}"):
            os.makedirs(f"{self.year}")
        if not os.path.exists(f"{self.year}/{self.day:02}"):
            os.makedirs(f"{self.year}/{self.day:02}")

        bad_counter = 0
        while not self.get_input(dest_path, url):
            # The session cookie may be invalid?
            os.unlink(dest_path)  # delete file
            self._reload_cookie()
            bad_counter += 1
            if bad_counter == 5:
                print(f"{CUE.FAIL} Bad Puzzle Input Get - Try Again Later")
                return False

        return True


    def get_test_answers(self) -> bool:
        '''Scrape the example test answers from the webpage'''

        url = f"https://adventofcode.com/{self.year}/day/{self.day}"
        webpage = self._get_request(url)
        if webpage is not None:
            t_answers = re.findall(r"<code><em>((\d+,?)+)</em></code>", str(webpage))
            with open(".test_answers", "w", encoding="utf-8") as testfile:
                for t_ans in t_answers:
                    testfile.write(f'{t_ans[0]}\n')
            return True

        return False


    def setup_env(self) -> None:
        """
        Makes a copy of the template into the current
        challenge's subdirectory and opens it in vscode
        """
        dest_path = f"{self.year}/{self.day:02}/"
        dest_file = f"day{self.day:02}.py"
        print(f'{CUE.INFO} Setting up environment for challenge in "./{self.year}/{self.day:02}/"')

        # os.copy template down to dest_path
        if not os.path.exists(f"{dest_path}/{dest_file}"):
            shutil.copy("template.py", f"{dest_path}/{dest_file}")

        # open puzzle and working file with `code -r`
        os.system(f"code -r {dest_path}/{dest_file}")
        os.system(f"code -r {dest_path}/input")
        os.system(f"code -r {dest_path}/test")

        # open the site
        webbrowser.open(f"https://adventofcode.com/{self.year}/day/{self.day}")


    def wait_for_live(self) -> None:
        """Countdown blocking function - wait if puzzle not yet available"""
        print_spacer = False

        # Download 2 seconds after release
        to_wait = self.time_to_release() + datetime.timedelta(seconds=self.time_padding)
        to_wait_seconds = int(to_wait.total_seconds())

        # countdown loop
        while to_wait_seconds > 0:
            print_spacer = True
            time.sleep(1)
            to_wait_seconds -= 1
            print_countdown(to_wait_seconds, "Puzzle is Available")

            # recalc the waittime every so often to account for potential drift of time
            if (to_wait_seconds % 300) == 0:  # every 5 minutes
                to_wait = self.time_to_release() + datetime.timedelta(seconds=self.time_padding)
                to_wait_seconds = int(to_wait.total_seconds())

        if print_spacer:
            print("")


    def time_to_release(self) -> datetime.datetime:
        """Calculates the time to release of the requested puzzle on (year) and (day)"""

        # Puzzles release at midnight EST (UTC-5)
        release_time = datetime.datetime(
            year=self.year, month=12, day=self.day, hour=5, tzinfo=dateutil.tz.tzutc()
        )
        now = datetime.datetime.now(dateutil.tz.tzutc())
        return release_time - now


    def submit_answer(self, part: int, answer: str) -> Tuple[bool, Union[str, None]]:
        """Submit an answer"""

        url = f"https://adventofcode.com/{self.year}/day/{self.day}/answer"
        res = self.session.post(url, data={"level": part, "answer": str(answer)})
        res.raise_for_status()

        if self.day == 25 and part == 2:
            return True, None

        too_recent_key = "You gave an answer too recently"
        bad_answer_keys = [
            "That's not the right answer",
            "You don't seem to be solving the right level",
        ]
        good_answer_key = "That's the right answer!"
        for line in res.text.splitlines():
            if good_answer_key in line:
                # print(line)
                return True, line  # Good answer
            if too_recent_key in line:
                # print(line)
                return False, line
            for k in bad_answer_keys:
                if k in line:
                    # print(line)
                    return False, line

        print(f"{CUE.FAIL} Bad request!")
        assert False


    def pass_the_test(self, part_func: Callable[[List[str]], int]) -> bool:
        '''
        Runs the current attempt against the test data provided in the website's writeup.

        This requires the sample data to be copy-pasted into a 'test' file.
        '''

        print(f"{CUE.INFO} Checking current solution against the test data.")

        if not self.get_test_answers():
            print(f"  {CUE.FAIL} Unable to get test answers. Try again later.")
            return False

        t_input = read_input("test")
        if t_input == [""]:
            print(f"  {CUE.FAIL} 'test' data file does not exist. Re-get it and try again.")
            return False

        answer = part_func(t_input)
        if answer is None:
            print(f"{CUE.FAIL} Test answer of '{answer}' is None, exiting.")
            return False

        if not check_test_answer(answer):
            print(f"  {CUE.FAIL} Test answer '{answer}' is incorrect. Try again.")
            return False

        print(f"  {CUE.GOOD} Test solution passed! ({CUE.CYAN}{answer}{CUE.RESET})")
        return True


    def eval_answer(self, part_func: Callable[[List[str]], int], part: int, bypass: bool) -> None:
        """Evaluates the provided answer. Auto submits answer, and evals if correct or incorrect"""
        print(f"{CUE.INFO} Solving Part {part} for {self.year} {self.day}")


        if not bypass:
            if not self.pass_the_test(part_func):
                return
        else:
            print(f"{CUE.WARN} Skipping the tests for {self.year} {self.day:02} - part {part}")

        answer = part_func(read_input())
        if answer is None:
            print(f"{CUE.FAIL} Real answer of '{answer}' is None, exiting.")
            return

        if answer == 0:
            print(f"{CUE.FAIL} Answer of '{answer}' for {self.year} " +
                  f"{self.day:02} - part {part} given. Auto exiting.")
            return

        print(f"{CUE.INFO} Sending answer of ({CUE.GREEN}{answer}{CUE.RESET}) " +
              f"for {self.year} {self.day:02} - part {part}\n")

        if check_if_old_answer(part, answer):
            print(f"{CUE.WARN} You already tried this answer!")
            return

        b_submit, response = self.submit_answer(part, answer)
        if b_submit:
            add_to_answers(part, answer)
            os.system(f"touch .part{part}solved")
            print(f"{CUE.GOOD} {part}. {answer} - Correct! {'⭐' * int(part)}")
        else:
            if "already complete it" in response:
                os.system(f"touch .part{part}solved")
                print(f"{CUE.GOOD} You already have this star! {'⭐' * int(part)}")
            else:
                add_to_answers(part, answer)
                print(f"{CUE.FAIL} {part} - {answer} was incorrect.")
                print(f"{response = }")
                aoc_timeout(response)
                print("\n")


    def __str__(self):
        return f"{self.year} {self.day:02}"
