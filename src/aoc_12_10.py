import sys
import time

import numpy as np
import pandas as pd

# Part 1
start = time.time()
df = pd.read_csv("data/input_data_12_10.csv", header=None)

print(df.head())

clock_ctr = 1
signal = 1
total = 0


def check_signal(clock_ctr, signal, total):
    if clock_ctr == 20:
        total += signal * 20
    if clock_ctr == 60:
        total += signal * 60
    if clock_ctr == 100:
        total += signal * 100
    if clock_ctr == 140:
        total += signal * 140
    if clock_ctr == 180:
        total += signal * 180
    if clock_ctr == 220:
        total += signal * 220
    return total


for i in range(df.shape[0]):
    if df.iloc[i, 0] == "noop":
        clock_ctr += 1
        total = check_signal(clock_ctr, signal, total)
    else:
        clock_ctr += 1
        total = check_signal(clock_ctr, signal, total)
        signal += int(df.iloc[i, 0].split(" ")[-1])
        clock_ctr += 1
        total = check_signal(clock_ctr, signal, total)

print(total)
print(time.time() - start)

# Part 2
start = time.time()
df = pd.read_csv("data/input_data_12_10.csv", header=None)


def draw_crt(clock_ctr, curr_sprite_loc, crt_pixels):
    ctr_loc = clock_ctr % 40 - 1
    if abs(curr_sprite_loc - ctr_loc) <= 1:
        crt_pixels.append(1)
    else:
        crt_pixels.append(0)
    return crt_pixels


curr_sprite_loc = 1
clock_ctr = 1
crt_pixels = []

for i in range(df.shape[0]):
    if df.iloc[i, 0] == "noop":
        crt_pixels = draw_crt(clock_ctr, curr_sprite_loc, crt_pixels)
        clock_ctr += 1
    else:
        crt_pixels = draw_crt(clock_ctr, curr_sprite_loc, crt_pixels)
        clock_ctr += 1
        crt_pixels = draw_crt(clock_ctr, curr_sprite_loc, crt_pixels)
        curr_sprite_loc += int(df.iloc[i, 0].split(" ")[-1])
        clock_ctr += 1

print(crt_pixels)
a = np.array(crt_pixels).reshape(6, 40)

print(a[:, :20])
print(a[:, 20:])


print(time.time() - start)
