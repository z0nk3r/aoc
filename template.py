import os

from aoc import submit_answer, aoc_timeout


def check_if_old_answer(part: int, answer: int) -> bool:
    given_answers = [line.replace("\n", "") for line in open(f".part{part}tries").readlines()]
    return answer in given_answers

def add_to_bad_answers(part: int, answer: int):
    with open(f".part{part}tries", "a") as given_answers:
        given_answers.write(answer)


def eval_answer(year: int, day: int, part: int, answer: int) -> None:
    if check_if_old_answer(part, answer):
        print("[!] You already tried this answer!")
        return
    b_submit, response = submit_answer(year, day, part, answer)
    if b_submit:
        os.system(f"touch .part{part}solved")
        print(f"{part}. {answer} - {response}")
    else:
        print(f"{part} - {answer} was incorrect.")
        add_to_bad_answers(part, answer)
        aoc_timeout(response)


def part1(lines):
    for line in lines:
        pass
    
    '''
    solve part 1 of the problem here
    '''
    
    # answer = <the answer to the problem>
    # eval_answer(year, day, 1, answer)


def part2(lines):
    for line in lines:
        pass
    
    
    '''
    solve part 2 of the problem here
    '''
    
    # answer = <the answer to the problem>
    # eval_answer(year, day, 2, answer)


if __name__ == "__main__":
    # placeholders; update before running
    year = -1
    day = -1
    
    if not os.path.exists(".part1tries"):
        os.system("touch .part1tries")
    if not os.path.exists(".part2tries"):
        os.system("touch .part2tries")
    
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    if not os.path.exists(".part1solved"):
        part1(lines, year, day)
    elif os.path.exists(".part1solved") and not os.path.exists(".part2solved"):
        part2(lines, year, day)
    else:
        print("You already have these stars!")
