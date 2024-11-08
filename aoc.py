import os
import sys
import time
import requests
import datetime
import dateutil.tz

from typing import Tuple

# ported from https://github.com/morgoth1145/advent-of-code/blob/8c17e50b4067d00a5ccc0753b1a0a7289e3f20e5/lib/aoc.py


def forget_cookie(_s: requests.Session) -> None:
    """Delete the Cookie for the Session"""
    del _s.cookies["session"]


def load_cookie(_s: requests.Session, bad: bool) -> None:
    """Load the Cookie from disk and add to session. If it doesn't exist, user is prompted."""
    cookie_file = "cookie.txt"
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


def load_username() -> str:
    """Load the Username for User-Agent strings from disk. If it doesn't exist, user is prompted."""
    username_file = "username.txt"
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


def get_input(year: str, day: str) -> bool:
    """Get the puzzle file from the advent of code website. Loads the username, cookie, and makes the session_get_file request. Returns True/False on success."""
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    dest_path = f"{year}/{day:02}/input"

    print(f"\n[-] Downloading Puzzle Input for {year} Day {day} to ", end="")
    print(f'"{os.getcwd()}/{year}/{day:02}/input"')

    if not os.path.exists(f"{year}"):
        os.makedirs(f"{year}")
    if not os.path.exists(f"{year}/{day:02}"):
        os.makedirs(f"{year}/{day:02}")

    _s = requests.Session()

    username = load_username()
    _s.headers.update({"User-Agent": f"github.com/{username}"})

    load_cookie(_s, False)
    bad_counter = 0
    while not session_get_file(_s, dest_path, url):
        # The session cookie may be invalid?
        os.unlink(dest_path)  # delete file
        forget_cookie()
        load_cookie(_s, True)
        time.sleep(2)  # avoid potential rate limit
        bad_counter += 1
        if bad_counter == 5:
            print("[x] Bad Puzzle Input Get - Try Again Later")
            return False

    return True


def setup_env(year: str, day: str) -> None:
    """Makes a copy of the template into the current challenge's subdirectory and opens it in vscode"""
    # [ ] TODO: Setup Working Environment Automagically with VSCode
    dest_path = f"{year}/{day:02}/"
    dest_file = f"day{day:02}.py"
    print(f"[-] Setting up environment for challenge in {os.getcwd()}/{year}/{day:02}/")

    # os.copy template down to dest_path

    # rename template to destfile

    # open dest_path/dest_file with `code -r`


def time_to_release(year: str, day: str) -> datetime.datetime:
    """Calculates the time to release of the requested puzzle on (year) and (day)"""

    # Puzzles release at midnight EST (UTC-5)
    release_time = datetime.datetime(
        year=year, month=12, day=day, hour=5, tzinfo=dateutil.tz.tzutc()
    )
    now = datetime.datetime.now(dateutil.tz.tzutc())
    return release_time - now


def print_countdown(to_wait_seconds: int) -> None:
    """Takes the time to release (to_wait_seconds) and prints the associated countdown to the terminal"""
    days = int(to_wait_seconds // 86400)
    hrs = int((to_wait_seconds - (days * 86400)) // 3600)
    mins = int((to_wait_seconds - (days * 86400) - (hrs * 3600)) // 60)
    secs = int((to_wait_seconds - (days * 86400) - (hrs * 3600) - mins * 60))
    print(
        f"\r [x] {days:4}D, {hrs:02}H, {mins:02}M, {secs:02}S until Puzzle is Available. Waiting... ",
        end="",
        flush=True,
    )


def download_input_when_live(year: str, day: str) -> None:
    """Countdown blocking function - wait if puzzle not yet available"""

    # Download 2 seconds after release
    to_wait = time_to_release(year, day) + datetime.timedelta(seconds=2)
    to_wait_seconds = int(to_wait.total_seconds())

    # countdown loop
    while to_wait_seconds > 0:
        time.sleep(1)
        to_wait_seconds -= 1
        print_countdown(to_wait_seconds)

        # recalc the waittime every so often to account for potential drift of time
        if (to_wait_seconds % 300) == 0:  # every 5 minutes
            to_wait = time_to_release(year, day) + datetime.timedelta(seconds=2)
            to_wait_seconds = int(to_wait.total_seconds())


def autocalc_yearday() -> Tuple[int, int]:
    """
    When using the '-a' cli opt, auto figure out year and day of next challenge.
    If its before Dec 1st , return current year, and 1.
    if its after dec 25th, return next year and 1.
    Otherwise, return current year, current day + 1.
    """

    # [ ] TODO: Use the Datetime.datetime lib; placeholder retvals until complete
    return 2024, 1


def print_usage() -> None:
    """Print the Usage/how-to line"""
    print("\nUsage:\n  $> python3 aoc.py [<year> <day>] [-a]\n")


def main() -> None:
    year = -1
    day = -1

    try:
        if sys.argv[1] == "-a":
            year, day = autocalc_yearday()
        elif len(sys.argv) != 3:
            print("[x] Not all or too many arguments provided")
            print_usage()
            return
    except IndexError:
        print("[x] Not all or too many arguments provided")
        print_usage()
        return

    try:
        if year == -1 and day == -1:
            year = int(sys.argv[1])
            day = int(sys.argv[2])

        if 2030 > year > 2015 and 0 < day < 26:
            try:
                download_input_when_live(year, day)
                if get_input(year, day):
                    setup_env(year, day)
            except KeyboardInterrupt:
                print("\nQuitting!")
        else:
            print(f"[x] Invalid Year or Day Given: {year} {day}")
            print(
                "[x] Must be in year range 2015 - 2030, and in the day range of the 1st - 25th"
            )
            print_usage()

    except ValueError:
        print(f"[x] Invalid Arguments provided: {sys.argv[1]} {sys.argv[2]}")
        print_usage()


if __name__ == "__main__":
    main()
