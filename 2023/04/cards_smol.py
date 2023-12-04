def cards():
    with open("input") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
    ans1 = 0
    card_track = [1 for i in range(len(lines))]

    for lidx, line in enumerate(lines):
        score1 = score2 = 0
        wins = line.split(":")[1].split("|")[0].split()
        card = line.split(":")[1].split("|")[1].split()
        for num in card:
            if num in wins:
                score1 = score1 + 1 if score1 == 0 else score1 * 2
                score2 += 1

        ans1 += score1
        for i in range(score2):
            card_track[lidx+i+1] += card_track[lidx]

    print(f"1: {ans1}\n2: {sum(card_track)}")

if __name__ == "__main__":
    cards()