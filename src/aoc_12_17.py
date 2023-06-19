import itertools
import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()


def jet_flow_move(move, cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y, rock_type):
    curr_box = cavern_array[min_curr_x:max_curr_x, min_curr_y:max_curr_y]
    # cavern_array[ca_size - min_curr_x : ca_size - max_curr_x, min_curr_y:max_curr_y] = 0
    if move == ">":
        if not max_curr_y + 1 > 7:
            test_box = cavern_array[min_curr_x:max_curr_x, min_curr_y + 1 : max_curr_y + 1]
            test_sum = rock_type + test_box
            if np.max(test_sum) == 10:
                return cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y
            else:
                inv_rock_type = np.multiply(rock_type, -1)
                cavern_array[min_curr_x:max_curr_x, min_curr_y:max_curr_y] = curr_box + inv_rock_type
                save_nines = cavern_array[min_curr_x:max_curr_x, min_curr_y + 1 : max_curr_y + 1]
                save_nines[save_nines < 9] = 0
                cavern_array[min_curr_x:max_curr_x, min_curr_y + 1 : max_curr_y + 1] = rock_type + save_nines
                min_curr_y += 1
                max_curr_y += 1
        return cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y
    else:
        if not min_curr_y - 1 < 0:
            test_box = cavern_array[min_curr_x:max_curr_x, min_curr_y - 1 : max_curr_y - 1]
            test_sum = rock_type + test_box
            if np.max(test_sum) == 10:
                return cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y
            else:
                inv_rock_type = np.multiply(rock_type, -1)
                cavern_array[min_curr_x:max_curr_x, min_curr_y:max_curr_y] = curr_box + inv_rock_type
                save_nines = cavern_array[min_curr_x:max_curr_x, min_curr_y - 1 : max_curr_y - 1]
                save_nines[save_nines < 9] = 0
                cavern_array[min_curr_x:max_curr_x, min_curr_y - 1 : max_curr_y - 1] = rock_type + save_nines
                min_curr_y -= 1
                max_curr_y -= 1
        return cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y


def downward_move(cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y, rock_type):
    if min_curr_x - 1 < 0:
        cavern_array[cavern_array == 1] = 9
        finished = True
        return cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y, finished
    # cavern_array[min_curr_x:max_curr_x, min_curr_y:max_curr_y] = 0
    curr_box = cavern_array[min_curr_x:max_curr_x, min_curr_y:max_curr_y]
    test_box = cavern_array[min_curr_x - 1 : max_curr_x - 1, min_curr_y:max_curr_y]
    test_sum = rock_type + test_box
    if np.max(test_sum) == 10:
        finished = True
        cavern_array[cavern_array == 1] = 9
        return cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y, finished
    else:
        inv_rock_type = np.multiply(rock_type, -1)
        cavern_array[min_curr_x:max_curr_x, min_curr_y:max_curr_y] = curr_box + inv_rock_type
        save_nines = cavern_array[min_curr_x - 1 : max_curr_x - 1, min_curr_y:max_curr_y]
        save_nines[save_nines < 9] = 0
        cavern_array[min_curr_x - 1 : max_curr_x - 1, min_curr_y:max_curr_y] = rock_type + save_nines
        min_curr_x -= 1
        max_curr_x -= 1
        finished = False
        return cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y, finished


def get_curr_height(cavern_array):
    if np.sum(cavern_array) == 0:
        return 0
    else:
        for r in range(cavern_array.shape[0]):
            if np.sum(cavern_array[r, :]) == 0:
                return r


reverse_rock_types = {
    "horizontal": np.array([[1, 1, 1, 1]]),
    "cross": np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
    "l-shape": np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]]),
    "straight": np.array([[1], [1], [1], [1]]),
    "box": np.array([[1, 1], [1, 1]]),
}

df = pd.read_csv("data/input_data_12_17.csv", header=None)
df_e = pd.read_csv("data/input_data_12_17_example.csv", header=None)

curr_df = df

cavern_array = np.zeros([4000, 7])
piece_list = ["horizontal", "cross", "l-shape", "straight", "box"]
moves_list = [i for i in curr_df.iloc[0, 0]]
repeating_piece_gen = itertools.cycle(piece_list)
repeating_move_gen = itertools.cycle(moves_list)

for i in range(20):
    curr_height = get_curr_height(cavern_array)
    piece = next(repeating_piece_gen)
    min_curr_x = curr_height + 3
    max_curr_x = curr_height + 3 + reverse_rock_types[piece].shape[0]
    min_curr_y = 2
    max_curr_y = 2 + reverse_rock_types[piece].shape[1]
    finished = False

    cavern_array[min_curr_x:max_curr_x, min_curr_y:max_curr_y] = reverse_rock_types[piece]
    while not finished:
        move = next(repeating_move_gen)
        cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y = jet_flow_move(
            move, cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y, reverse_rock_types[piece]
        )
        cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y, finished = downward_move(
            cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y, reverse_rock_types[piece]
        )
print(get_curr_height(cavern_array))


print(time.time() - start)

# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_17.csv", header=None)
df_e = pd.read_csv("data/input_data_12_17_example.csv", header=None)

curr_df = df

reverse_rock_types = {
    "horizontal": np.array([[1, 1, 1, 1]]),
    "cross": np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
    "l-shape": np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]]),
    "straight": np.array([[1], [1], [1], [1]]),
    "box": np.array([[1, 1], [1, 1]]),
}

df = pd.read_csv("data/input_data_12_17.csv", header=None)
df_e = pd.read_csv("data/input_data_12_17_example.csv", header=None)

debug = False
if debug:
    curr_df = df_e
    cycle_start = 123
    cycle_len = 35
    cycle_height = 53
else:
    curr_df = df
    cycle_start = 170
    cycle_len = 1720
    cycle_height = 2702


cavern_array = np.zeros([1600, 7])
piece_list = ["horizontal", "cross", "l-shape", "straight", "box"]
moves_list = [i for i in curr_df.iloc[0, 0]]
repeating_piece_gen = itertools.cycle(piece_list)
repeating_move_gen = itertools.cycle(moves_list)

target_blocks = 1_000_000_000_000
target_blocks -= cycle_start
repeats = np.floor(target_blocks / cycle_len)
additional_blocks = target_blocks - (repeats * cycle_len)

blocks_to_check = cycle_start + cycle_len + additional_blocks

for i in range(int(blocks_to_check)):
    curr_height = get_curr_height(cavern_array)
    if i == cycle_start:
        cycle_start_height = curr_height
    if i == (cycle_start + cycle_len):
        cycle_len_height = curr_height - cycle_start_height
    # if i > cycle_start and curr_height - cycle_start_height == 2702:
    #     print(i)
    #     sys.exit()
    piece = next(repeating_piece_gen)
    min_curr_x = curr_height + 3
    max_curr_x = curr_height + 3 + reverse_rock_types[piece].shape[0]
    min_curr_y = 2
    max_curr_y = 2 + reverse_rock_types[piece].shape[1]
    finished = False

    cavern_array[min_curr_x:max_curr_x, min_curr_y:max_curr_y] = reverse_rock_types[piece]
    while not finished:
        move = next(repeating_move_gen)
        cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y = jet_flow_move(
            move, cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y, reverse_rock_types[piece]
        )
        cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y, finished = downward_move(
            cavern_array, min_curr_x, max_curr_x, min_curr_y, max_curr_y, reverse_rock_types[piece]
        )

    if (i + 1) % 1000 == 0:
        print(i, curr_height)
        new_rows = cavern_array.shape[0] + 1700
        new_cols = cavern_array.shape[1]
        cavern_array.resize((new_rows, new_cols), refcheck=False)
# print(np.flipud(cavern_array))
additional_block_height = get_curr_height(cavern_array) - cycle_len_height - cycle_start_height

print(cycle_start_height, cycle_len_height, additional_block_height)
print(cycle_start_height + (repeats * cycle_len_height) + additional_block_height)
# np.save('aoc_12_17_ca.npy', cavern_array)

print(time.time() - start)
