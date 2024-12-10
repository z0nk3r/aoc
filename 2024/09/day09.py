import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run


def part1(lines):
    answer = 0

    disk = []

    fid = 0
    freespace = False

    for char in lines[0]:
        if not freespace:
            disk += [fid] * int(char)
            fid += 1 
        else:
            disk += ['.'] * int(char)
        freespace = not freespace

    dot_skipper = 0
    for s_idx, spot in enumerate(disk):
        if dot_skipper == disk.count('.') - 1:
            break
        if spot == '.':
            char = disk[-1 - dot_skipper]
            while char == '.':
                dot_skipper += 1
                char = disk[-1 - dot_skipper]
            disk[s_idx] = char
            disk[-1 - dot_skipper] = '.'
        else:
            continue

    for s_idx, spot in enumerate(disk):
        if spot == '.':
            continue
        answer += int(disk[s_idx]) * s_idx

    return answer


def part2(lines):
    answer = 0

    files = dict()
    blanks = []

    fid = 0
    location = 0
    freespace = False

    for char in lines[0]:
        if not freespace:
            files[fid] = (location, int(char))
            fid += 1
        else:
            if int(char) != 0:
                blanks.append((location, int(char)))
        freespace = not freespace
        location += int(char)

    print(f"1: {files = }")

    while fid > 0:
        fid -= 1
        offset, num = files[fid]
        for b_idx, (start, length) in enumerate(blanks):
            if num <= length:
                files[fid] = (start, num)
                if num == length:
                    blanks.pop(b_idx)
                else:
                    blanks[b_idx] = (start + num, length - num)
                break
            if start >= offset:
                blanks = blanks[:b_idx]
                break

    print(f"2: {files = }")


    for fid, (offset, num) in files.items():
        for o_idx in range(offset, offset + num):
            answer += fid * o_idx

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
