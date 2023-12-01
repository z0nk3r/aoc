#!/usr/bin/env python3

def main():
    with open("../input.txt") as input:
        rounds = [x.replace("\n", "") for x in input.readlines()]

    score = 0
    for idx, round in enumerate(rounds):
        print(f"Round {idx}:")
        opp, you = round.split()

        # translate to common and recognizable char
        if opp == "A":
            opp = "r"
        elif opp == "B":
            opp = "p"
        else:
            opp = "s"

        if you == "X":
            if opp == 'r':
                you = 's'
            elif opp == 'p':
                you = 'r'
            elif opp == 's':
                you = 'p'
            else:
                pass

        elif you == "Y":
            you = opp

        else:
            if opp == 'r':
                you = 'p'
            elif opp == 'p':
                you = 's'
            elif opp == 's':
                you = 'r'
            else:
                pass

        if you == 'r':
            you_score = 1
        elif you == 'p':
            you_score = 2
        elif you == 's':
            you_score = 3
        else:
            you_score = 0

        print(f"Opp: {opp} vs You: {you}")

        # # # # # # # # # # # #
        #       scoring       #
        # # # # # # # # # # # #

        # draw
        if opp == you:
            score += 3
            score += you_score

        # opp win
        if opp == 'r' and you == 's':
            score += you_score

        if opp == 'p' and you == 'r':
            score += you_score

        if opp == 's' and you == 'p':
            score += you_score

        # you win
        if you == 'r' and opp == 's':
            score += 6
            score += you_score

        if you == 'p' and opp == 'r':
            score += 6
            score += you_score

        if you == 's' and opp == 'p':
            score += 6
            score += you_score

        print(score)

    print(f"Final Score: {score}")


if __name__ == "__main__":
    main()
