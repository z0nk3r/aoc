"""Module for solving today's puzzle"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import puzzle_run
from itertools import combinations
import re

shop = '''Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Nothing       0     0       0
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +0     0     0       0
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +0    0     0       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''

def fight(player, boss):
    b_hp = boss['Hit Points']
    b_dmg = boss['Damage']
    b_arm = boss['Armor']
    p_hp = player['Hit Points']
    p_dmg = player['Damage']
    p_arm = player['Armor']

    while True:
        b_hp -= max(p_dmg - b_arm, 1)
        if b_hp <= 0:
            return True
        p_hp -= max(b_dmg - p_arm, 1)
        if p_hp <= 0:
            return False


def part1(lines):
    '''Function to solve part 1'''
    answer = 0

    boss = {}
    player = {'Hit Points': 100, 'Damage': 0, 'Armor': 0}
    for line in lines:
        stat, val = line.split(": ")
        boss[stat] = int(val)

    s_weapons, s_armor, s_rings = shop.split('\n\n')
    weaps = [tuple(map(int, re.findall("(\d+)", line[10:]))) for line in s_weapons.split('\n')[1:]]
    arms = [tuple(map(int, re.findall("(\d+)", line[10:]))) for line in s_armor.split('\n')[1:]]
    rings = [tuple(map(int, re.findall("(\d+)", line[10:]))) for line in s_rings.split('\n')[1:]]

    wins = []
    for w_cost, w_dmg, w_arm in weaps:
        for a_cost, a_dmg, a_arm in arms:
            for r1, r2 in combinations(rings, 2):
                r1_cost, r1_dmg, r1_arm = r1
                r2_cost, r2_dmg, r2_arm = r2
                total_cost = w_cost + a_cost + r1_cost + r2_cost
                player['Damage'] = w_dmg + a_dmg + r1_dmg + r2_dmg
                player['Armor'] = w_arm + a_arm + r1_arm + r2_arm
                if fight(player, boss):
                    wins.append(total_cost)

    answer = min(wins)
    return answer


def part2(lines):
    '''Function to solve part 2'''
    answer = 0

    boss = {}
    player = {'Hit Points': 100, 'Damage': 0, 'Armor': 0}
    for line in lines:
        stat, val = line.split(": ")
        boss[stat] = int(val)

    s_weapons, s_armor, s_rings = shop.split('\n\n')
    weaps = [tuple(map(int, re.findall("(\d+)", line[10:]))) for line in s_weapons.split('\n')[1:]]
    arms = [tuple(map(int, re.findall("(\d+)", line[10:]))) for line in s_armor.split('\n')[1:]]
    rings = [tuple(map(int, re.findall("(\d+)", line[10:]))) for line in s_rings.split('\n')[1:]]

    losses = []
    for w_cost, w_dmg, w_arm in weaps:
        for a_cost, a_dmg, a_arm in arms:
            for r1, r2 in combinations(rings, 2):
                r1_cost, r1_dmg, r1_arm = r1
                r2_cost, r2_dmg, r2_arm = r2
                total_cost = w_cost + a_cost + r1_cost + r2_cost
                player['Damage'] = w_dmg + a_dmg + r1_dmg + r2_dmg
                player['Armor'] = w_arm + a_arm + r1_arm + r2_arm
                if not fight(player, boss):
                    losses.append(total_cost)

    answer = max(losses)
    return answer


if __name__ == "__main__":
    try:
        puzzle_run(part1, part2, bypass=True)
    except KeyboardInterrupt:
        print("")
