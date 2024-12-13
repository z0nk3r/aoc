import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run


def part1(lines):
    answer = 0
    lefts = []
    rights = []
    
    for line in lines:
        leftright = line.split('   ')
        lefts.append(int(leftright[0]))
        rights.append(int(leftright[1]))
    
    lefts = sorted(lefts)
    rights = sorted(rights)
    
    for idx, _ in enumerate(lefts):
        if lefts[idx] > rights[idx]:
            answer += (lefts[idx] - rights[idx])
        else:
            answer += (rights[idx] - lefts[idx])

    return answer


def part2(lines):
    answer = 0
    
    lefts = []
    rights = []
    
    for line in lines:
        leftright = line.split('   ')
        lefts.append(int(leftright[0]))
        rights.append(int(leftright[1]))
    
    lefts = sorted(lefts)
    rights = sorted(rights)

    for left in lefts:
        answer += left * rights.count(left)

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
