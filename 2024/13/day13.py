import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

import re
from lib import puzzle_run


def get_tokens(a_x, a_y, b_x, b_y, p_x, p_y):
    a_press = 0
    b_press = 0

    # pt 1 bruteforce
    # presses = []
    # max_presses = 100
    # for a in range(max_presses):
    #     for b in range(max_presses):
    #         if (a_x * a + b_x * b == p_x) and (a_y * a + b_y * b == p_y):
    #             presses.append((a, b))
    # if presses:
    #     if len(presses) == 1:
    #         a_press = presses[0][0]
    #         b_press = presses[0][1]
    #     else:
    #         print("got to more than one set of presses")
    #         print(f"{presses = }")

    # https://en.wikipedia.org/wiki/System_of_linear_equations
    # Using systems of linear equations and solving for the number of apresses and bpresses, we
    # can deduce the necessary formulas to solve for each of the number of required presses.
    a_press = (((p_x * b_y) - (p_y * b_x)) / ((a_x * b_y) - (a_y * b_x)))
    b_press = ((p_x - (a_x * a_press)) / b_x)

    # only whole button presses count here
    if (a_press % 1 == 0) and (b_press % 1 == 0):
        return int((a_press * 3) + b_press)
    else:
        return 0


def part1(lines):
    answer = 0

    for line in lines:
        if "Button A" in line:
            a_x = int(re.findall("X\+(\d+),", line)[0])
            a_y = int(re.findall("Y\+(\d+)", line)[0])
        elif "Button B" in line:
            b_x = int(re.findall("X\+(\d+),", line)[0])
            b_y = int(re.findall("Y\+(\d+)", line)[0])
        elif "Prize" in line:
            p_x = int(re.findall("X=(\d+),", line)[0])
            p_y = int(re.findall("Y=(\d+)", line)[0])
        else:
            answer += get_tokens(a_x, a_y, b_x, b_y, p_x, p_y)

    answer += get_tokens(a_x, a_y, b_x, b_y, p_x, p_y)

    return answer


def part2(lines):
    answer = 0

    for l_idx, line in enumerate(lines):
        if "Button A" in line:
            a_x = int(re.findall("X\+(\d+),", line)[0])
            a_y = int(re.findall("Y\+(\d+)", line)[0])
        elif "Button B" in line:
            b_x = int(re.findall("X\+(\d+),", line)[0])
            b_y = int(re.findall("Y\+(\d+)", line)[0])
        elif "Prize" in line:
            p_x = int(re.findall("X=(\d+),", line)[0]) + 10000000000000
            p_y = int(re.findall("Y=(\d+)", line)[0]) + 10000000000000
        else:
            answer += get_tokens(a_x, a_y, b_x, b_y, p_x, p_y)

    answer += get_tokens(a_x, a_y, b_x, b_y, p_x, p_y)

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, True)
    except KeyboardInterrupt:
        print("")
