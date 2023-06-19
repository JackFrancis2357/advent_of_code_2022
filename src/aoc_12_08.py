import re
import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()
df = pd.read_csv("data/input_data_12_08_parsed.csv", header=None)
vis_array = np.zeros((df.shape[0], df.shape[1])).astype(np.int8)

min_ind = 0
max_ind = df.shape[0]

# Check looking left to right
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        vals = df.iloc[i, min_ind:j].tolist()
        if len(vals) == 0:
            vis_array[i, j] = 1
        elif int(df.iloc[i, j]) > max(vals):
            vis_array[i, j] = 1
        else:
            continue

# Check looking right to left
for i in range(df.shape[0]):
    for j in reversed(range(df.shape[1])):
        vals = df.iloc[i, (j + 1) : max_ind].tolist()
        if len(vals) == 0:
            vis_array[i, j] = 1
        elif int(df.iloc[i, j]) > max(vals):
            vis_array[i, j] = 1
        else:
            continue

# Check looking top to bottom
for j in range(df.shape[1]):
    for i in range(df.shape[0]):
        vals = df.iloc[min_ind:i, j].tolist()
        if len(vals) == 0:
            vis_array[i, j] = 1
        elif int(df.iloc[i, j]) > max(vals):
            vis_array[i, j] = 1
        else:
            continue

# Check looking bottom to top
for j in range(df.shape[1]):
    for i in reversed(range(df.shape[0])):
        vals = df.iloc[(i + 1) : max_ind, j].tolist()
        if len(vals) == 0:
            vis_array[i, j] = 1
        elif int(df.iloc[i, j]) > max(vals):
            vis_array[i, j] = 1
        else:
            continue

print(sum(sum(vis_array)))

print(time.time() - start)

# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_08_parsed.csv", header=None)


def check_neighbor_direction(df, i, j):
    start_height = df.iloc[i, j]
    # Check north
    n_view = 0
    s_view = 0
    e_view = 0
    w_view = 0
    max_ind = df.shape[0]
    if i == 0 or i == max_ind or j == 0 or j == max_ind:
        return 0
    for mv_n in reversed(range(j)):
        if df.iloc[i, mv_n] < start_height:
            n_view += 1
        else:
            n_view += 1
            break
    for mv_s in range(j + 1, max_ind):
        if df.iloc[i, mv_s] < start_height:
            s_view += 1
        else:
            s_view += 1
            break
    for mv_w in reversed(range(i)):
        if df.iloc[mv_w, j] < start_height:
            w_view += 1
        else:
            w_view += 1
            break
    for mv_e in range(i + 1, max_ind):
        if df.iloc[mv_e, j] < start_height:
            e_view += 1
        else:
            e_view += 1
            break
    return n_view * s_view * w_view * e_view


running_score = 0
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        score = check_neighbor_direction(df, i, j)
        if score > running_score:
            running_score = score

print(running_score)
print(time.time() - start)
