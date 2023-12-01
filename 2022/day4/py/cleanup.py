#!/usr/bin/env python3

def main():

    score = 0

    with open("../input.txt") as input:
        pairs = [x.replace("\n", "") for x in input.readlines()]

    for idx, pair in enumerate(pairs):
        print(f"{idx}: {pair:<13}", end="")

        elf1 = pair.split(',')[0]
        elf2 = pair.split(',')[1]

        elf1_lower = int(elf1.split('-')[0])
        elf1_upper = int(elf1.split('-')[1])
        elf2_lower = int(elf2.split('-')[0])
        elf2_upper = int(elf2.split('-')[1])

        if (elf1_lower >= elf2_lower) and (elf1_upper <= elf2_upper):
            print("Elf 1 within Elf 2")
            score += 1
        elif (elf2_lower >= elf1_lower) and (elf2_upper <= elf1_upper):
            print("Elf 2 within Elf 1")
            score += 1
        else:
            print("\n")

    print(f"Final score (1): {score}")

    print("======= Part two =======")

    score = 0

    for idx, pair in enumerate(pairs):
        print(f"{idx}: {pair:<13}", end="")

        elf1 = pair.split(',')[0]
        elf2 = pair.split(',')[1]

        elf1_lower = int(elf1.split('-')[0])
        elf1_upper = int(elf1.split('-')[1])
        elf2_lower = int(elf2.split('-')[0])
        elf2_upper = int(elf2.split('-')[1])

        elf1_list = [x for x in range(elf1_lower, elf1_upper+1)]
        elf2_list = [x for x in range(elf2_lower, elf2_upper+1)]

        # print(f"{elf1_list} {elf2_list}")

        if any(x in elf2_list for x in elf1_list):
            print("Overlap Found!")
            score += 1

        elif any(x in elf1_list for x in elf2_list):
            print("Overlap Found!")
            score += 1

        else:
            print("")

    print(f"Final score (2): {score}")


if __name__ == "__main__":
    main()
