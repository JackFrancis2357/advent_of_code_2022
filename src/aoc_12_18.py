import itertools
import sys
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Part 1
start = time.time()
df = pd.read_csv("data/input_data_12_18.csv", header=None)
df_e = pd.read_csv("data/input_data_12_18_example.csv", header=None)

debug = True
if debug:
    curr_df = df_e
else:
    curr_df = df
curr_df.columns = ["x", "y", "z"]


def generate_faces(x, y, z):
    a = [x, y, z]
    b = [x + 1, y, z]
    c = [x, y, z + 1]
    d = [x + 1, y, z + 1]
    e = [x, y + 1, z]
    f = [x + 1, y + 1, z]
    g = [x, y + 1, z + 1]
    h = [x + 1, y + 1, z + 1]

    face_1 = [a, b, c, d]
    face_2 = [a, b, e, f]
    face_3 = [a, c, e, g]
    face_4 = [b, d, f, h]
    face_5 = [c, d, g, h]
    face_6 = [e, f, g, h]

    return face_1, face_2, face_3, face_4, face_5, face_6


faces_list = []
for i in range(curr_df.shape[0]):
    cube_x, cube_y, cube_z = curr_df.iloc[i, :]
    new_faces = generate_faces(cube_x, cube_y, cube_z)
    faces_list.append(new_faces)

full_face_list = [item for sublist in faces_list for item in sublist]
total_faces = len(full_face_list)
full_face_list.sort()
dupe_removed_faces = len(list(k for k, _ in itertools.groupby(full_face_list)))

print(total_faces - (2 * (total_faces - dupe_removed_faces)))

print(time.time() - start)

# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_18.csv", header=None)
df_e = pd.read_csv("data/input_data_12_18_example.csv", header=None)

debug = False
if debug:
    curr_df = df_e
else:
    curr_df = df
curr_df.columns = ["x", "y", "z"]

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.scatter(curr_df["x"], curr_df["y"], curr_df["z"], c="b")
plt.savefig("lava_bubble.png")

lava_cubes = []
for i in range(curr_df.shape[0]):
    lava_cubes.append((curr_df.iloc[i, 0], curr_df.iloc[i, 1], curr_df.iloc[i, 2]))

min_val, max_val = -1, 21

air_cubes = {}
for x in range(min_val, max_val):
    for y in range(min_val, max_val):
        for z in range(min_val, max_val):
            if (x, y, z) in lava_cubes:
                continue
            air_cubes[x, y, z] = False

starting_cube = (-1, -1, -1)
potential_air_cubes = [starting_cube]


def check_air_cube(cube, lava_cubes, air_cubes, potential_air_cubes, ctr):
    # Flood fill, if we come across this cube it is connected to starting cube
    if air_cubes[cube] is True:
        return potential_air_cubes, air_cubes, ctr
    air_cubes[cube] = True
    neighbors = [
        (cube[0] + 1, cube[1], cube[2]),
        (cube[0] - 1, cube[1], cube[2]),
        (cube[0], cube[1] + 1, cube[2]),
        (cube[0], cube[1] - 1, cube[2]),
        (cube[0], cube[1], cube[2] + 1),
        (cube[0], cube[1], cube[2] - 1),
    ]
    for neighbor in neighbors:
        if neighbor in lava_cubes:
            ctr += 1
        if neighbor in air_cubes.keys():
            if air_cubes[neighbor] is not True:
                potential_air_cubes.append(neighbor)
    return potential_air_cubes, air_cubes, ctr


def get_surface_area(cube_list):
    faces_list = []
    for i in cube_list:
        cube_x, cube_y, cube_z = i[:]
        new_faces = generate_faces(cube_x, cube_y, cube_z)
        faces_list.append(new_faces)

    full_face_list = [item for sublist in faces_list for item in sublist]
    total_faces = len(full_face_list)
    full_face_list.sort()
    dupe_removed_faces = len(list(k for k, _ in itertools.groupby(full_face_list)))
    return total_faces - (2 * (total_faces - dupe_removed_faces))


ctr = 0
while len(potential_air_cubes) > 0:
    curr_air_cube = potential_air_cubes[0]
    potential_air_cubes.pop(0)
    potential_air_cubes, air_cubes, ctr = check_air_cube(curr_air_cube, lava_cubes, air_cubes, potential_air_cubes, ctr)

print(ctr)
inner_cubes = []
for cube in air_cubes.keys():
    if not air_cubes[cube]:
        inner_cubes.append(cube)

print(len(inner_cubes))


print(get_surface_area(lava_cubes))
print(get_surface_area(inner_cubes))

total_surface_area = get_surface_area(lava_cubes) - get_surface_area(inner_cubes)
print(total_surface_area)

print(time.time() - start)
