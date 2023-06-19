import sys

import numpy as np

b = np.load("aoc_12_17_ca.npy")
print(b.shape)

start = 200
cycle_len = 2702

print(np.all(b[start : start + cycle_len, :] == b[start + cycle_len : start + cycle_len + cycle_len, :]))
# sys.exit()
for i in range(130, b.shape[0]):
    a = b[i:, :]
    for rpt in range(2, int(np.floor(a.shape[0] / 2))):
        test = a[:rpt, :]
        val = True
        for j in range(10):
            new_val = j * rpt
            if np.array_equal(test, a[new_val : new_val + rpt, :]):
                continue
            else:
                val = False
                break
            print(j)
        if val:
            print(i, rpt, j)
            print(a.shape[0])
            print(a.shape[0] / rpt)
            print(b.shape)
        # print(rpt)
    print(i, j)
