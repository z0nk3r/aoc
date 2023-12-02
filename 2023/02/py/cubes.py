def part1():
    with open("../input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
        
    red = 12
    green = 13
    blue = 14
    answer = 0
    id_ctr = 0
    for line in lines:
        id = line.split(":")[0].split(" ")[1]
        games = line.split(":")[1].split(";")
        for game in games:
            
            for play in game.split(","):
                if play.split()[1] == "blue":
                    blue -= int(play.split()[0])
                elif play.split()[1] == "red":
                    red -= int(play.split()[0])
                elif play.split()[1] == "green":
                    green -= int(play.split()[0])
            print(f"{id}: {game = }")
            print(f"{red = }{green = }{blue = }")
            if (red >= 0 and green >= 0 and blue >= 0):
                id_ctr += 1
            red = 12
            green = 13
            blue = 14

        if (id_ctr == len(games)):
            answer += int(id)
        
        id_ctr = 0

    print(f"1: {answer = }")

def part2():
    with open("../input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
        
    red = green = blue = 0
    answer = 0
    for line in lines:
        id = line.split(":")[0].split(" ")[1]
        print(f"================= {id} ==================")
        games = line.split(":")[1].split(";")
        for game in games:
            for play in game.split(","):
                if play.split()[1] == "blue":
                    if int(play.split()[0]) > blue:
                        blue = int(play.split()[0])
                elif play.split()[1] == "red":
                    if int(play.split()[0]) > red:
                        red = int(play.split()[0])
                elif play.split()[1] == "green":
                    if int(play.split()[0]) > green:
                        green = int(play.split()[0])
            print(f"{id}: {game = }")
            print(f"{red = } {green = } {blue = }")
            
            power = (red * green * blue)
            
        
        answer += power
        print(f"{id}: {power = }")
        red = green = blue = 0
    
    print(f"2: {answer = }")

if __name__ == "__main__":
    part1()
    part2()