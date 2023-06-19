import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()
df = pd.read_csv("data/input_data_12_24.csv", header=None)
df_e = pd.read_csv("data/input_data_12_24_example.csv", header=None)

debug = True
if debug:
    curr_df = df_e
else:
    curr_df = df


def blizzard_exist(symbol):
    if symbol == ".":
        return False, None
    elif symbol == ">":
        return True, np.array([0, 1])
    elif symbol == "<":
        return True, np.array([0, -1])
    elif symbol == "^":
        return True, np.array([-1, 0])
    elif symbol == "v":
        return True, np.array([1, 0])


def initialize_blizzard_dict(curr_df):
    blizzard_dict = {}
    b_ctr = 0
    for i in range(1, curr_df.shape[0] - 1):
        curr_x = i - 1
        for curr_y, j in enumerate(curr_df.iloc[i, 0][1:-1]):
            blizz_exist, update_val = blizzard_exist(j)
            if blizz_exist:
                blizzard_dict[f"b_{b_ctr}"] = {
                    "curr_pos": np.array([curr_x, curr_y]),
                    "update_val": update_val,
                    "symbol": j,
                }
                b_ctr += 1
            print(j, end="")
        print("\n")
    return blizzard_dict


def print_board(blizzard_dict):
    board = [["." for y in range(max_y)] for x in range(max_x)]
    for k, v in blizzard_dict.items():
        blizz_x, blizz_y = blizzard_dict[k]["curr_pos"]
        blizz_symbol = blizzard_dict[k]["symbol"]
        board[blizz_x][blizz_y] = blizz_symbol
    for i, vals in enumerate(board):
        for j in vals:
            print(j, end="")
        print("\n")


def blizzard_update_step(blizzard_dict, max_x, max_y):
    for k, v in blizzard_dict.items():
        blizzard_dict[k]["curr_pos"] += blizzard_dict[k]["update_val"]
        blizzard_dict[k]["curr_pos"][0] = blizzard_dict[k]["curr_pos"][0] % max_x
        blizzard_dict[k]["curr_pos"][1] = blizzard_dict[k]["curr_pos"][1] % max_y
    return blizzard_dict


def get_safe_spots(blizzard_dict, max_x, max_y):
    safe_places = np.ones((max_x, max_y))
    for k, v in blizzard_dict.items():
        safe_places[blizzard_dict[k]["curr_pos"][0], blizzard_dict[k]["curr_pos"][1]] = 0
    return safe_places


def get_next_states(x, y, safe_spot, max_x, max_y):
    safe_spot_list = []
    if safe_spot[x][y] == 1:
        safe_spot_list.append([x, y])
    if x + 1 < max_x:
        if safe_spot[x + 1][y] == 1:
            safe_spot_list.append([x + 1, y])
    if x >= 1:
        if safe_spot[x - 1][y] == 1:
            safe_spot_list.append([x - 1, y])
    if y + 1 < max_y:
        if safe_spot[x][y + 1] == 1:
            safe_spot_list.append([x, y + 1])
    if y >= 1:
        if safe_spot[x][y - 1] == 1:
            safe_spot_list.append([x, y - 1])
    return safe_spot_list


blizzard_dict = initialize_blizzard_dict(curr_df)
max_x = curr_df.shape[0] - 2
max_y = len(curr_df.iloc[0, 0]) - 2
print(max_x, max_y)
safe_spots = []
for _ in range(300):
    blizzard_dict = blizzard_update_step(blizzard_dict, max_x, max_y)
    safe_spots.append(get_safe_spots(blizzard_dict, max_x, max_y))


current_list = [[0, 0]]
for round, safe_spot in enumerate(safe_spots):
    if round == 0:
        continue
    new_list = []
    for coord in current_list:
        new_vals = get_next_states(coord[0], coord[1], safe_spot, max_x, max_y)
        for val in new_vals:
            if val == [max_x - 1, max_y - 1]:
                # print(round)
                pass
            new_list.append(val)
    current_list = []
    intermed_list = new_list
    for elem in intermed_list:
        if elem not in current_list:
            current_list.append(elem)


print(time.time() - start)


# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_24.csv", header=None)
df_e = pd.read_csv("data/input_data_12_24_example.csv", header=None)

debug = False
if debug:
    curr_df = df_e
else:
    curr_df = df


def get_next_states_pt2(x, y, safe_spot, max_x, max_y, start=False):
    safe_spot_list = []
    if start:
        if x == 0 and y == 0:
            return [[-1, 0]]
    else:
        if x == (max_x - 1) and y == (max_y - 1):
            return [[max_x, max_y - 1]]
    if safe_spot[x][y] == 1:
        safe_spot_list.append([x, y])
    if x + 1 < max_x:
        if safe_spot[x + 1][y] == 1:
            safe_spot_list.append([x + 1, y])
    if x >= 1:
        if safe_spot[x - 1][y] == 1:
            safe_spot_list.append([x - 1, y])
    if y + 1 < max_y:
        if safe_spot[x][y + 1] == 1:
            safe_spot_list.append([x, y + 1])
    if y >= 1:
        if safe_spot[x][y - 1] == 1:
            safe_spot_list.append([x, y - 1])
    return safe_spot_list


def move_off_start(safe_spot):
    if safe_spot[0][0] == 1:
        return [[0, 0]], False
    else:
        return [[-1, 0]], True


def move_off_finish(safe_spot):
    if safe_spot[max_x - 1][max_y - 1] == 1:
        return [[max_x - 1, max_y - 1]], False
    else:
        return [[max_x, max_y - 1]], True


def traveling_func(starting_round, starting_list, destination, safe_spots, start=False):
    current_list = starting_list
    for round, safe_spot in enumerate(safe_spots):
        if round == starting_round and not start:
            current_list, possible_move = move_off_start(safe_spots[round + 1])
            starting_round += possible_move
            continue
        elif round == starting_round and start:
            current_list, possible_move = move_off_finish(safe_spots[round + 1])
            starting_round += possible_move
            continue
        elif round < starting_round:
            continue
        new_list = []
        for coord in current_list:
            new_vals = get_next_states_pt2(coord[0], coord[1], safe_spots[round + 1], max_x, max_y, start)
            for val in new_vals:
                if val == destination:
                    return round + 1
                new_list.append(val)
        current_list = []
        intermed_list = new_list
        for elem in intermed_list:
            if elem not in current_list:
                current_list.append(elem)
        if len(current_list) == 0:
            starting_round = round + 1
            current_list = starting_list


blizzard_dict = initialize_blizzard_dict(curr_df)
max_x = curr_df.shape[0] - 2
max_y = len(curr_df.iloc[0, 0]) - 2
print(max_x, max_y)
safe_spots = []
safe_spots.append(get_safe_spots(blizzard_dict, max_x, max_y))
for _ in range(1000):
    blizzard_dict = blizzard_update_step(blizzard_dict, max_x, max_y)
    safe_spots.append(get_safe_spots(blizzard_dict, max_x, max_y))

trip_1 = traveling_func(0, [[-1, 0]], [max_x, max_y - 1], safe_spots)
print(trip_1)
trip_2 = traveling_func(trip_1, [[max_x, max_y - 1]], [-1, 0], safe_spots, start=True)
print(trip_2)
trip_3 = traveling_func(trip_2, [[-1, 0]], [max_x, max_y - 1], safe_spots)
print(trip_3)

print(time.time() - start)
