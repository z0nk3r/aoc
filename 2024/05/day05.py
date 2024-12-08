import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_setup, puzzle_run


def sort_the_pages(pageorder, pages):
    new_pages = pages.copy()
    for pg_idx in range(len(new_pages) - 1, -1, -1):
        for ppg_idx in range(pg_idx, -1, -1):
            if new_pages[pg_idx] in pageorder[new_pages[ppg_idx]]:
                swap = new_pages.pop(ppg_idx)
                new_pages.insert(pg_idx, swap)

    return int(new_pages[len(new_pages)//2])


def part1(lines):
    answer = 0
    pageorder = {}

    for i in range(10,100):
        pageorder[f"{i}"] = []
    
    for line in lines:
        if '|' in line:
            pages = line.split('|')
            pageorder[pages[0]].append(pages[1])
        elif line == '':
            pass
        else:
            bad = False
            pages = line.split(",")
            for p_idx, page in enumerate(pages):
                try:
                    if pages[p_idx + 1] not in pageorder[page]:
                        bad = True
                except:
                    pass
            if not bad:
                answer += int(pages[len(pages)//2])

    return answer


def part2(lines):
    answer = 0
    pageorder = {}

    for i in range(10,100):
        pageorder[f"{i}"] = []
    
    for line in lines:
        if '|' in line:
            pages = line.split('|')
            pageorder[pages[0]].append(pages[1])
        elif line == '':
            pass
        else:
            bad = False
            pages = line.split(",")
            for p_idx, page in enumerate(pages):
                try:
                    if pages[p_idx + 1] not in pageorder[page]:
                        bad = True
                except:
                    pass
            if bad:
                answer += sort_the_pages(pageorder, pages)

    return answer


if __name__ == "__main__":
    year, day = puzzle_setup()

    lines = [line.replace("\n", "") for line in open(0).readlines()]

    puzzle_run(part1, part2, lines, year, day)
