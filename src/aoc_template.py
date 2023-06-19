import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()
df = pd.read_csv("data/input_data_12_XX.csv", header=None)
df_e = pd.read_csv('data/input_data_12_XX_example.csv', header=None)

debug = True
base_filename = "./data/input_data_12_XX"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line)

print(time.time() - start)

# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_XX.csv", header=None)
df_e = pd.read_csv('data/input_data_12_XX_example.csv', header=None)

debug = True
base_filename = "./data/input_data_12_XX"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line)


print(time.time() - start)
