import numpy

def part1(lines):
    moves  = lines[0]
    
    maps = {}
    for line in lines[2::]:
        src = line.split(" = ")[0]
        dests = line.split(" = ")[1].replace("(", "").replace(")", "").split(", ")
        maps[src] = dests
    
    curr = "AAA"
    ans1 = 0
    ctr = 0
    while curr != "ZZZ":
        if ctr >= len(moves):
            ctr = 0
        if moves[ctr] == "L":
            curr = maps[curr][0]
        else:
            curr = maps[curr][1]
        ans1 += 1
        ctr += 1
    
    print(f"1: {ans1}")

def part2(lines):
    moves  = lines[0]
    
    maps = {}
    for line in lines[2::]:
        src = line.split(" = ")[0]
        dests = line.split(" = ")[1].replace("(", "").replace(")", "").split(", ")
        maps[src] = dests
        
    ans2 = 0
    currs = ["AAA", "PRA", "PVA", "XLA", "PTA", "FBA"]
    curr_count = [0, 0, 0, 0, 0, 0]
    for idx, curr in enumerate(currs):
        ctr = 0
        while not curr.endswith("Z"):
            if ctr >= len(moves):
                ctr = 0
            if moves[ctr] == "L":
                curr = maps[curr][0]
            else:
                curr = maps[curr][1]
            curr_count[idx] += 1
            ctr += 1

    ans2 = numpy.lcm.reduce(curr_count)
    print(f"2: {ans2}")

if __name__ == "__main__":
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    part1(lines)
    part2(lines)