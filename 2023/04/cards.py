def part1(lines):
    ans1 = 0
    for line in lines:
        score = 0
        wins = line.split(":")[1].split("|")[0].split()
        card = line.split(":")[1].split("|")[1].split()
        for num in card:
            if num in wins:
                if score == 0:
                    score += 1
                else:
                    score *= 2
        ans1 += score

    print(f"{ans1 = }")

def part2(lines):
    ans2 = 0
    card_track = []
    for i in range(len(lines)):
        card_track.append(1)

    for lidx, line in enumerate(lines):
        score = 0
        wins = line.split(":")[1].split("|")[0].split()
        card = line.split(":")[1].split("|")[1].split()
        for num in card:
            if num in wins:
                score += 1

        for i in range(score):
            card_track[lidx+i+1] += card_track[lidx]
        
    ans2 = sum(card_track)

    print(f"{ans2 = }")

if __name__ == "__main__":
    with open("input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
    part1(lines)
    part2(lines)