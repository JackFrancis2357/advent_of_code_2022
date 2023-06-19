import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()


def generate_array(arr, first, second, min_value):
    first_x, first_y = first.split(",")
    second_x, second_y = second.split(",")
    first_x, first_y, second_x, second_y = int(first_x), int(first_y), int(second_x), int(second_y)
    if second_x < first_x:
        first_x, second_x = second_x, first_x
    elif second_y < first_y:
        first_y, second_y = second_y, first_y
    if first_y == second_y:
        arr[first_y, first_x - min_value : second_x - min_value + 1] = 1
    elif first_x == second_x:
        arr[first_y : second_y + 1, first_x - min_value] = 1
    return arr


def get_min_max(all_lines):
    max_x = -1
    max_y = -1
    min_x = 100000
    min_y = 100000
    for line in all_lines:
        for i, entry in enumerate(line):
            y, x = entry.split(",")
            x, y = int(x), int(y)
            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y
    return min_x, max_x, min_y, max_y


def move_sand(arr, x, y):
    try:
        if arr[x + 1, y] != 1:
            arr[x, y] = 0
            arr[x + 1, y] = 1
            return arr, x + 1, y
        elif arr[x + 1, y - 1] != 1:
            arr[x, y] = 0
            arr[x + 1, y - 1] = 1
            return arr, x + 1, y - 1
        elif arr[x + 1, y + 1] != 1:
            arr[x, y] = 0
            arr[x + 1, y + 1] = 1
            return arr, x + 1, y + 1
        else:
            return arr, None, None
    except IndexError:
        return arr, "Finished", "Finished"


debug = False
base_filename = "./data/input_data_12_14"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line.split("->"))

min_x, max_x, min_y, max_y = get_min_max(all_lines)
if min_x > 0:
    min_x = 0
sand_array = np.zeros((max_x - min_x + 1, max_y - min_y + 1))

for rock_form in all_lines:
    for i in range(len(rock_form) - 1):
        sand_array = generate_array(sand_array, rock_form[i], rock_form[i + 1], min_y)

start_index = 500
curr_x = 0
curr_y = start_index - min_y
ctr = 0
while True:
    if curr_x == "Finished" and curr_y == "Finished":
        break
    curr_x, curr_y = 0, start_index - min_y
    while curr_x is not None and curr_y is not None:
        sand_array, new_x, new_y = move_sand(sand_array, curr_x, curr_y)
        curr_x, curr_y = new_x, new_y
        if curr_x == "Finished" and curr_y == "Finished":
            print(ctr)
            break
    ctr += 1

print(time.time() - start)

# Part 2
start = time.time()

debug = False
base_filename = "./data/input_data_12_14"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line.split("->"))

min_x, max_x, min_y, max_y = get_min_max(all_lines)
max_x += 2
if min_x > 0:
    min_x = 0
sand_array = np.zeros((max_x - min_x + 1, 1000))

for rock_form in all_lines:
    for i in range(len(rock_form) - 1):
        sand_array = generate_array(sand_array, rock_form[i], rock_form[i + 1], 0)

sand_array[-1, :] = 1
ctr = 0
while True:
    curr_x, curr_y = 0, start_index
    if sand_array[curr_x, curr_y] == 1:
        print(ctr)
        break
    while curr_x is not None and curr_y is not None:
        sand_array[curr_x, curr_y] = 1
        sand_array, new_x, new_y = move_sand(sand_array, curr_x, curr_y)
        curr_x, curr_y = new_x, new_y
    ctr += 1

print(time.time() - start)
