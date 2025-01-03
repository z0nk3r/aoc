"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from functools import cache

signals = {}

@cache
def get_value(reg):
    try:
        if len(signals[reg]) == 1:
            return int(signals[reg][0])
    except KeyError:
        return -1

    first, oper, second = signals[reg].split(' ')
    
    if oper == "AND":
        return get_value(first) & get_value(second)

    elif oper == "OR":
        return get_value(first) | get_value(second)

    elif oper == "XOR":
        return get_value(first) ^ get_value(second)


def verify_z_reg(reg, r_idx):
    if reg not in signals:
        return False
    
    first, oper, second = signals[reg].split(' ')
    if oper != 'XOR':
        return False
    
    if r_idx == 0:
        return sorted([first, second]) == ['x00', 'y00']
    
    return (verify_xor(first, r_idx) and verify_carry(second, r_idx)) or (verify_xor(second, r_idx) and verify_carry(first, r_idx))


def verify_xor(reg, r_idx):
    if reg not in signals:
        return False

    first, oper, second = signals[reg].split(' ')
    if oper != 'XOR':
        return False
    
    return sorted([first, second]) == [f'x{r_idx:02}', f'y{r_idx:02}']


def verify_carry(reg, r_idx):
    if reg not in signals:
        return False
    
    first, oper, second = signals[reg].split(' ')
    if r_idx == 1:
        if oper != 'AND':
            return False
        return sorted([first, second]) == ['x00', 'y00']
    if oper != 'OR':
        return False
    
    return (verify_subcarry(first, r_idx - 1) and verify_recarry(second, r_idx - 1)) or (verify_subcarry(second, r_idx - 1) and verify_recarry(first, r_idx - 1))


def verify_subcarry(reg, r_idx):
    if reg not in signals:
        return False
    
    first, oper, second = signals[reg].split(' ')
    if oper != 'AND':
        return False
    
    return sorted([first, second]) == [f'x{r_idx:02}', f'y{r_idx:02}']


def verify_recarry(reg, r_idx):
    if reg not in signals:
        return False
    
    first, oper, second = signals[reg].split(' ')
    if oper != 'AND':
        return False
    
    return (verify_xor(first, r_idx) and verify_carry(second, r_idx)) or (verify_xor(second, r_idx) and verify_carry(first, r_idx))


def check_regs():
    r_idx = 0
    while True:
        if not verify_z_reg(f'z{r_idx:02}', r_idx):
            break
        r_idx += 1
    
    return r_idx


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    for line in lines:
        if ': ' in line:
            reg, val = line.split(': ')
            signals[reg] = val
        elif '->' in line:
            oper, reg = line.split(' -> ')
            signals[reg] = oper

    z_vals = []
    z_idx = 0
    while True:
        z_val = str(get_value(f"z{z_idx:02}"))
        if z_val == '-1':
            break
        z_vals.insert(0, z_val)
        z_idx += 1
    answer = int("".join(z_vals), 2)

    get_value.cache_clear()  # for testing to work
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    for line in lines:
        if ': ' in line:
            continue
        elif '->' in line:
            oper, reg = line.split(' -> ')
            signals[reg] = oper

    swaps = []
    for _ in range(4):
        score = check_regs()
        for first_reg in signals:
            for second_reg in signals:
                if first_reg == second_reg:
                    continue
                signals[first_reg], signals[second_reg] = signals[second_reg], signals[first_reg]
                if check_regs() > score:
                    break
                signals[first_reg], signals[second_reg] = signals[second_reg], signals[first_reg]
            else:
                continue
            break
        print("swapped: ", [first_reg, second_reg])
        swaps += [first_reg, second_reg]

    answer = ','.join(sorted(swaps))
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
