#!/usr/bin/env python3

def main():
    score = 0
    results = []
    start_count = 0
    end_count = 0

    '''
        [C]             [L]         [T]
        [V] [R] [M]     [T]         [B]
        [F] [G] [H] [Q] [Q]         [H]
        [W] [L] [P] [V] [M] [V]     [F]
        [P] [C] [W] [S] [Z] [B] [S] [P]
    [G] [R] [M] [B] [F] [J] [S] [Z] [D]
    [J] [L] [P] [F] [C] [H] [F] [J] [C]
    [Z] [Q] [F] [L] [G] [W] [H] [F] [M]
     1   2   3   4   5   6   7   8   9
    '''

    dict_crate = {
        1: ['Z', 'J', 'G'],
        2: ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'],
        3: ['F', 'P', 'M', 'C', 'L', 'G', 'R'],
        4: ['L', 'F', 'B', 'W', 'P', 'H', 'M'],
        5: ['G', 'C', 'F', 'S', 'V', 'Q'],
        6: ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'],
        7: ['H', 'F', 'S', 'B', 'V'],
        8: ['F', 'J', 'Z', 'S'],
        9: ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T'],
    }
    with open("../input.txt") as input:
        moves = [x.replace("\n", "") for x in input.readlines()]

    # count of all crates for sanity checking later
    for i in range(1, 10):
        start_count += len(dict_crate[i])

    for idx, move in enumerate(moves):
        if idx <= 9:
            continue
        else:
            quantity = int(move.split()[1])
            src = int(move.split()[3])
            dst = int(move.split()[5])
            print(f"Move {idx-9:>3}: (Q: {quantity:>2}) {src}>{dst}", end="")

            # part 1 needs a reverse here ([::-1]), part two removes it)
            new_list = dict_crate[src][-quantity:]  # [::-1]
            print(f" ([{']['.join(new_list)}])")
            for _ in range(quantity):
                dict_crate[src].pop()
            dict_crate[dst].extend(new_list)

    print("======== results ========")
    for i in range(1, 10):
        print(f"{i}: [{']['.join(dict_crate[i])}]")
        results.append(dict_crate[i][-1])
        end_count += len(dict_crate[i])

    # sanity check
    print(f"Starting: {start_count} Ending: {end_count}")

    print(f"Flag: {''.join(results)}")


if __name__ == "__main__":
    main()
