def get_maxes(line):
    red = green = blue = 0
    games = line.split(":")[1].split(";")
    for game in games:
        for play in game.split(","):
            cnt, col = play.split()
            if col == "blue":
                if int(cnt) > blue:
                    blue = int(cnt)
            elif col == "red":
                if int(cnt) > red:
                    red = int(cnt)
            elif col == "green":
                if int(cnt) > green:
                    green = int(cnt)
            
            # if play.split()[1] == "blue":
            #     if int(play.split()[0]) > blue:
            #         blue = int(play.split()[0])
            # elif play.split()[1] == "red":
            #     if int(play.split()[0]) > red:
            #         red = int(play.split()[0])
            # elif play.split()[1] == "green":
            #     if int(play.split()[0]) > green:
            #         green = int(play.split()[0])

    return red, green, blue

def part1():
    with open("../input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
        
    red = 12
    green = 13
    blue = 14
    answer = 0
    for line in lines:
        id = int(line.split(":")[0].split(" ")[1])
        
        r, g, b = get_maxes(line)
        if (r <= red and g <= green and b <= blue):
            answer += id

    print(f"1: {answer = }")

def part2():
    with open("../input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
        
    answer = 0
    for line in lines:
        r, g, b = get_maxes(line)
        power = r * g * b
        answer += power
    
    print(f"2: {answer = }")

if __name__ == "__main__":
    part1()
    part2()