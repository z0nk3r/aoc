"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
import time

def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    regs = {'A': 0, 'B': 0, 'C': 0}
    progs = []
    stdout = []

    for line in lines:
        if 'A:' in line:
            regs['A'] = int(line.split(': ')[1])
        elif 'B:' in line:
            regs['B'] = int(line.split(': ')[1])
        elif 'C:' in line:
            regs['C'] = int(line.split(': ')[1])
        elif 'Program:' in line:
            progs = [int(prog) for prog in line.split(': ')[1].split(',')]

    eip = 0
    while eip < len(progs):
        opcode = progs[eip]
        operand = progs[eip + 1]
        if operand == 4:
            combo = regs['A']
        elif operand == 5:
            combo = regs['B']
        elif operand == 6:
            combo = regs['C']
        else:
            combo = operand
        match opcode:
            case 0:  # adv
                res = int(regs['A'] >> combo)
                regs['A'] = res
            case 1:  # bxl
                res = regs['B'] ^ operand
                regs['B'] = res
            case 2:  # bst
                res = combo % 8
                regs['B'] = res
            case 3:  # jnz
                if regs['A'] != 0:
                    eip = operand - 2
            case 4:  # bxc
                res = regs['B'] ^ regs['C']
                regs['B'] = res
            case 5:  # out
                res = combo % 8
                stdout.append(res)
            case 6:  # bdv
                res = int(regs['A'] >> combo)
                regs['B'] = res
            case 7:  # cdv
                res = int(regs['A'] >> combo)
                regs['C'] = res
            case _:  # fallthru
                pass

        eip += 2

    answer = ','.join([str(char) for char in stdout])
    return answer


def recurs_pt2(progs, p_stack, total):
    if p_stack == []:
        return total

    regs = {'A': 0, 'B': 0, 'C': 0}

    for tot in range(8):
        regs['A'] = total << 3 | tot
        regs['B'] = 0
        regs['C'] = 0
        target = None

        for eip in range(0, len(progs) - 2, 2):
            opcode = progs[eip]
            operand = progs[eip + 1]
            if operand == 4:
                combo = regs['A']
            elif operand == 5:
                combo = regs['B']
            elif operand == 6:
                combo = regs['C']
            else:
                combo = operand

            match opcode:
                case 0:  # adv
                    pass
                case 1:  # bxl
                    res = regs['B'] ^ operand
                    regs['B'] = res
                case 2:  # bst
                    res = combo % 8
                    regs['B'] = res
                case 3:  # jnz
                    pass
                case 4:  # bxc
                    res = regs['B'] ^ regs['C']
                    regs['B'] = res
                case 5:  # out
                    res = combo % 8
                    target = res
                case 6:  # bdv
                    res = int(regs['A'] >> combo)
                    regs['B'] = res
                case 7:  # cdv
                    res = int(regs['A'] >> combo)
                    regs['C'] = res
                case _:  # fallthru
                    pass

            if target == p_stack[-1]:
                parent = recurs_pt2(progs, p_stack[:-1], regs['A'])
                if parent is None:
                    continue
                return parent

def part2(lines):
    '''Function to solve part 2'''
    answer = 0
    progs = []

    for line in lines:
        if 'Program:' in line:
            progs = [int(prog) for prog in line.split(': ')[1].split(',')]

    answer = recurs_pt2(progs, progs, 0)
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
