import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()
df = pd.read_csv("data/input_data_12_09.csv", header=None)


def move_head(curr_x, curr_y, direction):
    if direction == "R":
        curr_x += 1
    elif direction == "L":
        curr_x -= 1
    elif direction == "U":
        curr_y += 1
    elif direction == "D":
        curr_y -= 1
    return curr_x, curr_y


def move_tail(curr_head_x, curr_head_y, curr_tail_x, curr_tail_y):
    if curr_head_x == curr_tail_x and curr_head_y == curr_tail_y:
        return curr_tail_x, curr_tail_y

    x_deviation = curr_head_x - curr_tail_x
    y_deviation = curr_head_y - curr_tail_y

    if abs(x_deviation) <= 1 and abs(y_deviation) <= 1:
        return curr_tail_x, curr_tail_y

    if x_deviation == 2 and y_deviation == 0:
        curr_tail_x += 1
    elif x_deviation == -2 and y_deviation == 0:
        curr_tail_x -= 1
    elif y_deviation == 2 and x_deviation == 0:
        curr_tail_y += 1
    elif y_deviation == -2 and x_deviation == 0:
        curr_tail_y -= 1
    else:
        if x_deviation > 0:
            curr_tail_x += 1
        elif x_deviation < 0:
            curr_tail_x -= 1
        if y_deviation > 0:
            curr_tail_y += 1
        elif y_deviation < 0:
            curr_tail_y -= 1
    return curr_tail_x, curr_tail_y


curr_head_x, curr_head_y = 0, 0
curr_tail_x, curr_tail_y = 0, 0
tail_locations = []
for i in range(df.shape[0]):
    curr_direction, num_steps = df.iloc[i, 0].split(" ")
    for j in range(int(num_steps)):
        curr_head_x, curr_head_y = move_head(curr_head_x, curr_head_y, curr_direction)
        curr_tail_x, curr_tail_y = move_tail(curr_head_x, curr_head_y, curr_tail_x, curr_tail_y)
        tail_locations.append((curr_tail_x, curr_tail_y))
        # print(curr_direction, j)
        # print("Head", curr_head_x, curr_head_y)
        # print("Tail", curr_tail_x, curr_tail_y)
        # print("\n")

print(len(set(tail_locations)))
print(time.time() - start)


# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_09.csv", header=None)

num_knots = 10
location_dict = {}
for k in range(num_knots):
    location_dict[k] = [0, 0]

tail_locations = []

for i in range(df.shape[0]):
    curr_direction, num_steps = df.iloc[i, 0].split(" ")
    for j in range(int(num_steps)):
        for k in range(num_knots):
            if k == 0:
                location_dict[0] = move_head(*location_dict[0], curr_direction)
            else:
                location_dict[k] = move_tail(*location_dict[k - 1], *location_dict[k])
            if k == num_knots - 1:
                tail_locations.append((location_dict[k][0], location_dict[k][1]))

print(len(set(tail_locations)))

print(time.time() - start)
