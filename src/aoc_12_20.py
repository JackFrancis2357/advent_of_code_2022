import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()
df = pd.read_csv("data/input_data_12_20.csv", header=None)
df_e = pd.read_csv("data/input_data_12_20_example.csv", header=None)

# debug = True
debug = False
if debug:
    curr_df = df_e
else:
    curr_df = df


def get_answers(curr_list):
    zero_index = curr_list.index(0)
    print(zero_index)
    curr_list = [*curr_list[zero_index:], *curr_list[:zero_index]]
    # print(curr_list)
    one_thous_cycle = 1000 % len(curr_list)
    two_thous_cycle = 2000 % len(curr_list)
    three_thous_cycle = 3000 % len(curr_list)
    print(one_thous_cycle, two_thous_cycle, three_thous_cycle)
    one_thous_ans = curr_list[one_thous_cycle]
    two_thous_ans = curr_list[two_thous_cycle]
    three_thous_ans = curr_list[three_thous_cycle]
    print(one_thous_ans, two_thous_ans, three_thous_ans)
    return one_thous_ans + two_thous_ans + three_thous_ans


order_to_move = curr_df.iloc[:, 0].tolist()
curr_list = curr_df.iloc[:, 0].tolist()
curr_len = len(curr_list) - 1
order_list = [*range(curr_len + 1)]

for i in range(curr_len + 1):
    curr_index = order_list.index(i)
    curr_val = curr_list[curr_index]
    mod_val = curr_val % curr_len
    if (curr_index + mod_val) >= curr_len:
        new_position = (curr_index + mod_val) % curr_len
    else:
        new_position = curr_index + mod_val

    curr_list.pop(curr_index)
    order_list.remove(i)
    curr_list = [*curr_list[:new_position], curr_val, *curr_list[new_position:]]
    order_list = [*order_list[:new_position], i, *order_list[new_position:]]
    if debug:
        print(f"Moving {curr_val}")
        print(curr_list)
        print("\n")

print(get_answers(curr_list))

print(time.time() - start)

# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_20.csv", header=None)
df_e = pd.read_csv("data/input_data_12_20_example.csv", header=None)

debug = False
if debug:
    curr_df = df_e
else:
    curr_df = df


order_to_move = curr_df.iloc[:, 0].tolist()
curr_list = curr_df.iloc[:, 0].tolist()
curr_len = len(curr_list) - 1
order_list = [*range(curr_len + 1)]
curr_list = [i * 811589153 for i in curr_list]

for _ in range(10):
    for i in range(curr_len + 1):
        curr_index = order_list.index(i)
        curr_val = curr_list[curr_index]
        mod_val = curr_val % curr_len
        if (curr_index + mod_val) >= curr_len:
            new_position = (curr_index + mod_val) % curr_len
        else:
            new_position = curr_index + mod_val

        curr_list.pop(curr_index)
        order_list.remove(i)
        curr_list = [*curr_list[:new_position], curr_val, *curr_list[new_position:]]
        order_list = [*order_list[:new_position], i, *order_list[new_position:]]
        if debug:
            print(f"Moving {curr_val}")
            print(curr_list)
            print("\n")

print(get_answers(curr_list))


print(time.time() - start)
