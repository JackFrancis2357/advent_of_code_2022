import itertools
import sys
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shapely.geometry import Point, Polygon
from shapely.ops import unary_union

# Part 1
start = time.time()


def parse_sb_pair(sb_pair):
    vals = sb_pair.split(",")
    sensor_x = int(vals[0].split("=")[-1])
    sensor_y = int(vals[1].split(":")[0].split("=")[-1])
    beacon_x = int(vals[1].split("=")[-1])
    beacon_y = int(vals[2].split("=")[-1])
    return sensor_x, sensor_y, beacon_x, beacon_y


def get_impossible_beacon_vals(sensor_x, sensor_y, beacon_x, beacon_y):
    man_dist_sb = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    min_x = sensor_x - man_dist_sb
    max_x = sensor_x + man_dist_sb
    min_y = sensor_y - man_dist_sb
    max_y = sensor_y + man_dist_sb

    x_list = [*range(min_x, max_x + 1)]
    y_list = [*range(min_y, max_y + 1)]
    # y_list = [10]
    combinations = [p for p in itertools.product(x_list, y_list)]
    impossible_values = []
    for comb in combinations:
        if abs(sensor_x - comb[0]) + abs(sensor_y - comb[1]) <= man_dist_sb:
            impossible_values.append(comb)
    return impossible_values


debug = True
base_filename = "./data/input_data_12_15"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line)

print(all_lines, "\n")
total_imp_vals = []
first = True
for sb_pair in all_lines:
    sensor_x, sensor_y, beacon_x, beacon_y = parse_sb_pair(sb_pair)
    imp_vals = get_impossible_beacon_vals(sensor_x, sensor_y, beacon_x, beacon_y)
    total_imp_vals.append(imp_vals)

total_imp_vals = list(set([item for sublist in total_imp_vals for item in sublist]))

print(len(total_imp_vals))
print(time.time() - start)

# Part 2
start = time.time()


def get_impossible_beacon_borders(sensor_x, sensor_y, beacon_x, beacon_y, pbc=False):
    man_dist_sb = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    min_x = sensor_x - man_dist_sb
    max_x = sensor_x + man_dist_sb
    min_y = sensor_y - man_dist_sb
    max_y = sensor_y + man_dist_sb

    if pbc:

        possible_border_points_to_check = []
        for i in range(man_dist_sb + 1):
            x1, x2, x3, x4 = sensor_x + man_dist_sb + 1 - i, sensor_x - man_dist_sb - 1 + i, sensor_x - i, sensor_x + i
            y1, y2, y3, y4 = sensor_y - i, sensor_y + i, sensor_y + man_dist_sb + 1 - i, sensor_y - man_dist_sb - 1 + i

            if all(i > 0 for i in [x1, x2, x3, x4, y1, y2, y3, y4]) and all(
                j < 2000000 for j in [x1, x2, x3, x4, y1, y2, y3, y4]
            ):
                possible_border_points_to_check.append((sensor_x + man_dist_sb + 1 - i, sensor_y - i))
                possible_border_points_to_check.append((sensor_x - man_dist_sb - 1 + i, sensor_y + i))
                possible_border_points_to_check.append((sensor_x - i, sensor_y + man_dist_sb + 1 - i))
                possible_border_points_to_check.append((sensor_x + i, sensor_y - man_dist_sb - 1 + i))

        # print(possible_border_points_to_check)
        return min_x, max_x, min_y, max_y, possible_border_points_to_check
    else:
        return min_x, max_x, min_y, max_y


debug = False
base_filename = "./data/input_data_12_15"
if debug:
    base_filename += "_example.csv"
else:
    base_filename += ".csv"

all_lines = []
with open(base_filename) as f:
    for line in f.read().splitlines():
        all_lines.append(line)

poly_list = []
all_pbc_list = []
first = True
for sb_pair in all_lines:
    sensor_x, sensor_y, beacon_x, beacon_y = parse_sb_pair(sb_pair)
    min_x, max_x, min_y, max_y = get_impossible_beacon_borders(sensor_x, sensor_y, beacon_x, beacon_y)
    poly_list.append(Polygon([(max_x, sensor_y), (sensor_x, max_y), (min_x, sensor_y), (sensor_x, min_y)]))

my_full_poly = unary_union(poly_list)


def extract_poly_coords(geom):
    if geom.type == "Polygon":
        exterior_coords = geom.exterior.coords[:]
        interior_coords = []
        for interior in geom.interiors:
            interior_coords += interior.coords[:]
    elif geom.type == "MultiPolygon":
        exterior_coords = []
        interior_coords = []
        for part in geom:
            epc = extract_poly_coords(part)  # Recursive call
            exterior_coords += epc["exterior_coords"]
            interior_coords += epc["interior_coords"]
    else:
        raise ValueError("Unhandled geometry type: " + repr(geom.type))
    return {"exterior_coords": exterior_coords, "interior_coords": interior_coords}


coords_dict = extract_poly_coords(my_full_poly)

pts = coords_dict["interior_coords"]

print(pts)

print(3_267_801 * 4_000_000 + 2703981.0)

print(time.time() - start)
