import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()

debug = False
base_filename = "./data/input_data_12_25"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line)


def parse_snafu(val):
    ttl = 0
    snafu_lookup = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    for i, v in enumerate(reversed(val)):
        ttl += snafu_lookup[v] * (5**i)
    return ttl


def reverse_snafu(val):
    snafu_lookup = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}

    power_five = 0
    while int(val) > (5**power_five):
        power_five += 1
    x_array = [5**i for i in range(power_five)]
    original_val = val
    curr_val = 0
    curr_list = []
    possible_vals = [-2, -1, 0, 1, 2]
    for i in reversed(x_array):
        curr_add = 0
        round_start_val = curr_val
        for j in possible_vals:
            new_val = round_start_val + (i * j)
            if abs(original_val - new_val) < abs(original_val - curr_val):
                curr_val = new_val
                curr_add = j
        curr_list.append(curr_add)
        print(curr_val)
        if curr_val == original_val:
            print("Done")
            print(curr_list)
            print(*reversed(x_array))
    snafu_digits = ""
    for character in curr_list:
        snafu_digits += snafu_lookup[character]
    return snafu_digits


ttl_sum = 0
for line in all_lines:
    ttl_sum += parse_snafu(line)

print(ttl_sum)
print(reverse_snafu(ttl_sum))


print(time.time() - start)

# Part 2
start = time.time()

debug = True
base_filename = "./data/input_data_12_25"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line)


print(time.time() - start)
