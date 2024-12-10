import sys

from lib import AoCSession, YeardayError, CUE


def print_usage() -> None:
    """Print the Usage/how-to line"""
    print("\nUsage:\n  $> python3 aoc.py [<year> <day>] [-a]\n")


def main() -> None:

    aoc = None

    try:
        if "-a" in sys.argv:
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