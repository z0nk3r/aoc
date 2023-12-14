def part1(grid):
    total = 0
    r_complete = 0
    
    for row in grid:
        print(row)
    
    print()
    for dir in [(-1, 0)]:
        while r_complete != len(grid):
            for ridx, row in enumerate(grid):
                r_sz = len(row)
                if ridx == 0:
                    continue
                for cidx, col in enumerate(row):
                    try:
                        if grid[ridx][cidx] == "O":
                            if grid[ridx+dir[0]][cidx+dir[1]] == ".":
                                # grid[ridx-1][cidx] = "O"
                                new_list = list(grid[ridx-1])
                                new_list[cidx] = "O"
                                grid[ridx-1] = "".join(new_list)
                                # grid[ridx][cidx] = "."
                                new_list = list(grid[ridx])
                                new_list[cidx] = "."
                                grid[ridx] = "".join(new_list)
                                # print(f"{ridx}x{cidx} moved to {ridx-1}x{cidx}")
                                r_sz -= 1
                    
                    except IndexError:
                        pass
                
            if r_sz == len(row):
                r_complete += 1
            # print(f"{r_complete} vs {len(grid)}")
        
        for ridx, row in enumerate(grid):
            print(row)
            for cidx, char in enumerate(row):
                if grid[ridx][cidx] == "O":
                    total += len(grid) - ridx
        
    print(f"1: {total}") # 107053

def part2(grid):
    total = 0
    grid_sets = set()
    grid_iters = []
    start = 0
    end = 0
    end_grid = tuple()
    for row in grid:
        print(row)
    
    print()
    for iter in range(1500):
        if iter % 10 == 0:
            print(f"\r ============== {iter:4} ==============", end="", flush=True)
        for dir in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            r_complete = 0
            while r_complete != len(grid):
                for ridx, row in enumerate(grid):
                    r_sz = len(row)
                    if (dir[0] == -1 and ridx == 0) or (dir[0] == 1 and ridx == len(grid)):
                        continue
                    for cidx, col in enumerate(row):
                        if cidx + dir[1] < 0:
                            continue
                        try:
                            if grid[ridx][cidx] == "O":
                                if grid[ridx+dir[0]][cidx+dir[1]] == ".":
                                    if dir[1] == 0:
                                        new_list = list(grid[ridx+dir[0]])
                                        new_list[cidx] = "O"
                                        grid[ridx+dir[0]] = "".join(new_list)
                                        new_list = list(grid[ridx])
                                        new_list[cidx] = "."
                                        grid[ridx] = "".join(new_list)
                                        r_sz -= 1
                                    else:
                                        new_list = list(grid[ridx])
                                        new_list[cidx+dir[1]] = "O"
                                        new_list[cidx] = '.'
                                        grid[ridx] = "".join(new_list)
                                        
                        
                        except IndexError:
                            pass
                    
                if r_sz == len(row):
                    r_complete += 1
                # print(f"{r_complete} vs {len(grid)}")
            # print(f"\n{dir = }")
        if tuple(grid) not in grid_sets:
            grid_sets.add(tuple(grid))
            grid_iters.append(tuple(grid))
        else:
            print(f"Cycle found at iter {iter}")
            end = iter
            end_grid = tuple(grid)
            for row in grid:
                print(row)
            break
        # if iter % 1000000 == 0:
        #     print(f"\rIter: {iter+1:10}", end="", flush=True)
    for gidx, grids in enumerate(grid_iters):
        if end_grid == grids:
            start = gidx

    print(f"{start = } {end = }")
    b_index = (1000000000-start) % (end - start) + start
    print(f"1000000000 is at idx ({b_index})")
    print()
    grid = grid_iters[b_index-1]
    for ridx, row in enumerate(grid):
        print(row)
        for cidx, char in enumerate(row):
            if grid[ridx][cidx] == "O":
                total += len(grid) - ridx
        
    print(f"2: {total}")

if __name__ == "__main__":
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    # part1(lines)
    part2(lines)