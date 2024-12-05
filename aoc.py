import datetime
import os
import shutil
import sys
import time
import webbrowser

from lib import (
    setup_session,
    session_get_file,
    reload_cookie,
    time_to_release,
    print_countdown,
    get_yearday,
)

# ported from https://github.com/morgoth1145/advent-of-code/blob/8c17e50b4067d00a5ccc0753b1a0a7289e3f20e5/lib/aoc.py


def get_puzzle(year: str, day: str) -> bool:
    """Get the puzzle file from the advent of code website. Loads the username, cookie, and makes the session_get_file request. Returns True/False on success."""
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    dest_path = f"{year}/{day:02}/input"

    print(f"[-] Downloading Puzzle Input for {year} Day {day} to ", end="")
    print(f'"./{year}/{day:02}/input"')

    if not os.path.exists(f"{year}"):
        os.makedirs(f"{year}")
    if not os.path.exists(f"{year}/{day:02}"):
        os.makedirs(f"{year}/{day:02}")

    _s = setup_session()

    bad_counter = 0
    while not session_get_file(_s, dest_path, url):
        # The session cookie may be invalid?
        os.unlink(dest_path)  # delete file
        reload_cookie()
        bad_counter += 1
        if bad_counter == 5:
            print("[x] Bad Puzzle Input Get - Try Again Later")
            return False

    return True


def setup_env(year: str, day: str) -> None:
    """Makes a copy of the template into the current challenge's subdirectory and opens it in vscode"""
    dest_path = f"{year}/{day:02}/"
    dest_file = f"day{day:02}.py"
    print(f'[-] Setting up environment for challenge in "./{year}/{day:02}/"')

    # os.copy template down to dest_path
    if not os.path.exists(f"{dest_path}/{dest_file}"):
        shutil.copy("template.py", f"{dest_path}/{dest_file}")

    # open puzzle and working file with `code -r`
    os.system(f"code -r {dest_path}/{dest_file}")
    os.system(f"code -r {dest_path}/input")

    # open the site
    webbrowser.open(f"https://adventofcode.com/{year}/day/{day}")


def download_input_when_live(year: str, day: str) -> None:
    """Countdown blocking function - wait if puzzle not yet available"""

    # Download 2 seconds after release
    to_wait = time_to_release(year, day) + datetime.timedelta(seconds=2)
    to_wait_seconds = int(to_wait.total_seconds())

    # countdown loop
    while to_wait_seconds > 0:
        time.sleep(1)
        to_wait_seconds -= 1
        print_countdown(to_wait_seconds, "Puzzle is Available")

        # recalc the waittime every so often to account for potential drift of time
        if (to_wait_seconds % 300) == 0:  # every 5 minutes
            to_wait = time_to_release(year, day) + datetime.timedelta(seconds=2)
            to_wait_seconds = int(to_wait.total_seconds())
    print("")


def print_usage() -> None:
    """Print the Usage/how-to line"""
    print("\nUsage:\n  $> python3 aoc.py [<year> <day>] [-a]\n")


def main() -> None:
    year = -1
    day = -1

    try:
        if sys.argv[1] == "-a":
            year, day = get_yearday()
            if year == -2 or day == -2:
                print("[x] Automagic datecalc failed.")
                return
            print(f"[!] Auto-Grabber: Next Puzzle is {year} {day:02}")
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
                if get_puzzle(year, day):
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
