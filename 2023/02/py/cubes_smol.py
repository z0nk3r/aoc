def get_maxes(games):
    maxes = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        for play in game.split(","):
            cnt, col = play.split()
            if int(cnt) > maxes[col]:
                maxes[col] = int(cnt)

    return maxes["red"], maxes["green"], maxes["blue"]

def main():
    with open("../input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]

    ans_1 = ans_2 = 0
    for line in lines:
        r, g, b = get_maxes(line.split(": ")[1].split(";"))  # [games]
        if (r <= 12 and g <= 13 and b <= 14):
            ans_1 += int(line.split(": ")[0].split(" ")[1])  # game_id
        ans_2 += r * g * b

    print(f"{ans_1 = }\n{ans_2 = }")

if __name__ == "__main__":
    main()