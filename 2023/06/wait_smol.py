from math import floor, ceil

def quadr(b, c):
    lower = int((-b + (b*b - 4*c) ** 0.5) // -2)
    return b - lower - lower - 1

def main():
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    times = list(map(int, lines[0].split(":")[1].split()))
    time = int("".join(lines[0].split(":")[1].split()))
    dists = list(map(int, lines[1].split(":")[1].split()))
    dist = int("".join(lines[1].split(":")[1].split()))

    ans1 = 1
    for i in range(len(times)):
        ans1 *= quadr(-times[i], dists[i])
    print(f"1: {ans1}")

    ans2 = quadr(-time, dist)
    print(f"2: {ans2}")

if __name__ == "__main__":
    main()