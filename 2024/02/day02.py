import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_setup, puzzle_run


def test_line(line):
    dir = line[1] - line[0]

    for i in range(1, len(line)):
        dir_check = ((line[i] - line[i - 1]) * dir) > 0
        line_limit = (1 <= abs(line[i] - line[i - 1]) <= 3)

        if not (dir_check and line_limit):
            return 0

    return 1


def part1(lines):
    answer = 0

    for line in enumerate(lines):
        line = [int(item) for item in line.split(" ")]
        answer += test_line(line)

    return answer


def part2(lines):
    answer = 0

    for lidx, line in enumerate(lines):
        line = [int(item) for item in line.split(" ")]
        poss_answers = [test_line(line[:idx] + line[idx + 1 :]) for idx in range(len(line))]
        print(f"{lidx + 1}: {line} - {poss_answers = }")
        answer += 1 if 1 in poss_answers else 0

    return answer


if __name__ == "__main__":
    year, day = puzzle_setup()

    lines = [line.replace("\n", "") for line in open(0).readlines()]

    puzzle_run(part1, part2, lines, year, day)
