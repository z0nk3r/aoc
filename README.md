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
├── lib
│   ├── __init__.py
│   ├── cookie.txt
│   ├── username.txt
│   └── utils.py
├── README.md
└── template.py
```

## Setup
There are two setup steps required:
* Provide your username to include as part of the User-Agent in HTTP Requests, (`lib/username.txt`) 
* Get your individual Advent of Code account cookie (`lib/cookie.txt`)

Typically, just run the Auto-Grabber. You will be auto-prompted to manually retrieve/provide the above setup items.
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
- For both the manual and automatic methods, run `aoc.py` from the root level directory (the dir you `git clone`-d down)

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
 [x]   10D, 05H, 14M, 15S until Puzzle is Available. Waiting... 
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
[!] Auto-Grabber: Next Puzzle is 2024 01
 [x]   10D, 05H, 14M, 15S until Puzzle is Available. Waiting... 
```

### Workflow
Generally, the workflow to solve a problem is as follows:

- `cd <root-dir>`
- `python3 aoc.py -a`
    - puzzle will download, template will copy down to `<year>/<day>` dir
    - vscode will open working file `day<day>.py` and puzzle `input`
    - puzzle website will open in most-recently-used browser window
- `cd <year>/<day>`
- edit `day<day>.py` part1
    - `python3 day<day>.py < input`
    - answer autosubmits
    - repeat/rework until correct

- edit `day<day>.py` part2
    - `python3 day<day>.py < input`
    - answer for part2 autosubmits
    - repeat/rework until correct

- `cd ../..` (back to the root-dir)
- `python3 aoc.py -a` (to sit in countdown and wait for the next days problem)


# template

A Python3 template (`template.py`) to solve each problem is also provided. The template supports auto submission of answers and will keep track of incorrect answers tried. 

See below:
```python
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import eval_answer, puzzle_setup, puzzle_run


def part1(lines, year, day):
    answer = 0
    
    for line in lines:
        print(line)
    
    '''
    solve part 1 of the problem here
    # answer = <the answer to the problem>
    '''
    
    # eval_answer(year, day, 1, answer)


def part2(lines, year, day):
    answer = 0
    
    for line in lines:
        print(line)
    
    '''
    solve part 2 of the problem here
    # answer = <the answer to the problem>
    '''
    
    # eval_answer(year, day, 2, answer)


if __name__ == "__main__":
    year, day = puzzle_setup()
    
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    puzzle_run(part1, part2, lines, year, day)
```

`open(0)` indicates the use of STDIN, so in order to run this template to solve a puzzle, use a PIPE or a FIFO on the command line. Either of the below examples work:
```shell
 $> python3 day1.py < input
 $> cat input | python3 day1.py
```

If correctly solved, you should see an output similar to this:
```shell
user@hostname:~/aoc/2020/04 $ python3 day04.py < input
[-] Attempting answer of 190 for 2020 04 - part 1
[-] 1. 190 - Correct! ⭐
user@hostname:~/aoc/2020/04 $ python3 day04.py < input
[-] Solving Part 2 for 2020 4
[-] Attempting answer of 121 for 2020 04 - part 2
[-] 2. 121 - Correct! ⭐⭐
```