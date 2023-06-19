import itertools
import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()


def do_comparison(first, second):
    for elem_f, elem_s in itertools.zip_longest(first, second):
        if elem_f is None:
            return True
        elif elem_s is None:
            return False
        if type(elem_f) == list and type(elem_s) == list:
            return_val = do_comparison(elem_f, elem_s)
            if return_val is not None:
                return return_val
        elif type(elem_f) != list and type(elem_s) == list:
            return_val = do_comparison([elem_f], elem_s)
            if return_val is not None:
                return return_val
        elif type(elem_f) == list and type(elem_s) != list:
            return_val = do_comparison(elem_f, [elem_s])
            if return_val is not None:
                return return_val
        else:
            if elem_f < elem_s:
                return True
            elif elem_f > elem_s:
                return False
    return None


with open("./data/input_data_12_13.csv") as f:
    ctr = 0
    total_ctr = 0
    for line in f.read().splitlines():
        if ctr % 3 == 0:
            first_line = line
            ctr += 1
        elif ctr % 3 == 1:
            second_line = line
            ctr += 1
        elif ctr % 3 == 2:
            ctr += 1
            val = do_comparison(eval(first_line), eval(second_line))
            if val:
                total_ctr += ctr / 3


print(total_ctr)

print(time.time() - start)

# Part 2
start = time.time()

all_lines = []
with open("./data/input_data_12_13.csv") as f:
    ctr = 0
    total_ctr = 0
    for line in f.read().splitlines():
        if ctr % 3 == 0:
            first_line = line
            all_lines.append(line)
            ctr += 1
        elif ctr % 3 == 1:
            second_line = line
            all_lines.append(line)
            ctr += 1
        elif ctr % 3 == 2:
            ctr += 1

all_lines.append("[[2]]")
all_lines.append("[[6]]")

sorted_list = False
while not sorted_list:
    sorted_list = True
    for i in range(len(all_lines) - 1):
        if not do_comparison(eval(all_lines[i]), eval(all_lines[i + 1])):
            all_lines[i], all_lines[i + 1] = all_lines[i + 1], all_lines[i]
            sorted_list = False


print(all_lines.index("[[2]]") + 1, all_lines.index("[[6]]") + 1)
print((all_lines.index("[[2]]") + 1) * (all_lines.index("[[6]]") + 1))
print(time.time() - start)
