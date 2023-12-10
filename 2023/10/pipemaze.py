import time
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[1;94m"
DARK_GRAY = "\033[1;30m"
END = "\033[0m"
SLEEP_VAR = 0.001

def part1(matrix):
    charmap = {'-': '═', '|': '║', 'F': '╔', '7': '╗', 'L': '╚', 'J': '╝', '.': ' ', 'S': 'S'}
    tot_row = 0
    # clearscreen
    print("\033[2J\033[;H")
    # hide cursor
    print("\033[?25l", end="")
    st_row = st_col = 0
    for ridx, row in enumerate(matrix):
        tot_row += 1
        for cidx, col in enumerate(row):
            # print(f"{DARK_GRAY}{charmap[matrix[ridx][cidx]]}{END}", end='', flush=True)
            print(f"{DARK_GRAY}{matrix[ridx][cidx]}{END}", end='', flush=True)
            if col == "S":
                st_row = ridx
                st_col = cidx
        print("")

    # move cursor to start pos
    print(f"\033[{st_row+2};{st_col+1}H", end="", flush=True)
    print(f"{RED}S{END}", end="", flush=True)
    
    path = [(st_row, st_col)]
    neighs = [(st_row, st_col)]

    while len(neighs) > 0:
        curr_r, curr_c = neighs.pop(0)
        curr = matrix[curr_r][curr_c]
        
        if curr in "S|JL" and matrix[curr_r - 1][curr_c] in "|7F" and (curr_r - 1, curr_c) not in path:
            path.append((curr_r - 1, curr_c))
            neighs.append((curr_r - 1, curr_c))

        if curr in "S|7F" and matrix[curr_r + 1][curr_c] in "|JL" and (curr_r + 1, curr_c) not in path:
            path.append((curr_r + 1, curr_c))
            neighs.append((curr_r + 1, curr_c))

        if curr in "S-J7" and matrix[curr_r][curr_c - 1] in "-LF" and (curr_r, curr_c - 1) not in path:
            path.append((curr_r, curr_c - 1))
            neighs.append((curr_r, curr_c - 1))

        if curr in "S-LF" and matrix[curr_r][curr_c + 1] in "-J7" and (curr_r, curr_c + 1) not in path:
            path.append((curr_r, curr_c + 1))
            neighs.append((curr_r, curr_c + 1))

    for idx, _ in enumerate(path):
        (curr_r, curr_c) = path[idx]
        curr = matrix[curr_r][curr_c]
        if curr != "S":
            print(f"\033[{curr_r+2};{curr_c+1}H", end="", flush=True)
            # print(f"{RED}{charmap[curr]}{END}", end="", flush=True)
            print(f"{RED}{curr}{END}", end="", flush=True)

            time.sleep(SLEEP_VAR)
            if idx > 1:
                (curr_r, curr_c) = path[idx-1]
                curr = matrix[curr_r][curr_c]
                print(f"\033[{curr_r+2};{curr_c+1}H", end="", flush=True)
                # print(f"{GREEN}{charmap[curr]}{END}", end="", flush=True)
                print(f"{GREEN}{curr}{END}", end="", flush=True)

    # fix second to last for viz
    end_r, end_c = path[-2]
    print(f"\033[{end_r+2};{end_c+1}H", end="", flush=True)
    # print(f"{GREEN}{charmap[matrix[end_r][end_c]]}{END}", end="", flush=True)
    print(f"{GREEN}{matrix[end_r][end_c]}{END}", end="", flush=True)

    # furthest point from the start
    end_r, end_c = path[-1]
    print(f"\033[{end_r+2};{end_c+1}H", end="", flush=True)
    # print(f"{RED}{charmap[matrix[end_r][end_c]]}{END}", end="", flush=True)
    print(f"{RED}{matrix[end_r][end_c]}{END}", end="", flush=True)

    # showcursor
    print("\033[?25h", end="")
    # move cursor back to the bottom
    print(f"\033[{tot_row+3};{0}H", end="", flush=True)
    print(f"1. {len(path)//2}")
    # time.sleep(5)

def part2(matrix):
    tot_row = 0
    st_row = st_col = 0
    # move cursor back to top to overlay part2 onto part 1
    print(f"\033[{1};{0}H", end="", flush=True)
    # hide cursor
    print("\033[?25l", end="")

    for ridx, row in enumerate(matrix):
        tot_row += 1
        for cidx, col in enumerate(row):
            # uncomment if not doing part1
            # print(f"{DARK_GRAY}{matrix[ridx][cidx]}{END}", end='', flush=True)
            if col == "S":
                st_row = ridx
                st_col = cidx
        print("")

    path = {(st_row, st_col)}
    neighs = [(st_row, st_col)]

    s_list = {"|", "-", "J", "L", "7", "F"}

    while len(neighs) > 0:
        curr_r, curr_c = neighs.pop(0)
        curr = matrix[curr_r][curr_c]
        
        if curr in "S|JL" and matrix[curr_r - 1][curr_c] in "|7F" and (curr_r - 1, curr_c) not in path:
            path.add((curr_r - 1, curr_c))
            neighs.append((curr_r - 1, curr_c))
            if curr == "S":
                s_list &= {"|", "J", "L"}

        if curr in "S|7F" and matrix[curr_r + 1][curr_c] in "|JL" and (curr_r + 1, curr_c) not in path:
            path.add((curr_r + 1, curr_c))
            neighs.append((curr_r + 1, curr_c))
            if curr == "S":
                s_list &= {"|", "7", "F"}

        if curr in "S-J7" and matrix[curr_r][curr_c - 1] in "-LF" and (curr_r, curr_c - 1) not in path:
            path.add((curr_r, curr_c - 1))
            neighs.append((curr_r, curr_c - 1))
            if curr == "S":
                s_list &= {"-", "J", "7"}

        if curr in "S-LF" and matrix[curr_r][curr_c + 1] in "-J7" and (curr_r, curr_c + 1) not in path:
            path.add((curr_r, curr_c + 1))
            neighs.append((curr_r, curr_c + 1))
            if curr == "S":
                s_list &= {"-", "L", "F"}
    
    # replace start S with actual pipechar
    matrix = [row.replace("S", list(s_list)[0]) for row in matrix]
    
    # remove any non-path pipechars to prevent directionality issues for in/out determination
    matrix = ["".join(char if (ridx, cidx) in path else "." for cidx, char in enumerate(row)) for ridx, row in enumerate(matrix)]

    outside = set()
    
    for ridx, row in enumerate(matrix):
        inside = False
        up = None
        for cidx, ch in enumerate(row):
            if ch == "|":
                inside = not inside
            elif ch == "-":
                pass
            elif ch in "LF":
                up = ch == "L"
            elif ch in "7J":
                if ch != ("J" if up else "7"):
                    inside = not inside
                up = None
            if not inside:
                outside.add((ridx, cidx))
    
    for ridx, row in enumerate(matrix):
        for cidx, ch in enumerate(row):
            if (ridx, cidx) not in path and (ridx, cidx) not in outside:
                print(f"\033[{ridx+2};{cidx+1}H", end="", flush=True)
                print(f"{BLUE}I{END}", end="", flush=True)
                # time.sleep(SLEEP_VAR)
            # uncomment if not showing part1
            # elif (ridx, cidx) in path:
            #     print(f"\033[{ridx+2};{cidx+1}H", end="", flush=True)
            #     print(f"{GREEN}{matrix[ridx][cidx]}{END}", end="", flush=True)
            #     time.sleep(SLEEP_VAR)
    
    # showcursor
    print("\033[?25h", end="")
    # move cursor back to the bottom
    print(f"\033[{tot_row+4};{0}H", end="", flush=True)

    ans2 = (len(matrix) * len(matrix[0])) - len(path | outside)
    print(f"2: {ans2}")

if __name__ == "__main__":
    matrix = [line.replace("\n", "") for line in open(0).readlines()]

    part1(matrix)
    part2(matrix)