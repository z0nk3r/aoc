def part1(lines):
    ans1 = 0
    times = lines[0].split(":")[1].split()
    dists = lines[1].split(":")[1].split()
    for i in range(len(times)):
        races = [1 for t in range(int(times[i])) if (t*(int(times[i])-t)) > int(dists[i])]
        ans1 = ans1 + sum(races) if not ans1 else ans1 * sum(races)
    
    print(f"1: {ans1}")

def part2(lines):
    time = int("".join(lines[0].split(":")[1].split()))
    dist = int("".join(lines[1].split(":")[1].split()))
    race = [1 for t in range(time) if (t*(time-t)) > dist]
    
    print(f"2: {sum(race)}")

if __name__ == "__main__":
    with open("input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
    part1(lines)
    part2(lines)