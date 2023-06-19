import random
import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()

debug = False
base_filename = "./data/input_data_12_19"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line)


def parse_blueprint(line):
    blueprint = {}
    vals = line.split(".")
    blueprint["ore"] = int(vals[0].split(" ")[-2])
    blueprint["clay"] = int(vals[1].split(" ")[-2])
    blueprint["obsidian"] = [int(vals[2].split(" ")[-5]), int(vals[2].split(" ")[-2])]
    blueprint["geode"] = [int(vals[3].split(" ")[-5]), int(vals[3].split(" ")[-2])]
    return blueprint


def run_simulation(blueprint, num_min):
    robots_list = ["ore"]
    material_dict = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
    for minute in range(num_min):
        new_robot_list = []
        if material_dict["ore"] >= blueprint["geode"][0] and material_dict["obsidian"] >= blueprint["geode"][1]:
            material_dict["ore"] -= blueprint["geode"][0]
            material_dict["obsidian"] -= blueprint["geode"][1]
            new_robot_list.append("geode")
        elif (
            material_dict["ore"] >= blueprint["obsidian"][0]
            and material_dict["clay"] >= blueprint["obsidian"][1]
            and random.random() > 0.25
            and len(new_robot_list) == 0
        ):
            material_dict["ore"] -= blueprint["obsidian"][0]
            material_dict["clay"] -= blueprint["obsidian"][1]
            new_robot_list.append("obsidian")
        elif material_dict["ore"] >= blueprint["clay"] and random.random() > 0.6 and len(new_robot_list) == 0:
            material_dict["ore"] -= blueprint["clay"]
            new_robot_list.append("clay")
        elif material_dict["ore"] >= blueprint["ore"] and random.random() > 0.7 and len(new_robot_list) == 0:
            material_dict["ore"] -= blueprint["ore"]
            new_robot_list.append("ore")
        for material in robots_list:
            material_dict[material] += 1
        if len(new_robot_list) > 0:
            for new_robot in new_robot_list:
                robots_list.append(new_robot)

    return material_dict


ttl = 0
for i, line in enumerate(all_lines):
    blueprint = parse_blueprint(line)
    max_geodes = 0
    for _ in range(10):
        mat_dict = run_simulation(blueprint, num_min=24)
        if mat_dict["geode"] > max_geodes:
            max_geodes = mat_dict["geode"]
    ttl += (i + 1) * max_geodes
#     print(max_geodes)
# print(ttl)

print(time.time() - start)

# Part 2
start = time.time()

debug = False
base_filename = "./data/input_data_12_19"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line)

all_lines = all_lines[:3]

ttl = 1
for i, line in enumerate(all_lines):
    blueprint = parse_blueprint(line)
    max_geodes = 0
    for _ in range(1000000):
        mat_dict = run_simulation(blueprint, num_min=32)
        if mat_dict["geode"] > max_geodes:
            max_geodes = mat_dict["geode"]
    ttl *= max_geodes
    print(max_geodes)
print(ttl)


print(time.time() - start)
