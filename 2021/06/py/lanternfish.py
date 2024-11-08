import os
import sys


def main():
    # ex_list = [3, 4, 3, 1, 2]
    ex_list = [4, 1, 3, 2, 4, 3, 1, 4, 4, 1, 1, 1, 5, 2, 4, 4, 2, 1, 2, 3, 4,
               1, 2, 4, 3, 4, 5, 1, 1, 3, 1, 2, 1, 4, 1, 1, 3, 4, 1, 2, 5, 1,
               4, 2, 2, 1, 1, 1, 3, 1, 5, 3, 1, 2, 1, 1, 1, 1, 4, 1, 1, 1, 2,
               2, 1, 3, 1, 3, 1, 3, 4, 5, 1, 2, 2, 1, 1, 1, 4, 1, 5, 1, 3, 1,
               3, 4, 1, 3, 2, 3, 4, 4, 4, 3, 4, 5, 1, 3, 1, 3, 5, 1, 1, 1, 1,
               1, 2, 4, 1, 2, 1, 1, 1, 5, 1, 1, 2, 1, 3, 1, 4, 2, 3, 4, 4, 3,
               1, 1, 3, 5, 3, 1, 1, 5, 2, 4, 1, 1, 3, 5, 1, 4, 3, 1, 1, 4, 2,
               1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 4, 5, 1, 2, 5, 3, 1, 1, 3,
               1, 1, 1, 1, 5, 1, 2, 5, 1, 1, 1, 1, 1, 1, 3, 5, 1, 3, 2, 1, 1,
               1, 1, 1, 1, 1, 4, 5, 1, 1, 3, 1, 5, 1, 1, 1, 1, 3, 3, 1, 1, 1,
               4, 4, 1, 1, 4, 1, 2, 1, 4, 4, 1, 1, 3, 4, 3, 5, 4, 1, 1, 4, 1,
               3, 1, 1, 5, 5, 1, 2, 1, 2, 1, 2, 3, 1, 1, 3, 1, 1, 2, 1, 1, 3,
               4, 3, 1, 1, 3, 3, 5, 1, 2, 1, 4, 1, 1, 2, 1, 3, 1, 1, 1, 1, 1,
               1, 1, 4, 5, 5, 1, 1, 1, 4, 1, 1, 1, 2, 1, 2, 1, 3, 1, 3, 1, 1,
               1, 1, 1, 1, 1, 5]

    print(f"Initial state: {ex_list}")
    for iter in range(256):
        for i in range(len(ex_list)):
            if ex_list[i] == 0:
                ex_list[i] += 7
                ex_list.append(8)
            ex_list[i] -= 1
        print(f"After {iter+1:02d} days: {len(ex_list)} items")

    print(f"[-] Total of {len(ex_list)} fish.")


if __name__ == "__main__":
    main()