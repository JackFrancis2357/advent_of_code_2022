import sys
import time

import numpy as np
import pandas as pd

# Part 1
# Notes
start = time.time()
df = pd.read_csv("data/input_data_12_03.csv", header=None)
df.columns = ["Rucksack"]
print([ord(char) - 96 for char in "b"])

total = 0
for i in range(df.shape[0]):
    val = df.loc[i, "Rucksack"]
    len_to_use = int(len(val) / 2)
    ruck_1 = val[:len_to_use]
    ruck_2 = val[len_to_use:]
    common_val = [v for v in ruck_1 if v in ruck_2][0]
    if common_val.isupper():
        total += ord(common_val.lower()) - 96 + 26
    else:
        total += ord(common_val.lower()) - 96

print(total)
print(time.time() - start)

# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_03.csv", header=None)
df.columns = ['Rucksack']

total = 0
for i in range(int(df.shape[0] / 3)):
    elf_1 = df.loc[i * 3, 'Rucksack']
    elf_2 = df.loc[i * 3 + 1, 'Rucksack']
    elf_3 = df.loc[i * 3 + 2, 'Rucksack']
    common_val = [v for v in elf_1 if v in elf_2 if v in elf_3][0]
    if common_val.isupper():
        total += ord(common_val.lower()) - 96 + 26
    else:
        total += ord(common_val.lower()) - 96

print(total)
print(time.time() - start)
