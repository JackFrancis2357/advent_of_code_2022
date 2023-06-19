import random
import sys
import time

import networkx as nx
import numpy as np
import pandas as pd

# Part 1
start = time.time()


def calc_best_node(curr_node, node_dict, path_lengths, time_remaining, curr_total):
    node_val = {}
    for k, v in node_dict.items():
        if k == curr_node:
            continue
        dist = len(path_lengths[curr_node][k]) - 1
        node_val[k] = (time_remaining - dist - 1) * v
    # next_node = max(node_val, key=node_val.get)
    try:
        next_node = random.choices(list(node_val.keys()), weights=node_val.values(), k=1)[0]
    except ValueError:
        return None, None, None, curr_total
    for i in path_lengths[curr_node][next_node]:
        if i == curr_node:
            continue
        elif i != next_node:
            time_remaining -= 1
            if time_remaining <= 0:
                return None, None, None, curr_total
            if node_dict[i] > 0 and (random.random() < (node_dict[i] / max(node_dict.values()))):
                time_remaining -= 1
                if time_remaining <= 0:
                    return None, None, None, curr_total
                # print(f"Opened valve {i} at time {time_remaining} for {node_dict[i] * time_remaining}")
                curr_total += node_dict[i] * time_remaining
                node_dict[i] = 0
        else:
            time_remaining -= 2
            if time_remaining <= 0:
                return None, None, None, curr_total
            # print(f"Opened valve {i} at time {time_remaining} for {node_dict[i] * time_remaining}")
            curr_total += node_dict[i] * time_remaining
            node_dict[next_node] = 0
    return next_node, node_dict, time_remaining, curr_total


debug = False
base_filename = "./data/input_data_12_16"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line)


nodes_dict = {}
G = nx.Graph()
for line in all_lines:
    G.add_node(line[6:8])
    nodes_dict[line[6:8]] = int(line.split("=")[1].split(";")[0])

for line in all_lines:
    ref_node = line[6:8]
    valves = line.split(",")
    for valve in valves:
        G.add_edge(ref_node, valve[-2:])

path_lengths = dict(nx.all_pairs_shortest_path(G))

curr_max = 0
for _ in range(1000):
    time_rem = 30
    next_node = "AA"
    curr_ttl = 0
    nd = nodes_dict.copy()
    pl = path_lengths.copy()
    while time_rem is not None:
        next_node, nd, time_rem, curr_ttl = calc_best_node(next_node, nd, pl, time_rem, curr_ttl)
    if curr_ttl > curr_max:
        curr_max = curr_ttl

print(curr_max)
print(time.time() - start)

# Part 2
start = time.time()


def get_dest_node(player, node_dict, path_lengths, time_remaining, other_player):
    node_val = {}
    for k, v in node_dict.items():
        if k == player["curr_node"]:
            continue
        elif k == other_player["dest_node"]:
            continue
        dist = len(path_lengths[player["curr_node"]][k]) - 1
        node_val[k] = (time_remaining - dist - 1) * v
    try:
        dest_node = random.choices(list(node_val.keys()), weights=node_val.values(), k=1)[0]
    except ValueError:
        dest_node = "AA"
    player["dest_node"] = dest_node
    player["path_to_dest"] = path_lengths[player["curr_node"]][player["dest_node"]]
    return player


def process_timestep(player, node_dict, path_lengths, curr_total, time_remaining, other_player):
    if player["curr_node"] == player["dest_node"]:
        curr_total += node_dict[player["curr_node"]] * time_remaining
        # print(f"{player['name']} Opened {player['curr_node']} time {time_remaining} for {node_dict[player['curr_node']] * time_remaining}")
        node_dict[player["curr_node"]] = 0

        player = get_dest_node(player, node_dict, path_lengths, time_remaining, other_player)
        return player, node_dict, path_lengths, curr_total
    elif node_dict[player["curr_node"]] > 0 and (
        random.random() < (node_dict[player["curr_node"]] / max(node_dict.values()))
    ):
        curr_total += node_dict[player["curr_node"]] * time_remaining
        # print(f"{player['name']} Opened {player['curr_node']} time {time_remaining} for {node_dict[player['curr_node']] * time_remaining}")
        node_dict[player["curr_node"]] = 0

        return player, node_dict, path_lengths, curr_total
    else:
        player["path_to_dest"] = player["path_to_dest"][1:]
        player["curr_node"] = player["path_to_dest"][0]
        return player, node_dict, path_lengths, curr_total
    pass


debug = False
base_filename = "./data/input_data_12_16"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line)

nodes_dict = {}
G = nx.Graph()
for line in all_lines:
    G.add_node(line[6:8])
    nodes_dict[line[6:8]] = int(line.split("=")[1].split(";")[0])

for line in all_lines:
    ref_node = line[6:8]
    valves = line.split(",")
    for valve in valves:
        G.add_edge(ref_node, valve[-2:])

path_lengths = dict(nx.all_pairs_shortest_path(G))

curr_max = 0
for _ in range(10000):
    player_1 = {"curr_node": "AA", "dest_node": "N/A", "name": "player_1"}
    player_2 = {"curr_node": "AA", "dest_node": "N/A", "name": "player_2"}
    player_1 = get_dest_node(player_1, nodes_dict, path_lengths, 26, player_2)
    player_2 = get_dest_node(player_2, nodes_dict, path_lengths, 26, player_1)
    curr_ttl = 0
    nd = nodes_dict.copy()
    pl = path_lengths.copy()
    for time_rem in reversed(range(26)):
        player_1, nd, pl, curr_ttl = process_timestep(player_1, nd, pl, curr_ttl, time_rem, player_2)
        player_2, nd, pl, curr_ttl = process_timestep(player_2, nd, pl, curr_ttl, time_rem, player_1)
        if curr_ttl > curr_max:
            curr_max = curr_ttl

print(curr_max)
print(time.time() - start)
