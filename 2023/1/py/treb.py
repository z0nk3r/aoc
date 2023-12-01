# def line_parse(line):
#     nums = [int(char) for char in line if char.isdigit()]
#     return nums[0], nums[-1]

# def main():
#     with open("../input") as input:
#         lines = [x.replace("\n", "") for x in input.readlines()]
    
#     answer = 0
#     for line in lines:
#         num1, num2 = line_parse(line)

#         answer += (10 * num1)
#         answer += num2
#         # print(f" {num1 * 10} + {num2} = {(10 * num1) + num2} ({answer})")

#     print(f"1: {answer = }")

#     answer = 0
#     for line in lines:

#         line = line.replace("one", "o1e").replace("two", "t2o")
#         line = line.replace("three", "t3e").replace("four", "f4r")
#         line = line.replace("five", "f5e").replace("six", "s6x")
#         line = line.replace("seven", "s7n").replace("eight", "e8t")
#         line = line.replace("nine", "n9e")

#         num1, num2 = line_parse(line)

#         answer += (10 * num1)
#         answer += num2
#         # print(f" {num1 * 10} + {num2} = {(10 * num1) + num2} ({answer})")

#     print(f"2: {answer = }")

def treb(part):
    with open("../input") as input:
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

treb(1)
treb(2)

#main()