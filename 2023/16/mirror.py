def part1(matrix, start):
    # start = ((0, -1), (0, 1))
    start = start
    visited = set()
    
    queue = []
    queue.append(start)
    
    while queue:
        curr_c, curr_d = queue.pop(0)
        curr_c = tuple(map(lambda i, j: i + j, curr_c, curr_d))

        if curr_c[0] < 0 or curr_c[0] >= len(matrix) or curr_c[1] < 0 or curr_c[1] >= len(matrix[0]):
            # out-of-bounds dropoff
            continue

        match str(matrix[curr_c[0]][curr_c[1]]):
            case ".":
                next_t = (curr_c, curr_d)
                if next_t not in visited:
                    queue.append(next_t)
                    visited.add(next_t)

            case "/":
                next_d = (-curr_d[1], -curr_d[0])
                next_t = (curr_c, next_d)
                if next_t not in visited:
                    queue.append(next_t)
                    visited.add(next_t)

            case "\\":
                next_d = (curr_d[1], curr_d[0])
                next_t = (curr_c, next_d)
                if next_t not in visited:
                    queue.append(next_t)
                    visited.add(next_t)

            case "|":
                if curr_d[0] == 0:  # moving horiz
                    next_d1 = (-curr_d[1], curr_d[0])
                    next_d2 = (curr_d[1], curr_d[0])
                    next_t1 = (curr_c, next_d1)
                    next_t2 = (curr_c, next_d2)
                    if next_t1 not in visited:
                        queue.append(next_t1)
                        visited.add(next_t1)
                    if next_t2 not in visited:
                        queue.append(next_t2)
                        visited.add(next_t2)

                else:               # moving vert
                    next_t = (curr_c, curr_d)
                    if next_t not in visited:
                        queue.append(next_t)
                        visited.add(next_t)

            case "-":
                if curr_d[1] != 0:  # moving horiz
                    next_t = (curr_c, curr_d)
                    if next_t not in visited:
                        queue.append(next_t)
                        visited.add(next_t)

                else:               # moving vert
                    next_d1 = (curr_d[1], -curr_d[0])
                    next_d2 = (curr_d[1], curr_d[0])
                    next_t1 = (curr_c, next_d1)
                    next_t2 = (curr_c, next_d2)
                    if next_t1 not in visited:
                        queue.append(next_t1)
                        visited.add(next_t1)
                    if next_t2 not in visited:
                        queue.append(next_t2)
                        visited.add(next_t2)

    visit_s = set()
    for coord, _ in visited:
        visit_s.add(coord)

    return len(visit_s)

def part2(matrix):
    max_found = 0
    start = ((0, -1), (0, 1))
    ans = part1(matrix, start)
    print(f"1: {ans}")

    # > ...
    for ridx in range(len(matrix)):
        start = ((ridx, -1), (0, 1))
        ans = part1(matrix, start)
        if ans > max_found:
            max_found = ans

    # ... <
    for ridx in range(len(matrix)):
        start = ((ridx, len(matrix[0])), (0, -1))
        ans = part1(matrix, start)
        if ans > max_found:
            max_found = ans

    #  v
    # ...
    for cidx in range(len(matrix)):
        start = ((-1, cidx), (1, 0))
        ans = part1(matrix, start)
        if ans > max_found:
            max_found = ans

    # ...
    #  ^
    for cidx in range(len(matrix)):
        start = ((len(matrix), cidx), (-1, 0))
        ans = part1(matrix, start)
        if ans > max_found:
            max_found = ans
    
    print(f"2: {max_found}")

if __name__ == "__main__":
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    # part1(lines)
    part2(lines)