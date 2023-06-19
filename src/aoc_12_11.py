import math
import sys
import time

import numpy as np
import pandas as pd

from aoc_12_11_example import get_example_dict_counts, mky_opers_example, mky_opers_example_pt2
from aoc_12_11_input import get_input_dict_counts, mky_opers, mky_opers_pt2

# Part 1
start = time.time()


def get_maxes(mky_dict, mky_count, num_rounds, mky_func):
    for _ in range(num_rounds):
        for k, v in mky_dict.items():
            for i in v:
                mky_dict = mky_func(k, i, mky_dict)
                mky_count[k] += 1
            mky_dict[k] = []

    max_1, max_2 = 0, 0

    for k, v in mky_count.items():
        if v > max_1:
            max_2 = max_1
            max_1 = v
        elif v > max_2:
            max_2 = v

    return max_1, max_2


monkey_dict_example, monkey_counts_example = get_example_dict_counts()
monkey_dict_input, monkey_counts_input = get_input_dict_counts()


ex_m1, ex_m2 = get_maxes(monkey_dict_example, monkey_counts_example, 20, mky_opers_example)
in_m1, in_m2 = get_maxes(monkey_dict_input, monkey_counts_input, 20, mky_opers)

print(ex_m1, ex_m2, ex_m1 * ex_m2)
print(in_m1, in_m2, in_m1 * in_m2)

print(time.time() - start)

# Part 2
start = time.time()

monkey_dict_example, monkey_counts_example = get_example_dict_counts()
monkey_dict_input, monkey_counts_input = get_input_dict_counts()

ex_m1_p2, ex_m2_p2 = get_maxes(monkey_dict_example, monkey_counts_example, 10000, mky_opers_example_pt2)
in_m1_p2, in_m2_p2 = get_maxes(monkey_dict_input, monkey_counts_input, 10000, mky_opers_pt2)

print(ex_m1_p2, ex_m2_p2, ex_m1_p2 * ex_m2_p2)
print(in_m1_p2, in_m2_p2, in_m1_p2 * in_m2_p2)

print(time.time() - start)
