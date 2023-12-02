def get_maxes(games):
    maxes = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        for play in game.split(","):
            cnt, col = play.split()
            if int(cnt) > maxes[col]:
                maxes[col] = int(cnt)

    return maxes["red"], maxes["green"], maxes["blue"]

def part1(lines):
    answer = 0
    for line in lines:
        g_id = int(line.split(": ")[0].split(" ")[1])
        r, g, b = get_maxes(line.split(": ")[1].split(";"))  # [games]
        if (r <= 12 and g <= 13 and b <= 14):
            answer += g_id
    print(f"1: {answer = }")

def part2(lines):
    answer = 0
    for line in lines:
        r, g, b = get_maxes(line.split(": ")[1].split(";"))  # [games]
        power = r * g * b
        answer += power
    print(f"2: {answer = }")

if __name__ == "__main__":
    with open("../input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
    part1(lines)
    part2(lines)