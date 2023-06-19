import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()
df = pd.read_csv("data/input_data_12_12.csv", header=None)
df_e = pd.read_csv("data/input_data_12_12_example.csv", header=None)

curr_df = df

test_array = np.empty((curr_df.shape[0], len(curr_df.iloc[0, 0])))

for i in range(curr_df.shape[0]):
    for j, char in enumerate(curr_df.iloc[i, 0]):
        if char == "S":
            starting_index = (i, j)
            test_array[i, j] = 1
        elif char == "E":
            ending_index = (i, j)
            test_array[i, j] = 26
        else:
            test_array[i, j] = ord(char) - 96

print(test_array, starting_index, ending_index)


def get_possible_states(curr_loc, visited_states_list, test_array):
    new_possible_states = []
    curr_state_x = curr_loc[0]
    curr_state_y = curr_loc[1]
    visited_states_list.append(curr_loc)
    neighbors = [
        (curr_state_x + 1, curr_state_y),
        (curr_state_x - 1, curr_state_y),
        (curr_state_x, curr_state_y + 1),
        (curr_state_x, curr_state_y - 1),
    ]
    for neighbor in neighbors:
        if (
            neighbor[0] < 0
            or neighbor[1] < 0
            or neighbor[0] > (test_array.shape[0] - 1)
            or neighbor[1] > (test_array.shape[1] - 1)
            or neighbor in visited_states_list
        ):
            continue
        else:
            if test_array[neighbor] - test_array[curr_loc] <= 1:
                new_possible_states.append(neighbor)
    return new_possible_states, visited_states_list


end_state_found = False
visited_states_list = []
curr_locations = [starting_index]
val = 0
while end_state_found is False:
    next_possible_states = []
    for curr_loc in curr_locations:
        nps, visited_states_list = get_possible_states(curr_loc, visited_states_list, test_array)
        next_possible_states.append(nps)
    next_possible_states = list(set([item for sublist in next_possible_states for item in sublist]))
    visited_states_list = list(set(visited_states_list))
    curr_locations = next_possible_states
    if ending_index in curr_locations:
        path_length = val + 1
        print(path_length)
        end_state_found = True
    val += 1

print(time.time() - start)

# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_12.csv", header=None)
df_e = pd.read_csv("data/input_data_12_12_example.csv", header=None)

curr_df = df

test_array = np.empty((curr_df.shape[0], len(curr_df.iloc[0, 0])))

starting_index_list = []
for i in range(curr_df.shape[0]):
    for j, char in enumerate(curr_df.iloc[i, 0]):
        if char == "S" or char == "a":
            starting_index_list.append((i, j))
            test_array[i, j] = 1
        elif char == "E":
            ending_index = (i, j)
            test_array[i, j] = 26
        else:
            test_array[i, j] = ord(char) - 96

print(test_array, starting_index, ending_index)


min_path = 100000
for starting_index in starting_index_list:
    end_state_found = False
    visited_states_list = []
    curr_locations = [starting_index]
    val = 0
    while end_state_found is False:
        next_possible_states = []
        for curr_loc in curr_locations:
            nps, visited_states_list = get_possible_states(curr_loc, visited_states_list, test_array)
            next_possible_states.append(nps)
        next_possible_states = list(set([item for sublist in next_possible_states for item in sublist]))
        visited_states_list = list(set(visited_states_list))
        curr_locations = next_possible_states
        if len(curr_locations) == 0:
            end_state_found = True
        if ending_index in curr_locations:
            path_length = val + 1
            print(path_length)
            end_state_found = True
        val += 1
    if path_length < min_path:
        min_path = path_length

print(min_path)
print(time.time() - start)
