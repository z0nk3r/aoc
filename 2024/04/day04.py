import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_setup, puzzle_run
import numpy as np


def part1(lines):
    answer = 0

    matrix = [list(line) for line in lines]
    matrix = np.array(matrix)

    for _ in range(4):

        for ridx in range(len(matrix)):
            for cidx in range(len(matrix[0])):
                if matrix[ridx][cidx] == 'X':
                    # horiz right
                    try:
                        if (matrix[ridx    ][cidx + 1] == 'M' and
                            matrix[ridx    ][cidx + 2] == 'A' and
                            matrix[ridx    ][cidx + 3] == 'S'):
                            answer += 1
                    except (IndexError, ValueError):
                        pass

                    # diag down right
                    try:
                        if (matrix[ridx + 1][cidx + 1] == 'M' and
                            matrix[ridx + 2][cidx + 2] == 'A' and
                            matrix[ridx + 3][cidx + 3] == 'S'):
                            answer += 1
                    except (IndexError, ValueError):
                        pass

        matrix = np.rot90(matrix)

    return answer


def part2(lines):
    answer = 0

    matrix = [list(line) for line in lines]
    matrix = np.array(matrix)

    for _ in range(4):

        for ridx in range(len(matrix)):
            for cidx in range(len(matrix[0])):
                if matrix[ridx][cidx] == 'M':
                    try:
                        if (matrix[ridx    ][cidx + 2] == 'M' and
                            matrix[ridx + 1][cidx + 1] == 'A' and
                            matrix[ridx + 2][cidx    ] == 'S' and
                            matrix[ridx + 2][cidx + 2] == 'S'):
                            answer += 1
                    except (IndexError, ValueError):
                        pass

        matrix = np.rot90(matrix)

    return answer


if __name__ == "__main__":
    year, day = puzzle_setup()

    lines = [line.replace("\n", "") for line in open(0).readlines()]

    puzzle_run(part1, part2, lines, year, day)
