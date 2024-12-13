import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run


def part1(lines):
    answer = 0
    floor = 0
    
    for char in lines[0]:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
    
    answer = floor
    return answer


def part2(lines):
    answer = 0
    floor = 0
    for f_idx, char in enumerate(lines[0]):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        
        if floor == -1:
            answer = f_idx + 1
            break

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
