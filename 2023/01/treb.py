def treb(part):
    with open("input") as input:
        lines = [x.replace("\n", "") for x in input.readlines()]
    
    answer = 0
    for line in lines:

        if part == 2:
            line = line.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r")
            line = line.replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t")
            line = line.replace("nine", "n9e")

        nums = [int(char) for char in line if char.isdigit()]

        answer += (10 * nums[0])
        answer += nums[-1]

    print(f"{part}: {answer = }")

if __name__ == "__main__":
    treb(1)
    treb(2)