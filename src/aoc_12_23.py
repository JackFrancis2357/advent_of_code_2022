import sys
import time
from collections import Counter

import numpy as np
import pandas as pd

# Part 1
start = time.time()
df = pd.read_csv("data/input_data_12_23.csv", header=None)
df_e = pd.read_csv("data/input_data_12_23_example.csv", header=None)

debug = True
if debug:
    curr_df = df_e
else:
    curr_df = df

elf_dict = {}
ctr = 0
for i in range(curr_df.shape[0]):
    for j, sym in enumerate(curr_df.iloc[i, 0]):
        if sym == "#":
            print(i, j)
            elf_dict[f"elf_{ctr}"] = {"curr_pos": (i, j), "proposed_pos": (None, None)}
            ctr += 1


def get_all_curr_pos(elf_dict):
    curr_pos_list = []
    for k, v in elf_dict.items():
        curr_pos_list.append(elf_dict[k]["curr_pos"])
    return curr_pos_list


def get_elf_move(elf_curr_pos, curr_pos_list, curr_dir_val):
    all_poss_vals = [
        (elf_curr_pos[0] - 1, elf_curr_pos[1] - 1),
        (elf_curr_pos[0] - 1, elf_curr_pos[1]),
        (elf_curr_pos[0] - 1, elf_curr_pos[1] + 1),
        (elf_curr_pos[0] + 1, elf_curr_pos[1] - 1),
        (elf_curr_pos[0] + 1, elf_curr_pos[1]),
        (elf_curr_pos[0] + 1, elf_curr_pos[1] + 1),
        (elf_curr_pos[0], elf_curr_pos[1] - 1),
        (elf_curr_pos[0], elf_curr_pos[1] + 1),
    ]
    int_all_poss_vals = [i for i in all_poss_vals if i in curr_pos_list]
    if len(int_all_poss_vals) == 0:
        return (elf_curr_pos[0], elf_curr_pos[1])
    for i in range(4):
        dir_v = (i + curr_dir_val) % 4
        # North
        if dir_v == 0:
            poss_vals = [
                (elf_curr_pos[0] - 1, elf_curr_pos[1] - 1),
                (elf_curr_pos[0] - 1, elf_curr_pos[1]),
                (elf_curr_pos[0] - 1, elf_curr_pos[1] + 1),
            ]
            int_vals = [i for i in poss_vals if i in curr_pos_list]
            if len(int_vals) == 0:
                return (elf_curr_pos[0] - 1, elf_curr_pos[1])
            else:
                continue
        # South
        elif dir_v == 1:
            poss_vals = [
                (elf_curr_pos[0] + 1, elf_curr_pos[1] - 1),
                (elf_curr_pos[0] + 1, elf_curr_pos[1]),
                (elf_curr_pos[0] + 1, elf_curr_pos[1] + 1),
            ]
            int_vals = [i for i in poss_vals if i in curr_pos_list]
            if len(int_vals) == 0:
                return (elf_curr_pos[0] + 1, elf_curr_pos[1])
            else:
                continue
        # West
        elif dir_v == 2:
            poss_vals = [
                (elf_curr_pos[0] - 1, elf_curr_pos[1] - 1),
                (elf_curr_pos[0], elf_curr_pos[1] - 1),
                (elf_curr_pos[0] + 1, elf_curr_pos[1] - 1),
            ]
            int_vals = [i for i in poss_vals if i in curr_pos_list]
            if len(int_vals) == 0:
                return (elf_curr_pos[0], elf_curr_pos[1] - 1)
            else:
                continue
        # East
        elif dir_v == 3:
            poss_vals = [
                (elf_curr_pos[0] - 1, elf_curr_pos[1] + 1),
                (elf_curr_pos[0], elf_curr_pos[1] + 1),
                (elf_curr_pos[0] + 1, elf_curr_pos[1] + 1),
            ]
            int_vals = [i for i in poss_vals if i in curr_pos_list]
            if len(int_vals) == 0:
                return (elf_curr_pos[0], elf_curr_pos[1] + 1)
            else:
                continue
    return elf_curr_pos


def print_elf_locations(elf_dict):
    min_x, max_x, min_y, max_y = 10000, -10, 10000, -10
    for k, v in elf_dict.items():
        x, y = elf_dict[k]["curr_pos"]
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    x_size = max_x - min_x
    y_size = max_y - min_y
    a = np.zeros((x_size + 1, y_size + 1))
    for k, v in elf_dict.items():
        cp_x, cp_y = elf_dict[k]["curr_pos"]
        a[cp_x - min_x, cp_y - min_y] = 1
    a = a.astype("str")
    a[a == "0.0"] = "."
    a[a == "1.0"] = "#"
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            print(a[i, j], end="")
        print("\n")
    # print(a)
    print("\n")


print_elf_locations(elf_dict)
num_elves = len(elf_dict.keys())
for round in range(10):
    dir_val = round % 4
    round_proposed_list = []
    curr_pos_list = get_all_curr_pos(elf_dict)
    for elf in range(num_elves):
        elf_curr_pos = elf_dict[f"elf_{elf}"]["curr_pos"]
        new_pos = get_elf_move(elf_curr_pos, curr_pos_list, dir_val)
        elf_dict[f"elf_{elf}"]["proposed_pos"] = new_pos
        round_proposed_list.append(new_pos)
    round_proposed_list = [k for k, v in Counter(round_proposed_list).items() if v == 1]
    for elf in range(num_elves):
        if elf_dict[f"elf_{elf}"]["proposed_pos"] in round_proposed_list:
            elf_dict[f"elf_{elf}"]["curr_pos"] = elf_dict[f"elf_{elf}"]["proposed_pos"]
    print_elf_locations(elf_dict)

min_x, max_x, min_y, max_y = 10000, -10, 10000, -10
for k, v in elf_dict.items():
    x, y = elf_dict[k]["curr_pos"]
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

print(max_x, min_x, max_y, min_y)
print((max_x - min_x + 1) * (max_y - min_y + 1) - num_elves)

print(time.time() - start)

# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_23.csv", header=None)
df_e = pd.read_csv("data/input_data_12_23_example.csv", header=None)

debug = False
if debug:
    curr_df = df_e
else:
    curr_df = df

elf_dict = {}
ctr = 0
for i in range(curr_df.shape[0]):
    for j, sym in enumerate(curr_df.iloc[i, 0]):
        if sym == "#":
            print(i, j)
            elf_dict[f"elf_{ctr}"] = {"curr_pos": (i, j), "proposed_pos": (None, None)}
            ctr += 1


def check_elf_no_move(elf_dict):
    for k, v in elf_dict.items():
        if elf_dict[k]['curr_pos'] == elf_dict[k]['proposed_pos']:
            continue
        else:
            return False
    return True


print_elf_locations(elf_dict)
num_elves = len(elf_dict.keys())
for round in range(1000):
    dir_val = round % 4
    round_proposed_list = []
    curr_pos_list = get_all_curr_pos(elf_dict)
    for elf in range(num_elves):
        elf_curr_pos = elf_dict[f"elf_{elf}"]["curr_pos"]
        new_pos = get_elf_move(elf_curr_pos, curr_pos_list, dir_val)
        elf_dict[f"elf_{elf}"]["proposed_pos"] = new_pos
        round_proposed_list.append(new_pos)
    if check_elf_no_move(elf_dict):
        print(round + 1)
        sys.exit(1)
    round_proposed_list = [k for k, v in Counter(round_proposed_list).items() if v == 1]
    for elf in range(num_elves):
        if elf_dict[f"elf_{elf}"]["proposed_pos"] in round_proposed_list:
            elf_dict[f"elf_{elf}"]["curr_pos"] = elf_dict[f"elf_{elf}"]["proposed_pos"]
    # print_elf_locations(elf_dict)
    print(round)

min_x, max_x, min_y, max_y = 10000, -10, 10000, -10
for k, v in elf_dict.items():
    x, y = elf_dict[k]["curr_pos"]
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

print(max_x, min_x, max_y, min_y)
print((max_x - min_x + 1) * (max_y - min_y + 1) - num_elves)

print(time.time() - start)

print(time.time() - start)
