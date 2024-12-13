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
In regards to the general workflow: in the editing and submitting portions below, the part to answer will automatically be determined by using hidden dotfiles in the challenge's directory. These files are automatically generated when a part to a challenge is completed (`.part1solved` & `.part2solved`). Additionally, previously submitted answers are cached in the challenge's directory so as not to overload the AoC server or cause a self-induced timeout (`.part1tries` & `.part2tries`). Upon re-encountering a previous attempt, or attempting to re-solve an already completed challenge, the user is notified accordingly.

Before sending the attempted answer, your solution will be tested against the test data provided in the challenge's writeup. 
This requires manual copy-pasting (for now) of the example puzzle input into the `test` file. If your solution fails the attempt, 
then your attempted answer will not be sent to the AoC server as a further mitigation of self-induced timeouts.

Generally, the workflow to solve a problem is as follows:

- `cd <root-dir>`
- `python3 aoc.py -a`
    - puzzle will download, template will copy down to `<year>/<day>` dir
    - vscode will open working file `day<day>.py`, puzzle `input`, and `test` file for test puzzle input.
    - puzzle website will open in most-recently-used/focused browser window
- `cd <year>/<day>`

- edit `day<day>.py` part1
    - `python3 day<day>.py < input`
    - answer for part1 autosubmits if tests pass
    - otherwise, repeat/rework until correct

- edit `day<day>.py` part2
    - `python3 day<day>.py < input`
    - answer for part2 autosubmits if tests pass
    - otherwise, repeat/rework until correct

- `cd ../..` (back to the root-dir)
- `python3 aoc.py -a` (to sit in countdown and wait for the next days problem)


# template

A Python3 template (`template.py`) to solve each problem is also provided. The template supports auto submission of answers, testing of possible solutions, and keeps track of incorrect answers tried using the `lib/utils` functions at the root level.

See below:
```python
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run


def part1(lines):
    answer = 0
    
    for line in lines:
        print(line)
    
    '''
    solve part 1 of the problem here
    # answer = <the answer to the problem>
    '''
    return answer


def part2(lines):
    answer = 0
    
    for line in lines:
        print(line)
    
    '''
    solve part 2 of the problem here
    # answer = <the answer to the problem>
    '''
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")

```

By default, the template will use the local `input` puzzle file. However, the use of `STDIN` is supported.
To run this template to solve a puzzle using `STDIN`, use a PIPE or a FIFO on the command line. Either of the below examples work:
```shell
 $> python3 day1.py < input
 $> cat input | python3 day1.py
```

If correctly solved, you should see an output similar to this:
```shell
user@hostname:~/aoc/2024/10 (2024)$ python3 day10.py 
[*] Solving Part 1 for 2024 10
[*] Checking current solution against the test data.
  [✔] Test solution passed! (36)
[*] Sending answer of (709) for 2024 10 - part 1

[✔] 1. 709 - Correct! ⭐
user@hostname:~/aoc/2024/10 (2024)$ python3 day10.py 
[*] Solving Part 2 for 2024 10
[*] Checking current solution against the test data.
  [✔] Test solution passed! (81)
[*] Sending answer of (1326) for 2024 10 - part 2

[✔] 2. 1326 - Correct! ⭐⭐
```