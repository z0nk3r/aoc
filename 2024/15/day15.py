"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run


def print_maze(maze):
    for row in maze:
        print(' '.join(row))
    return ''


def handle_move(char, move, location, maze):
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    c_dir = dirs[move]
    new_r = location[0] + c_dir[0]
    new_c = location[1] + c_dir[1]
    if maze[new_r][new_c] == '.':
        pass
    elif maze[new_r][new_c] == '#':
        return False, location
    elif maze[new_r][new_c] == 'O':
        status, loc = handle_move('O', move, (new_r, new_c), maze)
        if not status:
            return False, location

    maze[location[0]][location[1]] = '.'
    maze[new_r][new_c] = char
    loc = (new_r, new_c)
    return True, loc

def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    maze = []
    moves = ''
    bot = (-1, -1)

    for lidx, line in enumerate(lines):
        if line == '':
            maze = lines[:lidx]
            moves = ''.join(lines[lidx+1:])
    for ridx, row in enumerate(maze):
        maze[ridx] = list(row)
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == '@':
                bot = (ridx, cidx)

    for move in moves:
        _, bot = handle_move('@', move, bot, maze)

    # answer
    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == 'O':
                answer += 100 * ridx + cidx

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    for line in lines:
        print(line)

    # solve part 2 of the problem here
    # answer = <the answer to the problem>
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
