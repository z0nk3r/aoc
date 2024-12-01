import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_setup, puzzle_run


def part1(lines):
    answer = 0
    
    for line in lines:
        print(line)
    
    '''
    solve part 1 of the problem here
    # answer = <the answer to the problem>
    '''
    return answer


def part2(lines):
    answer = 0
    
    for line in lines:
        print(line)
    
    '''
    solve part 2 of the problem here
    # answer = <the answer to the problem>
    '''
    return answer


if __name__ == "__main__":
    year, day = puzzle_setup()

    lines = [line.replace("\n", "") for line in open(0).readlines()]

    puzzle_run(part1, part2, lines, year, day)
