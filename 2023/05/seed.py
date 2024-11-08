def mapper(lines):
    map_dict = {}
    for line in lines:
        line = [int(x) for x in line.split()]
        map_dict[line[1]] = line[0]
        map_dict[line[1]+(line[2]-1)] = line[0]+(line[2]-1)
    
    # for key in sorted(map_dict):
        # print(f"{key} > {map_dict[key]}")
    
    return map_dict

def translate(seed, map_dict):
    closest_key = min(map_dict.keys(), key = lambda key: abs(key-seed))
    key_delta = closest_key - seed
    found_val = map_dict[closest_key] - key_delta
    return found_val

def part1(lines):
    locs_found = []
    seeds = lines[0].split(":")[1].split()
    ss_dict = mapper(lines[3:38])        # seed>soil
    sf_dict = mapper(lines[40:73])       # soil>fert
    fw_dict = mapper(lines[75:103])      # fert>water
    wl_dict = mapper(lines[105:120])     # water>light
    lt_dict = mapper(lines[122:154])     # light>temp
    th_dict = mapper(lines[156:188])     # temp>humid
    hl_dict = mapper(lines[190:206])     # humid>loc
    for seed in seeds:
        curr = int(seed)
        for t_dict in [ss_dict, sf_dict, fw_dict, wl_dict, lt_dict, th_dict, hl_dict]:
            curr = translate(curr, t_dict)
    
        print(f"{curr = }")
        locs_found.append(curr)
    
    print(f"1: {min(locs_found)}")


def part2(lines):
    low_loc_found = 5000000000
    allseeds = lines[0].split(":")[1].split()
    seeds = tuple(map(lambda i: (allseeds[i], allseeds[i+1]), range(len(allseeds)-1)[::2]))
    ss_dict = mapper(lines[3:38])        # seed>soil
    sf_dict = mapper(lines[40:73])       # soil>fert
    fw_dict = mapper(lines[75:103])      # fert>water
    wl_dict = mapper(lines[105:120])     # water>light
    lt_dict = mapper(lines[122:154])     # light>temp
    th_dict = mapper(lines[156:188])     # temp>humid
    hl_dict = mapper(lines[190:206])     # humid>loc

    # TODO: redo part 2, take 24h56m and gets wrong answer
    num = 0
    for seed in seeds:
        for i in range(int(seed[1])):
            if i % 1000000 == 0:
                print(f"\r {num:2}: {i:12} of {seed[1]}", end="", flush=True)
            curr = int(seed[0]) + i
            for t_dict in [ss_dict, sf_dict, fw_dict, wl_dict, lt_dict, th_dict, hl_dict]:
                curr = translate(curr, t_dict)
            if curr < low_loc_found:
                low_loc_found = curr

        print(f"\nFinished Seed {num} - Curr Low: {low_loc_found}\n")
        num += 1 

    print(f"2: {low_loc_found}")

if __name__ == "__main__":
    with open("input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
    # part1(lines)
    part2(lines)