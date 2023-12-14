def check_rows(group):
    for ridx in range(1, len(group)):
        up = group[:ridx][::-1]
        down = group[ridx:]
        
        up = up[:len(down)]
        down = down[:len(up)]
        
        if ridx == 6: 
            print(f"6{up = } vs 6{down = }")
        if up == down:
            print(f"{up = } vs {down = }")
            return ridx
    
    return 0


def part1(groups):
    total = 0
    for gidx, group in enumerate(groups):
        print(f"\n---------------- {gidx} ---------------------")
        print(group)
        lines = group.splitlines()
        r_ans = 0
        c_ans = 0
        r_ans = check_rows(lines)
        lines_rot = list(zip(*lines))
        lines_rot = [''.join(tups) for tups in lines_rot]
        # print(f"{lines = }")
        # print(f"{lines_rot = }")
        
        c_ans = check_rows(lines_rot)
        print(f"reflect on row {r_ans}")
        print(f"reflect on col {c_ans}")
        print(f" {total}", end="", flush=True)
        total += (r_ans * 100) + c_ans
        print(f" > {total}")

    print("1: 29202 too low")
    print("1: 30617 too low")
    print(f"1: {total}")
    print("1: 31854 too high")

def part2(lines):
    for line in lines:
        pass

if __name__ == "__main__":
    lines = open(0).read().split("\n\n")

    part1(lines)
    part2(lines)