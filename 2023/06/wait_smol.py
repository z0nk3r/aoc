from math import sqrt, floor, ceil
def quadr(a, b, c):
    quad1 = (-b + -sqrt(b*b - (4*a*c)))/(2*a)
    quad2 = (-b - -sqrt(b*b - (4*a*c)))/(2*a)
    if quad1 > quad2:
        return floor(quad1) - ceil(quad2) + 1
    else:
        return floor(quad2) - ceil(quad1) + 1

def main():
    lines = [line.replace("\n", "") for line in open("input").readlines()]

    times = list(map(int, lines[0].split(":")[1].split()))
    time = int("".join(lines[0].split(":")[1].split()))
    dists = list(map(int, lines[1].split(":")[1].split()))
    dist = int("".join(lines[1].split(":")[1].split()))

    ans1 = 1
    for i in range(len(times)):
        # ans1 *= sum([1 for t in range(times[i]) if (t*(times[i]-t)) > dists[i]])
        ans1 *= quadr(1, -times[i], dists[i])
    print(f"1: {ans1}")

    ans2 = quadr(1, -time, dist)
    print(f"2: {ans2}")

if __name__ == "__main__":
    main()