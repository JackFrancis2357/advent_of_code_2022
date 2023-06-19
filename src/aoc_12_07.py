import sys
import time

import numpy as np
import pandas as pd

# Part 1 Original
start = time.time()
df = pd.read_csv("data/input_data_12_07.csv", header=None)

full_directory = {}

curr_path = "/"
for i in range(df.shape[0]):
    if i == 0:
        curr_path = df.iloc[i, 0].split(" ")[-1]
        full_directory[curr_path] = 0
    elif df.iloc[i, 0] == "$ cd ..":
        curr_path = curr_path[:-1].rsplit("/", 1)[0] + "/"
    elif df.iloc[i, 0][0:4] == "$ cd":
        curr_path = curr_path + df.iloc[i, 0].split(" ")[-1] + "/"
        full_directory[curr_path] = 0  # Add directory to full directory
    elif df.iloc[i, 0][0].isdigit():
        full_directory[curr_path] += int(df.iloc[i, 0].split(" ")[0])
    elif df.iloc[i, 0].split(" ")[0] == "dir":
        full_directory[curr_path + df.iloc[i, 0].split(" ")[-1] + "/"] = 0

# print(full_directory)

ttl = 0
total_size_dict = {}
for k1, v1 in full_directory.items():
    total_size_dict[k1] = 0
    for k, v in full_directory.items():
        if k1 == k[: len(k1)]:
            total_size_dict[k1] += full_directory[k]

# print(total_size_dict)
for k2, v2 in total_size_dict.items():
    if total_size_dict[k2] < 100000:
        ttl += total_size_dict[k2]

print(ttl)
print(time.time() - start)

# Part 2 Original
start = time.time()
df = pd.read_csv("data/input_data_12_07.csv", header=None)

total_disk_space = 70_000_000
update_required = 30_000_000

unused_space = total_disk_space - total_size_dict["/"]
target_amt_delete = update_required - unused_space

dir_diff = 100000000
dir_size = 0

for k3, v3 in total_size_dict.items():
    if total_size_dict[k3] - target_amt_delete > 0:
        overage = total_size_dict[k3] - target_amt_delete
        if overage < dir_diff:
            dir_diff = overage
            dir_size = total_size_dict[k3]


print(dir_size)
print(time.time() - start)


# Part 1 Cleaned up
start = time.time()
df = pd.read_csv("data/input_data_12_07.csv", header=None)

full_directory = {}

# curr_path = "/"
for i in range(df.shape[0]):
    command_vals = df.iloc[i, 0].split(" ")

    # Easier to sort out the first line with an if because it has a unique start
    if i == 0:
        curr_path = command_vals[-1]
        full_directory[curr_path] = 0

    # If we go up a directory, just remove the last bit from the current path
    elif df.iloc[i, 0] == "$ cd ..":
        curr_path = curr_path[:-1].rsplit("/", 1)[0] + "/"

    # If we move into a new directory, update the current path
    elif df.iloc[i, 0][0:4] == "$ cd":
        curr_path = curr_path + command_vals[-1] + "/"

    # If we get a value for file size, add that to the corespondign fully qual filepath
    elif df.iloc[i, 0][0].isdigit():
        full_directory[curr_path] += int(command_vals[0])

    # If we get a dir, add that as a new key to the dict
    elif command_vals[0] == "dir":
        full_directory[curr_path + command_vals[-1] + "/"] = 0


# Keep track of running total if full qual dir size < 100_000
ttl = 0
total_size_dict = {}
for k1, v1 in full_directory.items():
    # Initialize a counter for overall full qual dir size
    total_size_dict[k1] = 0
    for k2, v2 in full_directory.items():
        # Check if this is a subdirectory of the current dir
        if k1 == k2[: len(k1)]:
            total_size_dict[k1] += full_directory[k2]
    if total_size_dict[k1] < 100000:
        ttl += total_size_dict[k1]


print(ttl)
print(time.time() - start)
