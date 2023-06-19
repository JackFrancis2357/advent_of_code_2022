import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()
df = pd.read_csv("data/input_data_12_06.csv", header=None)

sample_string = df.iloc[0, 0]
for i in range(len(sample_string)):
    sub_seq = sample_string[i : i + 4]
    if len(set(sub_seq)) == len(sub_seq):
        print(i + 4)
        break

print(time.time() - start)

# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_06.csv", header=None)

sample_string = df.iloc[0, 0]
for i in range(len(sample_string)):
    sub_seq = sample_string[i : i + 14]
    if len(set(sub_seq)) == len(sub_seq):
        print(i + 14)
        break

print(time.time() - start)
