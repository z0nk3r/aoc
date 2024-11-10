import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from lib import eval_answer, get_yearday


def part1(lines, year, day):
    answer = 0
    
    bag_graph = {}
    bag_path = set()
    
    # build db
    for line in lines:
        children_bags = []
        line_items = line.split(" ")
        parent_bag = f"{line_items[0]} {line_items[1]}"
        children = " ".join(line_items[4:])
        childrens = children.split(",")
        for child in childrens:
            if "no other bags" not in child:
                split_child = child.strip().split(" ")
                children_bags.append(f"{split_child[1]} {split_child[2]}")
        
        bag_graph[parent_bag] = children_bags
    
    # bfs
    start = "shiny gold"
    neighbors = []
    neighbors.append(start)
    
    while neighbors != []:
        curr = neighbors.pop()
        for parent, children in bag_graph.items():
            if curr in children:
                neighbors.append(parent)
                bag_path.add(parent)
    
    answer = len(bag_path)
    print(f"{bag_path = }\n{answer = }")
    eval_answer(year, day, 1, answer)


def part2(lines, year, day):
    
    bag_graph = {}
    
    # build db
    for line in lines:
        total_count = 0
        children_bags = []
        line_items = line.split(" ")
        parent_bag = f"{line_items[0]} {line_items[1]}"
        children = " ".join(line_items[4:])
        childrens = children.split(",")
        for child in childrens:
            if "no other bags" not in child:
                split_child = child.strip().split(" ")
                total_count += int(split_child[0])
                children_bags.append({"count": int(split_child[0]), "child": f"{split_child[1]} {split_child[2]}"})
        
        bag_graph[parent_bag] = {"total": total_count, "children": children_bags}
    
    # bfs
    answer = 0
    start = "shiny gold"
    bag_path = set()
    bag_path.add(start)
    neighbors = []
    neighbors.append(start)
    
    while neighbors != []:
        curr = neighbors.pop()
        for parent, data in bag_graph.items():
            if curr == parent:
                for children in data["children"]:
                    neighbors.append(children["child"])
                    bag_path.add(children["child"])
    
    # [ ] Needs a rewrite for recusrive multiplication, not simple multiplication
    
    print(f'{bag_path = }')
    answer += bag_graph[start]["total"]
    for bag in bag_path:
        for children in bag_graph[bag]["children"]:
            print(f"{child = }")
            print(f'{children["count"] = } * {bag_graph[children["child"]]["total"] = }')
            answer += ( children["count"] * bag_graph[children["child"]]["total"] )
            print(f"{answer = }")

    print(f"final {answer = }")
    # 1151 too low
    # eval_answer(year, day, 2, answer)


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
