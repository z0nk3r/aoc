#!/usr/bin/env python3
import json


def print_helper1(kn, vn):
    p_flag = 0
    try:
        if vn["total_size"] <= 100000 and vn["type"] == 'dir':
            # print(f"{kn} is {vn['total_size']} bytes")
            p_flag += vn['total_size']
        # print(f"{p_flag = }")
    except: pass
    return p_flag

def print_helper2(kn, vn):
    p_flag = 0
    try:
        if vn["total_size"] >= (30000000-(70000000-43629016)) and vn["type"] == 'dir':
            print(f"{kn} is {vn['total_size']} bytes")
            # p_flag += vn['total_size']
        # print(f"{p_flag = }")
    except: pass
    return p_flag

def main():

    with open("../input.txt") as input:
        commands = [x.replace("\n", "") for x in input.readlines()]

    dir_dict = {'/': {"total_size": 0, "type": "dir"}}
    dir_depth = []
    deepest_dir = 0

    #
    #   vvv Parsing commands to json dir structure vvv
    #

    for idx, command in enumerate(commands):
        # print(f"{idx+1} {command}")

        try:
            cur_dir = eval("dir_dict[\'"+'\'][\''.join(dir_depth)+"\']")
        except KeyError:
            pass

        args = command.split()
        # if a cli command
        if args[0] == "$":

            # $cd handling
            if args[1] == 'cd':
                if args[2] == '..':
                    dir_depth.pop()
                else:
                    dir_depth.append(args[2])

            # $ls handling
            elif args[1] == 'ls':
                continue

            else:
                pass

        # if not a command
        else:
            # dir
            if args[0] == 'dir':
                cur_dir[args[1]] = {}
                cur_dir[args[1]]["total_size"] = 0
                cur_dir[args[1]]["type"] = 'dir'

            # file
            else:
                file_size = int(args[0])
                file = args[1]
                cur_dir[file] = {}
                cur_dir[file]['size'] = file_size
                cur_dir[file]['type'] = 'file'
                try:
                    cur_dir["total_size"] += file_size
                    # add file_size to total dir sizes all the way back up
                    try:
                        for i in range(1, len(dir_depth)):
                            if len(dir_depth) > deepest_dir:
                                deepest_dir = len(dir_depth)
                            try:
                                temp_dir = eval("dir_dict[\'"+'\'][\''.join(dir_depth[0:i])+"\']")
                                temp_dir["total_size"] += file_size
                            except KeyError:
                                pass
                    except KeyError:
                        pass
                except KeyError:
                    pass

    # write dir structure to file
    with open("../input.json", 'w') as out_json:
        json.dump(dir_dict, out_json, indent=4)

    # print(f"{deepest_dir = }")

    print("====== part 1 ======")
    # global flag
    flag = 0
    
    with open("../input.json", 'r') as in_json:
        json_data = json.load(in_json)

    # print(type(dir_dict))
    # print(type(json_data))
    # try:

    for k1, v1 in json_data.items():
        flag += print_helper1(k1, v1)
        if isinstance(v1, dict):
            for k2, v2 in v1.items():
                flag += print_helper1(k2, v2)
                if isinstance(v2, dict):
                    for k3, v3 in v2.items():
                        flag += print_helper1(k3, v3)
                        if isinstance(v3, dict):
                            for k4, v4 in v3.items():
                                flag += print_helper1(k4, v4)
                                if isinstance(v4, dict):
                                    for k5, v5 in v4.items():
                                        flag += print_helper1(k5, v5)
                                        if isinstance(v5, dict):
                                            for k6, v6 in v5.items():
                                                flag += print_helper1(k6, v6)
                                                if isinstance(v6, dict):
                                                    for k7, v7 in v6.items():
                                                        flag += print_helper1(k7, v7)
                                                        if isinstance(v7, dict):
                                                            for k8, v8 in v7.items():
                                                                flag += print_helper1(k8, v8)
                                                                if isinstance(v8, dict):
                                                                    for k9, v9 in v8.items():
                                                                        flag += print_helper1(k9, v9)
                                                                        if isinstance(v9, dict):
                                                                            for k10, v10 in v9.items():
                                                                                flag += print_helper1(k10, v10)
                                                                                if isinstance(v10, dict):
                                                                                    for k11, v11 in v10.items():
                                                                                        flag += print_helper1(k11, v11)
                                                                                        if isinstance(v11, dict):
                                                                                            for k12, v12 in v11.items():
                                                                                                flag += print_helper1(k12, v12)
                                                                                                if isinstance(v12, dict):
                                                                                                    for k13, v13 in v12.items():
                                                                                                        flag += print_helper1(k13, v13)
                                                                                                else: pass
                                                                                        else: pass
                                                                                else: pass
                                                                        else: pass
                                                                else: pass
                                                        else: pass
                                                else: pass
                                        else: pass
                                else: pass
                        else: pass
                else: pass
        else: print("no v1 items)")

    print(f"\n{flag = }")
    print("flag should be 1845346")

    print("====== part 2 ======")
    flag = 0
    print(f"Looking for gte: {30000000-(70000000-43629016)}")
    for k1, v1 in json_data.items():
        flag += print_helper2(k1, v1)
        if isinstance(v1, dict):
            for k2, v2 in v1.items():
                flag += print_helper2(k2, v2)
                if isinstance(v2, dict):
                    for k3, v3 in v2.items():
                        flag += print_helper2(k3, v3)
                        if isinstance(v3, dict):
                            for k4, v4 in v3.items():
                                flag += print_helper2(k4, v4)
                                if isinstance(v4, dict):
                                    for k5, v5 in v4.items():
                                        flag += print_helper2(k5, v5)
                                        if isinstance(v5, dict):
                                            for k6, v6 in v5.items():
                                                flag += print_helper2(k6, v6)
                                                if isinstance(v6, dict):
                                                    for k7, v7 in v6.items():
                                                        flag += print_helper2(k7, v7)
                                                        if isinstance(v7, dict):
                                                            for k8, v8 in v7.items():
                                                                flag += print_helper2(k8, v8)
                                                                if isinstance(v8, dict):
                                                                    for k9, v9 in v8.items():
                                                                        flag += print_helper2(k9, v9)
                                                                        if isinstance(v9, dict):
                                                                            for k10, v10 in v9.items():
                                                                                flag += print_helper2(k10, v10)
                                                                                if isinstance(v10, dict):
                                                                                    for k11, v11 in v10.items():
                                                                                        flag += print_helper2(k11, v11)
                                                                                        if isinstance(v11, dict):
                                                                                            for k12, v12 in v11.items():
                                                                                                flag += print_helper2(k12, v12)
                                                                                                if isinstance(v12, dict):
                                                                                                    for k13, v13 in v12.items():
                                                                                                        flag += print_helper2(k13, v13)
                                                                                                else: pass
                                                                                        else: pass
                                                                                else: pass
                                                                        else: pass
                                                                else: pass
                                                        else: pass
                                                else: pass
                                        else: pass
                                else: pass
                        else: pass
                else: pass
        else: print("no v1 items)")


if __name__ == "__main__":
    main()
