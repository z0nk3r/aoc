def hash(string):
    val = 0
    for char in string:
        c_ord = ord(char)
        val += c_ord
        val *= 17
        val = val % 256

    return val


def part1(line):
    total = 0
    # print(line)
    # print(f"{line[0].split(',') = }")
    for group in line[0].split(','):
        # score = 0
        # for char in group:
        #     c_ord = ord(char)
        #     score += c_ord
        #     score *= 17
        #     score %= 256
        # total += 
        # print(f"{group}: {score}")
        total += hash(group)

    print(f"1: {total}")  # i: 512950 s: 1320


def part2(line):
    total = 0
    hashmap = {}
    for i in range(256):
        hashmap[i] = []
    for gidx, group in enumerate(line[0].split(',')):
        # print(f'{"="*30} {gidx} {"="*30}')
        lens, num = group.replace('-', '=').split('=')
        curr_lens = tuple((lens, num))
        # print(f"{lens = }, {num = }")
        curr_ht = hashmap[hash(lens)]
        if num == '':
            for lidx, lenses in enumerate(curr_ht):
                if lenses[0] == lens:
                    curr_ht.pop(lidx)
                    # print(f"({lens}, {num}): removed from ht_idx {hash(lens)} at {lidx}")
        else:
            if curr_ht == []:
                curr_ht.append(curr_lens)
                # print(f"({lens}, {num}): appended1 to empty [] at ht_idx {hash(lens)}")
                continue
            try:
                for lidx, lenses in enumerate(curr_ht):
                    if lenses[0] == lens:
                        curr_ht[lidx] = curr_lens
                        # print(f"({lens}, {num}): replaced at ht_idx {hash(lens)} at {lidx}")
                        # continue
                        raise IndexError

                    if lidx == len(curr_ht) - 1:
                        curr_ht.append(curr_lens)
                        # print(f"({lens}, {num}): appended2 to at ht_idx {hash(lens)}")
                        # continue
                        raise IndexError
            except IndexError:
                pass

    for i in range(256):
        if hashmap[i] != []:
            print(f"Box {i}: {hashmap[i]}")
            for gidx, group in enumerate(hashmap[i]):
                total += (i + 1) * (gidx + 1) * int(group[1])

    print(f"2: {total}") # i: 247153 s: 145


if __name__ == "__main__":
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    # part1(lines)
    part2(lines)
