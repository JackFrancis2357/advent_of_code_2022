import sys
import time

import numpy as np
import pandas as pd


# Part 1
# Notes
def check_full_overlap(p1, p2):
    p1_l, p1_h = map(int, p1.split("-"))
    p2_l, p2_h = map(int, p2.split("-"))

    if p1_l <= p2_l and p1_h >= p2_h:
        return 1
    elif p2_l <= p1_l and p2_h >= p1_h:
        return 1
    else:
        return 0


def check_partial_overlap(p1, p2):
    p1_l, p1_h = map(int, p1.split("-"))
    p2_l, p2_h = map(int, p2.split("-"))

    p1_range = [*range(p1_l, p1_h + 1)]
    p2_range = [*range(p2_l, p2_h + 1)]
    if len(set(p1_range).intersection(p2_range)) > 0:
        return 1
    else:
        return 0


# Part 1
start = time.time()
df = pd.read_csv("data/input_data_12_04.csv", header=None)

ttl = 0
for i in range(df.shape[0]):
    ttl += check_full_overlap(df.iloc[i, 0], df.iloc[i, 1])

print(ttl)
print(time.time() - start)

# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_04.csv", header=None)

# Part 1
ttl = 0
for i in range(df.shape[0]):
    ttl += check_partial_overlap(df.iloc[i, 0], df.iloc[i, 1])

print(ttl)
print(time.time() - start)
