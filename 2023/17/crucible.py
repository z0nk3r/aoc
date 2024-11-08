from heapq import heappush, heappop
from time import sleep
import sys
GREEN = "\033[0;32m"
END = "\033[0m"
SLEEP_VAR = 0.00003
do_print = True
charmap = {(0, 0): '.', (-1, 0): 'v', (0, -1): '>', (1, 0): '^', (0, 1): '<'}

def travel(matrix, part, min_turn, max_turn):
    visited = set()
    start = (0, (0, 0), (0, 0), 0)
    pqueue = []
    pqueue.append(start)
    
    if do_print:
        # hide cursor
        print("\033[?25l", end="")
    
    while pqueue:
        heat_l, curr_c, curr_d, num = heappop(pqueue)
        if do_print:
            print(f"\033[{curr_c[0]+2};{curr_c[1]+1}H", end="", flush=True)
            print(f"{GREEN}{charmap[curr_d]}{END}", end="", flush=True)
            sleep(SLEEP_VAR)
        
        # print(f"{curr_c = }")
        if curr_c[0] == (len(matrix) - 1) and curr_c[1] == (len(matrix[0]) - 1) and num >= min_turn:
            if do_print:
                # show cursor
                print("\033[?25h", end="")
                # move cursor back to the bottom
                print(f"\033[{len(matrix)+3};{0}H", end="", flush=True)
            print(f"{part}: {heat_l}")
            break
    
        if (curr_c, curr_d, num) in visited:
            continue

        visited.add((curr_c, curr_d, num))

        if num < max_turn and curr_d != (0, 0):
            next_c = (curr_c[0] + curr_d[0], curr_c[1] + curr_d[1])
            if 0 <= next_c[0] < len(matrix) and 0 <= next_c[1] < len(matrix[0]):
                heappush(pqueue, (heat_l + int(matrix[next_c[0]][next_c[1]]), next_c, curr_d, num + 1))
        
        if num >= min_turn or curr_d == (0, 0):
            for diry, dirx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if (diry, dirx) != curr_d and (diry, dirx) != (-curr_d[0], -curr_d[1]):
                    next_c = (curr_c[0] + diry, curr_c[1] + dirx)
                    if 0 <= next_c[0] < len(matrix) and 0 <= next_c[1] < len(matrix[0]):
                        heappush(pqueue, (heat_l + int(matrix[next_c[0]][next_c[1]]), next_c, (diry, dirx), 1))

if __name__ == "__main__":
    matrix = [line.replace("\n", "") for line in open(0).readlines()]

    if "-q" in sys.argv:
        do_print = False
    if do_print:
        # clearscreen
        print("\033[2J\033[;H")

        for row in matrix:
            print(row)

    # part 1
    travel(matrix, 1, 0, 3)

    if do_print:
        sleep(5)
        # clearscreen
        print("\033[2J\033[;H")

        for row in matrix:
            print(row)
    
    # part 2
    travel(matrix, 2, 4, 10)