# ADVENT OF CODE

Repo for all of my Advent of Code solutions and my tools. Solutions are sorted by year and day in their respective folders.


# Puzzle Auto-Grabber

Puzzle Auto-Grabber (`aoc.py`) will automatically pull the puzzle provided by the arguments on the command line and put the puzzle into the corresponding folder. 
Therefore, run this from the root level of your 'Advent of Code' folder. 

Additionally, the provided `template.py` (see below), will auto copy down into the corresponding folder for your use. Once complete, the working file and the puzzle input will open in `vscode` and the puzzle text itself will open in your most recently-focused browser window.

See below for an example of the general structure:
```shell
.
├── 2023
│   ├── 01
│   │   ├── input
│   │   └── treb.py
│   ├── 02
│   │   ├── cubes.py
│   │   ├── cubes_smol.py
│   │   └── input
│   ├── 03
│   │   ├── smol
│   │   ├── gears.py
│   │   ├── gears_smol.py
│   │   └── input
│   ├── 04
│   │   └── input

  // ~~~~~ //

│   ├── 23
│   ├── 24
│   └── 25
├── 2024
│   ├── 01
│   ├── 02
│   ├── 03
│   ├── 04

  // ~~~~~ //

│   ├── 22
│   ├── 23
│   ├── 24
│   └── 25
├── aoc.py
├── cookie.txt
├── username.txt
├── README.md
└── template.py
```

## Setup
There are two setup steps required:
* Provide your username to include as part of the User-Agent in HTTP Requests, (`username.txt`) 
* Get your individual Advent of Code account cookie (`cookie.txt`)

If you haven't completed these steps and you run the Auto-Grabber, you will be auto-prompted to manually retrieve/provide them.
```shell
    Enter your username for the User-Agent string (Will cache locally, should only have to do this once)

    => 
```

```shell
    Copy/Paste Cookie from the AoC Website
    After Logging into AoC:
    Chrome: Right-click Page > Inspect > Application > Storage > Cookies > https://adventofcode.com > Value
    (The cookie is a SHA-512, 128 chars long) (Cookie will Cache locally, should only have to do this once per login)

    =>
```

## How to Use
### Manual
```shell
$> python3 aoc.py <year> <day>
```

```shell
$> python3 aoc.py 2023 1
```
will pull the puzzle input from the 1st of December, 2023 and place it in `./2023/01/input`. If the underlying folder structure does not exist, it will be created.

If the year or day provided is in the future, a countdown will show instead:
```shell
$> python3 aoc.py 2024 1
 [X]   10D, 05H, 14M, 15S until Puzzle is Available. Waiting... 
```

Once complete, you will be notified of the download of the puzzle input. If the download fails for any reason, an error will show and it will retry the download. If the download fails more than 5 times in a row, the script will exit, and you should try again later.

```shell
[-] Downloading Puzzle Input for 2023 Day 1 to "./2023/01/input"
[!] Download Complete!
```

### Automatic
Using the `-a` option will automatically pull the current date and determine the next puzzle to download or wait for.
```shell
$> python3 aoc.py -a
```

# template

A Python3 template (`template.py`) to solve each problem is also provided. The template supports auto submission of answers and will keep track of incorrect answers tried. See below:
```python 
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

```

`open(0)` indicates the use of STDIN, so in order to run this template to solve a puzzle, use a PIPE or a FIFO on the command line. Either of the below examples work:
```shell
 $> python3 day1.py < input
 $> cat input | python3 day1.py
```