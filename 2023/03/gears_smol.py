def get_num(ridx, cidx, matrix, sym):
    l_lim = r_lim = 0
    while l_lim >= -2 and matrix[ridx][cidx+l_lim] not in [sym, '.']:
        l_lim -= 1
    while r_lim <= 2 and matrix[ridx][cidx+r_lim] not in [sym, '.']:
        r_lim += 1
    nums = [matrix[ridx][cidx+i] for i in range(l_lim+1, r_lim)]
    return int("".join(nums))

def main():
    with open("input") as input:
        matrix = [line.replace("\n", "") for line in input.readlines()]
        
    ans1 = ans2 = 0
    dirx = [-1, 0, 1]
    diry = [-1, 0, 1]
    symbols = ["*", "+", "-", "/", "&", "#", "%", "$", "=", "@"]

    for ridx, row in enumerate(matrix):
        for cidx, col in enumerate(row):
            curr_neighs = set()
            curr = matrix[ridx][cidx]
            if curr in symbols:
                for xdir in dirx:
                    for ydir in diry:
                        try:
                            neighbor = matrix[ridx+xdir][cidx+ydir]
                            if neighbor.isdigit():
                                num = get_num(ridx+xdir, cidx+ydir, matrix, curr)
                                curr_neighs.add(num)
                        except IndexError:
                            pass
            for i in range(len(curr_neighs)):
                ans1 += list(curr_neighs)[i]
            if len(curr_neighs) == 2 and curr == "*":
                ans2 += (list(curr_neighs)[0] * list(curr_neighs)[1])
    print(f"1: {ans1}\n2: {ans2}")

if __name__ == "__main__":
    main()