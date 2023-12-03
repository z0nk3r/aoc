def get_num(ridx, cidx, matrix):
    num = 0
    curr = matrix[ridx][cidx]
    try:
        curr_l = matrix[ridx][cidx-1]
    except IndexError:
        curr_l = "a"
    try:
        curr_ll = matrix[ridx][cidx-2]
    except IndexError:
        curr_ll = "a"
    try:
        curr_r = matrix[ridx][cidx+1]
    except IndexError:
        curr_r = "a"
    try:
        curr_rr = matrix[ridx][cidx+2]
    except IndexError:
        curr_rr = "a"
    
    if (curr.isdigit() and curr_r.isdigit() and curr_rr.isdigit()):
        num = int(curr+curr_r+curr_rr)

    elif (curr_l.isdigit() and curr.isdigit() and curr_r.isdigit()):
        num = int(curr_l+curr+curr_r)

    elif (curr_ll.isdigit() and curr_l.isdigit() and curr.isdigit()):
        num = int(curr_ll+curr_l+curr)

    elif (not curr_l.isdigit() and curr.isdigit() and curr_r.isdigit()):
        num = int(curr+curr_r)

    elif (curr_l.isdigit() and curr.isdigit() and not curr_r.isdigit()):
        num = int(curr_l+curr)

    elif (not curr_l.isdigit() and curr.isdigit() and not curr_r.isdigit()):
        num = int(curr)

    else:
        print("we got here somehow!")
        print(f"? {matrix[ridx-1][cidx-1]} {matrix[ridx-1][cidx]} {matrix[ridx-1][cidx+1]} ?")
        print(f"{curr_ll} {curr_l} {curr} {curr_r} {curr_rr}")
        print(f"? {matrix[ridx+1][cidx-1]} {matrix[ridx+1][cidx]} {matrix[ridx+1][cidx+1]} ?")

    return num


def part1(lines):
    ans1 = 0
    last = 0
    lastx = 0
    lasty = 0
    matrix = []
    symbols = ["*", "+", "-", "/", "&", "#", "%", "$", "=", "@"]
    dirx = [-1, 0, 1]
    diry = [-1, 0, 1]
    for row, line in enumerate(lines):
        matrix.append([])
        for col, char in enumerate(line):
            matrix[row].append(char)
    
    for ridx, row in enumerate(matrix):
        for cidx, col in enumerate(row):
            curr = matrix[ridx][cidx]

            if (curr.isdigit()):
                for xdir in dirx:
                    for ydir in diry:
                        try:
                            neighbor = matrix[ridx+xdir][cidx+ydir]
                            if (neighbor in symbols):
                                num = get_num(ridx, cidx, matrix)
                                if ((last == num) and lasty == ridx):
                                    pass
                                else:
                                    ans1 += num
                                    last = num
                                    lastx = cidx
                                    lasty = ridx
                        except IndexError:
                            pass

    print(f"{ans1 = }")

def part2(lines):
    ans2 = 0
    matrix = []
    dirx = [-1, 0, 1]
    diry = [-1, 0, 1]
    for row, line in enumerate(lines):
        matrix.append([])
        for col, char in enumerate(line):
            matrix[row].append(char)
    
    for ridx, row in enumerate(matrix):
        for cidx, col in enumerate(row):
            curr_neighs = set()
            curr = matrix[ridx][cidx]
            
            if (curr == "*"):
                for xdir in dirx:
                    for ydir in diry:
                        try:
                            neighbor = matrix[ridx+xdir][cidx+ydir]
                            if (neighbor.isdigit()):
                                num = get_num(ridx+xdir, cidx+ydir, matrix)
                                curr_neighs.add(num)
                        except IndexError:
                            pass
                
                if len(curr_neighs) == 2:
                    print(f"{curr_neighs = }")
                    ans2 += (list(curr_neighs)[0] * list(curr_neighs)[1])

    
    print(f"{ans2 = }")


if __name__ == "__main__":
    with open("input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
    part1(lines)
    part2(lines)