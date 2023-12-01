#!/usr/bin/env python3
def main():
    with open("../input.txt") as input:
        all_heights = [x.replace("\n", "") for x in input.readlines()]

    scen_scores = {}
    found_coords = []
    debug_r = 86  # x_coord of largest scen_score
    debug_c = 49  # y_coord of largest scen_score

    print("original matrix:")
    print("    0000000000111111111122222222223333333333444444444455555555556666666666777777777788888888889999999999")
    print("    0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789")
    print("    vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    print()
    for idx, num in enumerate(all_heights):
        print(f"{idx:02d}> {num}")
    print()

    # forward - horizontal (--->)
    for row, heights in enumerate(all_heights):
        curr_height = -1

        try:
            if scen_scores[row]:
                pass
        except KeyError:
            scen_scores[row] = []

        for col, height in enumerate(heights):
            if int(height) > curr_height:
                curr_height = int(height)
                coord = f"{row:02d}x{col:02d}"
                found_coords.append(coord)

            try:
                if scen_scores[row][col]:
                    pass
            except IndexError:
                scen_scores[row].append(1)

            offset = 1
            try:
                while height > heights[col+offset]:
                    if (col+offset) >= len(heights)-1:
                        break
                    else:
                        offset += 1
            except IndexError:
                pass
            if row == debug_r and col == debug_c:
                print(f"fh: {row}x{col} *= {offset}")
            scen_scores[row][col] *= offset

    # backwards - horizontal (<---)
    for row, heights in enumerate(all_heights):
        curr_height = -1
        heights = heights[::-1]
        for col, height in enumerate(heights):
            mod_col = (len(heights)-1)-col
            if int(height) > curr_height:
                curr_height = int(height)
                coord = f"{row:02d}x{mod_col:02d}"
                found_coords.append(coord)

            offset = 1
            try:
                while height > heights[col+offset]:
                    if (col+offset) >= len(heights)-1:
                        break
                    else:
                        offset += 1
            except IndexError:
                pass
            if row == debug_r and mod_col == debug_c:
                print(f"bh: {row}x{mod_col} *= {offset}")
            scen_scores[row][mod_col] *= offset

    # convert each col to a list of rows
    new_heights = {}
    for row in all_heights:
        for idx in range(len(row)):
            try:
                if len(new_heights[idx]) == 0:
                    pass
            except KeyError:
                new_heights[idx] = []
            new_heights[idx].append(row[idx])

    # print("rotated matrix:")
    # for num in reversed(new_heights):
    #     print(f"{num:2d}: {''.join(new_heights[num])}")

    # forward - vertical (vvvv)
    for row, heights in new_heights.items():
        curr_height = -1
        for col, height in enumerate(heights):
            if int(height) > curr_height:
                curr_height = int(height)
                coord = f"{col:02d}x{row:02d}"
                found_coords.append(coord)

            offset = 1
            try:
                while height > heights[col+offset]:
                    if (col+offset) >= len(heights)-1:
                        break
                    else:
                        offset += 1
            except IndexError:
                pass
            if col == debug_r and row == debug_c:
                print(f"fv: {col}x{row} *= {offset}")
            scen_scores[col][row] *= offset

    # backwards - vertical (^^^^)
    for row, heights in new_heights.items():
        curr_height = -1
        heights = heights[::-1]
        for col, height in enumerate(heights):
            mod_col = (len(''.join(heights))-1)-col
            if int(height) > curr_height:
                curr_height = int(height)
                coord = f"{mod_col:02d}x{row:02d}"
                found_coords.append(coord)

            offset = 1
            try:
                while height > heights[col+offset]:
                    if (col+offset) >= len(heights)-1:
                        break
                    else:
                        offset += 1
            except IndexError:
                pass
            if mod_col == debug_r and row == debug_c:
                print(f"bv: {mod_col}x{row} *= {offset}")
            scen_scores[mod_col][row] *= offset

    the_trees = sorted(set(found_coords))  # , key=lambda x: x.split("x")[1])

    # for idx, tree in enumerate(the_trees):
    #     try:
    #         if tree[0:2] != the_trees[idx+1][0:2]:
    #             print(f"{tree},")
    #         else:
    #             print(f"{tree}", end=" ")
    #     except IndexError:
    #         print(f"{tree}")

    # print(f"{the_trees = }")

    print("scene scores: ")
    scen_score_per_row = []
    for idx in range(len(scen_scores)):
        print(f"{idx:2d}: {scen_scores[idx]}")
        scen_score_per_row.append(max(scen_scores[idx]))
    print(f"Max per row: {scen_score_per_row}")

    print(f"\nFLAG 1: {len(the_trees)}")
    
    print(f"FLAG 2: {max(scen_score_per_row)}")
    # 381600, 305280 is too high

if __name__ == "__main__":
    main()