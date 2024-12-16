"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from time import sleep


def print_maze(move, max_moves, maze):
    fps = 300
    print("\033[2J\033[;H")
    print(f"{move} of {max_moves}")
    for row in maze:
        print(' '.join(row))
    sleep(1/fps)


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    maze = []
    moves = ''
    bot = (-1, -1)
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    for lidx, line in enumerate(lines):
        if line == '':
            maze = lines[:lidx]
            moves = ''.join(lines[lidx+1:])
    for ridx, row in enumerate(maze):
        maze[ridx] = list(row)
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == '@':
                bot = (ridx, cidx)

    print_maze(0, len(moves), maze)
    for midx, move in enumerate(moves):
        dir_r, dir_c = dirs[move]
        moves_todo = []
        moves_todo.append(bot)
        do_move = True

        for mov_r, mov_c in moves_todo:
            new_r = mov_r + dir_r
            new_c = mov_c + dir_c
            if (new_r, new_c) in moves_todo:
                continue
            n_char = maze[new_r][new_c]
            if n_char == '#':
                do_move = False
                break
            if n_char == "O":
                moves_todo.append((new_r, new_c))

        if not do_move:
            continue

        maze[bot[0]][bot[1]] = '.'
        maze[bot[0] + dir_r][bot[1] + dir_c] = '@'

        for mov_r, mov_c in moves_todo[1:]:
            maze[mov_r][mov_c] = '.'
        for mov_r, mov_c in moves_todo[1:]:
            maze[mov_r + dir_r][mov_c + dir_c] = 'O'

        bot = (bot[0] + dir_r, bot[1] + dir_c)
        print_maze(midx, len(moves), maze)
    print_maze(len(moves), len(moves), maze)

    # answer
    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == 'O':
                answer += 100 * ridx + cidx

    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    maze = []
    moves = ''
    bot = (-1, -1)
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    for lidx, line in enumerate(lines):
        if line == '':
            maze = lines[:lidx]
            moves = ''.join(lines[lidx+1:])
    for ridx, row in enumerate(maze):
        row = row.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
        maze[ridx] = list(row)
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == '@':
                bot = (ridx, cidx)

    print_maze(0, len(moves), maze)
    for midx, move in enumerate(moves):
        dir_r, dir_c = dirs[move]
        moves_todo = []
        moves_todo.append(bot)
        do_move = True
        maze_bak = [list(row) for row in maze]

        for mov_r, mov_c in moves_todo:
            new_r = mov_r + dir_r
            new_c = mov_c + dir_c
            if (new_r, new_c) in moves_todo:
                continue
            n_char = maze[new_r][new_c]
            if n_char == '#':
                do_move = False
                break
            if n_char == "[":
                moves_todo.append((new_r, new_c))
                moves_todo.append((new_r, new_c + 1))
            if n_char == "]":
                moves_todo.append((new_r, new_c))
                moves_todo.append((new_r, new_c - 1))

        if not do_move:
            continue

        maze[bot[0]][bot[1]] = '.'
        maze[bot[0] + dir_r][bot[1] + dir_c] = '@'

        for mov_r, mov_c in moves_todo[1:]:
            maze[mov_r][mov_c] = '.'
        for mov_r, mov_c in moves_todo[1:]:
            maze[mov_r + dir_r][mov_c + dir_c] = maze_bak[mov_r][mov_c]
        
        bot = (bot[0] + dir_r, bot[1] + dir_c)
        print_maze(midx, len(moves), maze)
    print_maze(len(moves), len(moves), maze)

    # answer
    for ridx, row in enumerate(maze):
        for cidx, col in enumerate(row):
            if maze[ridx][cidx] == '[':
                answer += 100 * ridx + cidx

    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2)
    except KeyboardInterrupt:
        print("")
