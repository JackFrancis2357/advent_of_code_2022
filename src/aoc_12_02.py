import time

import numpy as np
import pandas as pd

# Part 1
# Notes
# A, B, C = Rock, Paper Scissor
# X, Y, Z = Rock, Paper, Scissor
start = time.time()
part_1_outcome_dict = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

df = pd.read_csv("data/input_data_12_02.csv", header=None)
total_score = 0
for i in range(df.shape[0]):
    total_score += part_1_outcome_dict[df.iloc[i, 0]]

print(total_score)
print(time.time() - start)

# Part 2
# A, B, C = Rock, Paper Scissor
# X, Y, Z = Rock, Paper, Scissor
start = time.time()
part_2_outcome_dict = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}

df = pd.read_csv("data/input_data_12_02.csv", header=None)
total_score = 0
for i in range(df.shape[0]):
    total_score += part_2_outcome_dict[df.iloc[i, 0]]

print(total_score)
print(time.time() - start)