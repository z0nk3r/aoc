"""Main calling Module for starting an Advent of Code puzzle solve"""

import sys
from lib import AoCSession, YeardayError, CUE


def print_usage() -> None:
    """Print the Usage/how-to line"""
    print(f"{CUE.CLEAR_TERM}")
    print(f"{CUE.BOLD}NAME{CUE.RESET}")
    print("\taoc - Advent of Code Auto Puzzle Grabber!")
    print(f"\n{CUE.BOLD}USAGE{CUE.RESET}")
    print(f"\t{CUE.PROMPT} python3 aoc.py ([<year> <day>]|[-a]) -h\n")
    print(f"{CUE.BOLD}OPTIONS{CUE.RESET}")
    print(f"\t{CUE.BOLD}[<year> <day>]{CUE.RESET}")
    print("\t\t- Provide the year and day to setup that specific puzzle")
    print(f"\n\t{CUE.BOLD}-a, --auto{CUE.RESET}")
    print("\t\t- Auto wait for and/or auto pull the next available puzzle")
    print(f"\n\t{CUE.BOLD}-h, --help{CUE.RESET}")
    print("\t\t- Display this help and exit\n")
    print(f"{CUE.BOLD}EXAMPLES{CUE.RESET}")
    print(f"\t{CUE.PROMPT} python3 aoc.py 2020 01")
    print("\t\tGets the Puzzle for year 2020 day 01\n")
    print(f"\t{CUE.PROMPT} python3 aoc.py -a")
    print("\t\tAuto wait countdown will start; once complete the puzzle will be displayed\n")


def main() -> None:
    """Main method for starting a puzzle solve"""
    aoc = None

    try:
        if "-h" in sys.argv or "--help" in sys.argv:
            print_usage()
            return
        if "-a" in sys.argv or "--auto" in sys.argv:
            aoc = AoCSession()
            print(f"{CUE.INFO} Auto-Grabber: Next Puzzle is {aoc}")
        elif len(sys.argv) == 3:
            aoc = AoCSession(f"{sys.argv[1]}/{sys.argv[2]}")
        else:
            print(f"{CUE.FAIL} Invalid arguments provided: {' '.join(sys.argv[1:])}")
            print_usage()
    except IndexError:
        print(f"{CUE.FAIL} Invalid arguments provided")
        print_usage()
    except ValueError:
        print(f"{CUE.FAIL} Invalid arguments provided: {' '.join(sys.argv[1:])}")
        print_usage()
    except YeardayError as exc:
        print(f"{CUE.FAIL} {exc}")
        print_usage()

    if aoc is not None:
        aoc.wait_for_live()
        if aoc.get_puzzle():
            aoc.setup_env()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{CUE.INFO} Quitting!")
