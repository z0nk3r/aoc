import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import eval_answer, get_yearday


def part1(lines, year, day):
    answer = 0
    
    pass_fields = {"byr": 0, "iyr": 0, "eyr": 0, "hgt": 0, "hcl": 0, "ecl": 0, "pid": 0, "cid": 0}
    # print(f"{lines = }")
    for line in lines:
        if line == '':
            # reset
            if pass_fields["byr"] > 0 and pass_fields["iyr"] > 0 and pass_fields["eyr"] > 0 and pass_fields["hgt"] > 0 and pass_fields["hcl"] > 0 and pass_fields["ecl"] > 0 and pass_fields["pid"] > 0:
                answer += 1
            for k in pass_fields.keys():
                pass_fields[k] = 0
        
        else:
            items = line.split(' ')
            for item in items:
                field, value = item.split(":")
                pass_fields[field] += 1

    eval_answer(year, day, 1, answer)


def part2(lines, year, day):
    answer = 0
    hexvalues = '1234567890abcdef'
    eye_cols = ["amb", 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    
    for line in lines:
        pass
    pass_fields = {"byr": 0, "iyr": 0, "eyr": 0, "hgt": 0, "hcl": 0, "ecl": 0, "pid": 0, "cid": 0}
    # print(f"{lines = }")
    for line in lines:
        if line == '':
            # reset
            if pass_fields["byr"] > 0 and pass_fields["iyr"] > 0 and pass_fields["eyr"] > 0 and pass_fields["hgt"] > 0 and pass_fields["hcl"] > 0 and pass_fields["ecl"] > 0 and pass_fields["pid"] > 0:
                answer += 1
            for k in pass_fields.keys():
                pass_fields[k] = 0
        
        else:
            items = line.split(' ')
            for item in items:
                field, value = item.split(":")
                if field == "byr":
                    if 1920 <= int(value) <= 2002:
                        pass_fields[field] += 1

                elif field == "iyr":
                    if 2010 <= int(value) <= 2020:
                        pass_fields[field] += 1
                elif field ==  "eyr":
                    if 2020 <= int(value) <= 2030:
                        pass_fields[field] += 1
                elif field == "hgt":
                    if "in" in value:
                        num, _ = value.split("i")
                        if 59 <= int(num) <= 76:
                            pass_fields[field] += 1
                    elif "cm" in value:
                        num, _ = value.split("c")
                        if 150 <= int(num) <= 193:
                            pass_fields[field] += 1
                elif field ==  "hcl":
                    if value[0] == '#': 
                        for char in value[1:]:
                            if char not in hexvalues:
                                continue
                        pass_fields[field] += 1
                elif field == "ecl":
                    if value in eye_cols:
                        pass_fields[field] += 1
                elif field == "pid":
                    if len(value) == 9:
                        pass_fields[field] += 1
                else:
                    pass

    eval_answer(year, day, 2, answer)


if __name__ == "__main__":
    year, day = get_yearday(os.getcwd())
    if year == -2 or day == -2:
        sys.exit(0)
    
    if not os.path.exists(".part1tries"):
        os.system("touch .part1tries")
    if not os.path.exists(".part2tries"):
        os.system("touch .part2tries")
    
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    if not os.path.exists(".part1solved"):
        print(f"[-] Solving Part 1 for {year} {day}")
        part1(lines, year, day)
    elif os.path.exists(".part1solved") and not os.path.exists(".part2solved"):
        print(f"[-] Solving Part 2 for {year} {day}")
        part2(lines, year, day)
    else:
        print(f"You already have all of the stars for {year} {day}!")
