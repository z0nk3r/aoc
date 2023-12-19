def part1(matrix, start):
    # start = ((0, -1), (0, 1))
    start = start
    visited = set()
    
    # visited.add(start)
    queue = []
    queue.append(start)
    
    while queue:
        curr_c, curr_d = queue.pop(0)

        curr_c = tuple(map(lambda i, j: i + j, curr_c, curr_d))

        # next_c = tuple(map(lambda i, j: i + j, curr_c, curr_d))
        # # if (curr_c, curr_d) not in visited:
        # #     visited.add((curr_c, curr_d))

        if curr_c[0] < 0 or curr_c[0] >= len(matrix) or curr_c[1] < 0 or curr_c[1] >= len(matrix[0]):
            # out-of-bounds dropoff
            continue

        match str(matrix[curr_c[0]][curr_c[1]]):
            case ".":
                # print(f"in case . with: {curr_c} {curr_d}	> ", end="")
                next_t = (curr_c, curr_d)
                # print(f"{next_t}")
                if next_t not in visited:
                    queue.append(next_t)
                    visited.add(next_t)

            case "/":
                # print(f"in case / with: {curr_c} {curr_d}	> ", end="")

                # if curr_d[0] != 0:  # moving horiz
                next_d = (-curr_d[1], -curr_d[0])
                # else:               # moving verti
                    # next_d = (curr_d[1], -curr_d[0])
                next_t = (curr_c, next_d)
                # print(f"{next_t}")
                if next_t not in visited:
                    queue.append(next_t)
                    visited.add(next_t)

            case "\\":
                # print(f"in case \ with: {curr_c} {curr_d}	> ", end="")

                # if curr_d[0] == 0:  # moving horiz
                next_d = (curr_d[1], curr_d[0])
                # else:               # moving verti
                    # next_d = ()
                next_t = (curr_c, next_d)
                # print(f"{next_t}")
                if next_t not in visited:
                    queue.append(next_t)
                    visited.add(next_t)

            case "|":
                # print(f"in case | with: {curr_c} {curr_d}	> ", end="")
                if curr_d[0] == 0:  # moving horiz
                    next_d1 = (-curr_d[1], curr_d[0])
                    next_d2 = (curr_d[1], curr_d[0])
                    next_t1 = (curr_c, next_d1)
                    next_t2 = (curr_c, next_d2)
                    # print(f"{next_t1} & {next_t2}")
                    if next_t1 not in visited:
                        queue.append(next_t1)
                        visited.add(next_t1)

                    if next_t2 not in visited:
                        queue.append(next_t2)
                        visited.add(next_t2)

                else:               # moving vert
                    next_t = (curr_c, curr_d)
                    # print(f"{next_t}")
                    if next_t not in visited:
                        queue.append(next_t)
                        visited.add(next_t)

            case "-":
                # print(f"in case - with: {curr_c} {curr_d}	> ", end="")

                if curr_d[1] != 0:  # moving horiz
                    next_t = (curr_c, curr_d)
                    # print(f"{next_t}")
                    if next_t not in visited:
                        queue.append(next_t)
                        visited.add(next_t)

                else:               # moving vert
                    next_d1 = (curr_d[1], -curr_d[0])
                    next_d2 = (curr_d[1], curr_d[0])
                    next_t1 = (curr_c, next_d1)
                    next_t2 = (curr_c, next_d2)
                    # print(f"{next_t1} & {next_t2}")
                    if next_t1 not in visited:
                        queue.append(next_t1)
                        visited.add(next_t1)

                    if next_t2 not in visited:
                        queue.append(next_t2)
                        visited.add(next_t2)

            # case _:
            #     pass
    # print()
    # for row in matrix:
    #     print(row)

    # visit_m = []
    visit_s = set()
    # for _ in range(len(matrix)):
    #     visit_m.append('.'*len(matrix[0]))
    for coord, _ in visited:
        # visit_m[coord[0]] = visit_m[coord[0]][:coord[1]] + "#" + visit_m[coord[0]][coord[1]+1:]
        visit_s.add(coord)
    # print("="*(len(matrix[0])+4))
    # for row in visit_m:
    #     print(row)
    # print(sorted(list(visit_s)))
    # print(f"1: {len(visit_s) = }")
    
    return len(visit_s)

def part2(matrix):
    max_found = 0
    max_start = ((0, 0), (0, 0))
    start = ((0, -1), (0, 1))
    ans = part1(matrix, start)
    print(f"1: {ans}")
    
    print(f"Going to the right >")
    # > ...
    for ridx in range(len(matrix)):
        start = ((ridx, -1), (0, 1))
        ans = part1(matrix, start)
        if ans > max_found:
            max_found = ans
            max_start = start
    
    print(f"Going to the left <")
    # ... <
    for ridx in range(len(matrix)):
        start = ((ridx, len(matrix[0])), (0, -1))
        ans = part1(matrix, start)
        if ans > max_found:
            max_found = ans
            max_start = start
    
    print(f"Going down v")
    #  v
    # ...
    for cidx in range(len(matrix)):
        start = ((-1, cidx), (1, 0))
        ans = part1(matrix, start)
        if ans > max_found:
            max_found = ans
            max_start = start

    print(f"Going up ^")
    # ...
    #  ^
    for cidx in range(len(matrix)):
        start = ((len(matrix), cidx), (-1, 0))
        ans = part1(matrix, start)
        if ans > max_found:
            max_found = ans
            max_start = start
    
    print(f"2: {max_found} {max_start}")

if __name__ == "__main__":
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    # part1(lines)
    part2(lines)