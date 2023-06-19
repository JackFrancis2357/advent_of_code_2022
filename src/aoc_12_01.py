import time

import numpy as np
import pandas as pd

df = pd.read_csv("./data/input_data_12_01.csv", header=None, skip_blank_lines=False)

start = time.time()
max_elf = 0
curr_elf = 0
all_elves = []
for i in range(df.shape[0]):
    if np.isnan(df.iloc[i, 0]):
        all_elves.append(curr_elf)
        if curr_elf > max_elf:
            max_elf = curr_elf
        curr_elf = 0
    else:
        curr_elf += df.iloc[i, 0]

# Part 1
print(max_elf)

# Part 2
top_elves = sorted(all_elves, reverse=True)
print(top_elves[0] + top_elves[1] + top_elves[2])
print(time.time() - start)
