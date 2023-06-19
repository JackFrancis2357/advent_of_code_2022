import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()

debug = False
base_filename = "./data/input_data_12_21"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line)


def parse_monkey_lines(line, monkey_dict):
    updated = False
    vals = line.split(":")
    if vals[-1][1:].isdigit():
        if vals[0] in monkey_dict:
            pass
        else:
            monkey_dict[vals[0]] = int(vals[-1][1:])
            updated = True
    else:
        comb_vals = vals[-1].split(" ")
        if comb_vals[1] in monkey_dict:
            if comb_vals[3] in monkey_dict:
                if vals[0] in monkey_dict:
                    pass
                else:
                    monkey_dict[vals[0]] = eval(
                        f"{monkey_dict[comb_vals[1]]} {comb_vals[2]} {monkey_dict[comb_vals[3]]}"
                    )
                    updated = True
    return monkey_dict, updated


def update_lines(i, monkey_dict):
    for j in range(i):
        monkey_dict, updated = parse_monkey_lines(all_lines[j], monkey_dict)
        if updated:
            update_lines(j, monkey_dict)
    return monkey_dict


monkey_dict = {}
last_updated = 0
for i, line in enumerate(all_lines):
    monkey_dict, updated = parse_monkey_lines(line, monkey_dict)
    if updated:
        monkey_dict = update_lines(i, monkey_dict)
    if "root" in monkey_dict:
        print(monkey_dict["root"])
        break

# print(monkey_dict)
# print(monkey_dict['drzm'])


print(time.time() - start)

# Part 2
start = time.time()

debug = False
base_filename = "./data/input_data_12_21"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line)


def parse_monkey_lines_two(line, monkey_dict, humn_value):
    updated = False
    vals = line.split(":")
    if vals[-1][1:].isdigit():
        if vals[0] in monkey_dict:
            pass
        else:
            monkey_dict[vals[0]] = int(vals[-1][1:])
            if vals[0] == "humn":
                monkey_dict[vals[0]] = humn_value
            updated = True
    else:
        comb_vals = vals[-1].split(" ")
        if comb_vals[1] in monkey_dict:
            if comb_vals[3] in monkey_dict:
                if vals[0] in monkey_dict:
                    pass
                else:
                    monkey_dict[vals[0]] = eval(
                        f"{monkey_dict[comb_vals[1]]} {comb_vals[2]} {monkey_dict[comb_vals[3]]}"
                    )
                    updated = True
    return monkey_dict, updated


def update_lines_two(i, monkey_dict, humn_value):
    for j in range(i):
        monkey_dict, updated = parse_monkey_lines_two(all_lines[j], monkey_dict, humn_value)
        if updated:
            update_lines_two(j, monkey_dict, humn_value)
    return monkey_dict


monkey_dict = {}
last_updated = 0
humn_value = 3876907167495
for i, line in enumerate(all_lines):
    monkey_dict, updated = parse_monkey_lines_two(line, monkey_dict, humn_value)
    if updated:
        monkey_dict = update_lines_two(i, monkey_dict, humn_value)
    if "root" in monkey_dict:
        print(monkey_dict["root"])
        print(monkey_dict["plmp"])
        print("\n")
        print(monkey_dict["rmtt"])
        print("\n")
        print(monkey_dict["plmp"] - monkey_dict["rmtt"])
        break


print(time.time() - start)
