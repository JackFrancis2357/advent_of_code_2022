import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()
df = pd.read_csv("data/input_data_12_05.csv", header=None)

starting_configuration = {
    "1": "RNPG",
    "2": "TJBLCSVH",
    "3": "TDBMNL",
    "4": "RVPSB",
    "5": "GCQSWMVH",
    "6": "WQSCDBJ",
    "7": "FQL",
    "8": "WMHTDLFV",
    "9": "LPBVMJF",
}


def update_configuration(conf, amt, orig, dest):
    orig_stack = conf[orig]
    dest_stack = conf[dest]
    for _ in range(int(amt)):
        val = orig_stack[-1]
        orig_stack = orig_stack[:-1]
        dest_stack += val
    conf[orig] = orig_stack
    conf[dest] = dest_stack
    return conf


current_configuration = starting_configuration

for i in range(df.shape[0]):
    sample_str = df.iloc[i, 0].split(" ")
    amount, origin, destination = sample_str[1], sample_str[3], sample_str[5]
    current_configuration = update_configuration(current_configuration, amount, origin, destination)
for i in range(1, 10):
    print(current_configuration[str(i)][-1], end="")
print('\n')
print(time.time() - start)

# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_05.csv", header=None)

starting_configuration = {
    "1": "RNPG",
    "2": "TJBLCSVH",
    "3": "TDBMNL",
    "4": "RVPSB",
    "5": "GCQSWMVH",
    "6": "WQSCDBJ",
    "7": "FQL",
    "8": "WMHTDLFV",
    "9": "LPBVMJF",
}


def update_configuration_2(conf, amt, orig, dest):
    orig_stack = conf[orig]
    dest_stack = conf[dest]
    val = orig_stack[-int(amt):]
    orig_stack = orig_stack[:-int(amt)]
    dest_stack += val
    conf[orig] = orig_stack
    conf[dest] = dest_stack
    return conf


current_configuration = starting_configuration

for i in range(df.shape[0]):
    sample_str = df.iloc[i, 0].split(" ")
    amount, origin, destination = sample_str[1], sample_str[3], sample_str[5]
    current_configuration = update_configuration_2(current_configuration, amount, origin, destination)
for i in range(1, 10):
    print(current_configuration[str(i)][-1], end="")
print('\n')
print(time.time() - start)
