"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from math import floor

def calc_distance(speed, time, rest, total):
    return (floor(total / (time + rest)) * time + min(total % (time + rest), time)) * speed


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    scores = []
    for line in lines:
        _, _, _, speed, _, _, time, _, _, _, _, _, _, rest, _ = line.split()
        scores.append(calc_distance(int(speed), int(time), int(rest), 2503))

    answer = max(scores)

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    deers = dict()
    for line in lines:
        name, _, _, speed, _, _, time, _, _, _, _, _, _, rest, _ = line.split()
        deers[name] = {'wins': 0, 'data': (speed, time, rest)}
    
    for sec in range(1, 2504):
        scores = []
        for deer in deers:
            speed, time, rest = deers[deer]['data']
            scores.append((deer, calc_distance(int(speed), int(time), int(rest), sec)))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        max_score = scores[0][1]
        for score in scores:
            r_name, dist = score
            if dist == max_score:
                deers[r_name]['wins'] += 1

    max_wins = 0
    for deer in deers:
        if deers[deer]['wins'] > max_wins:
            max_wins = deers[deer]['wins']
    answer = max_wins
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
