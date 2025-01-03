"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from collections import deque
from functools import cache
from itertools import product


def in_bounds(ridx, cidx, graph):
    row = 0 <= ridx < len(graph)
    col = 0 <= cidx < len(graph[0])
    return row and col


def valid_space(ridx, cidx, graph):
    return graph[ridx][cidx] != None


def gen_coords(given_pad):
    coords = {}
    for ridx, row in enumerate(given_pad):
        for cidx, _ in enumerate(row):
            if given_pad[ridx][cidx] is not None:
                coords[given_pad[ridx][cidx]] = (ridx, cidx)
    return coords


def gen_pattern(given_pad):
    coords = gen_coords(given_pad)
    patts = {}
    
    for row in coords:
        for col in coords:
            if row == col:
                patts[(row, col)] = ['A']
                continue
            queue = []
            queue.append((coords[row], ""))
            pattern = []
            score = 1 << 64
            while queue:
                (ridx, cidx), moves = queue.pop(0)
                for new_r, new_c, new_m in [(ridx - 1, cidx, "^"), (ridx + 1, cidx, "v"), (ridx, cidx - 1, "<"), (ridx, cidx + 1, ">")]:
                    if not in_bounds(new_r, new_c, given_pad):
                        continue
                    if not valid_space(new_r, new_c, given_pad):
                        continue

                    if given_pad[new_r][new_c] == col:
                        if score < len(moves) + 1:
                            break
                        score = len(moves) + 1
                        pattern.append(moves + new_m + 'A')
                    else:
                        queue.append(((new_r, new_c), moves + new_m))
                else:
                    continue
                break
            patts[(row, col)] = pattern
    
    return patts


def input_to_patts(input_str, patts):
    patts_per_step = [patts[(row, col)] for row, col in zip("A" + input_str, input_str)]
    return ["".join(opt) for opt in product(*patts_per_step)]

keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
]

dpad = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]

dpad_seqs = gen_pattern(dpad)
dpad_lengths = {key: len(value[0]) for key, value in dpad_seqs.items()}

@cache
def calc_length(patt, depth=25):  #part1 depth=2; part2 depth=25
    if depth == 1:
        return sum(dpad_lengths[(row, col)] for row, col in zip('A' + patt, patt))

    length = 0

    for row, col in zip('A' + patt, patt):
        length += min(calc_length(subpatt, depth - 1) for subpatt in dpad_seqs[(row, col)])

    return length


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    keypad_seqs = gen_pattern(keypad)

    for line in lines:
        keypad_inputs = input_to_patts(line, keypad_seqs)
        length = min(map(calc_length, keypad_inputs))
        answer += length * int(line[:-1])

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    keypad_seqs = gen_pattern(keypad)

    for line in lines:
        keypad_inputs = input_to_patts(line, keypad_seqs)
        length = min(map(calc_length, keypad_inputs))
        answer += length * int(line[:-1])

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True, refactor=True)
    except KeyboardInterrupt:
        print("")
