#!/usr/bin/env python3

def main():

    score = 0
    lower_priority = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    upper_priority = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    with open("../input.txt") as input:
        rucks = [x.replace("\n", "") for x in input.readlines()]

    print("======= Part one =======")
    for idx, ruck in enumerate(rucks):
        ruck_len = len(ruck)
        ruck_a = ruck[0:int(ruck_len/2)]
        ruck_b = ruck[int(ruck_len/2):ruck_len]
        print(f"Ruck {idx}: {ruck}. ", end="")
        for letter in ruck_a:
            if letter in ruck_b:
                letter_found = letter

        try:
            score_found = lower_priority[letter_found]
            score += score_found
        except:
            score_found = upper_priority[letter_found]+26
            score += score_found

        print(f"Matching Letter: {letter_found}. Priority Score: {score_found}")

    print(f"Final score (1): {score}")

    print("======= Part two =======")

    score = 0
    for idx, ruck in enumerate(rucks):

        if idx % 3 == 1:
            continue
        elif idx % 3 == 2:
            continue
        else:
            ruck_1 = rucks[idx]
            ruck_2 = rucks[idx+1]
            ruck_3 = rucks[idx+2]

            print(f"Elf group {int(idx/3)+1 if idx > 0 else idx+1}:")
            print(f"1: {ruck_1}\n2: {ruck_2}\n3: {ruck_3}")

            for letter in ruck_1:
                if letter in ruck_2 and letter in ruck_3:
                    letter_found = letter

            try:
                score_found = lower_priority[letter_found]
                score += score_found
            except:
                score_found = upper_priority[letter_found]+26
                score += score_found

            print(f"Matching Letter: {letter_found}. Priority Score: {score_found}\n")

    print(f"Final score (2): {score}")


if __name__ == "__main__":
    main()
