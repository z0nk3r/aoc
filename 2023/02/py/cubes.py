def get_maxes(games):
    red = green = blue = 0
    for game in games:
        for play in game.split(","):
            cnt, col = play.split()
            cnt = int(cnt)
            if col == "blue" and cnt > blue:
                blue = cnt
            elif col == "red" and cnt > red:
                red = cnt
            elif col == "green" and cnt > green:
                green = cnt

    return red, green, blue

def part1():
    with open("../input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
        
    red = 12
    green = 13
    blue = 14
    answer = 0
    for line in lines:
        id = int(line.split(": ")[0].split(" ")[1])
        r, g, b = get_maxes(line.split(": ")[1].split(";"))  # [games]
        if (r <= red and g <= green and b <= blue):
            answer += id
    print(f"1: {answer = }")

def part2():
    with open("../input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]

    answer = 0
    for line in lines:
        r, g, b = get_maxes(line.split(": ")[1].split(";"))  # [games]
        power = r * g * b
        answer += power
    print(f"2: {answer = }")

if __name__ == "__main__":
    part1()
    part2()