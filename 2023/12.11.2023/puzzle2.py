import numpy as np
from itertools import combinations

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
lines = [list(line) for line in lines]
lines = np.array(lines)

empty_cols = np.where(np.all(lines == ".", axis=0))[0]
empty_rows = np.where(np.all(lines == ".", axis=1))[0]


def custom_manhattan(c1, c2, expansion):
    expansion1 = len(empty_rows[(empty_rows - min(c1[0],c2[0]) > 0) & (empty_rows - max(c1[0],c2[0]) < 0)])
    expansion2 = len(empty_cols[(empty_cols - min(c1[1],c2[1]) > 0) & (empty_cols - max(c1[1],c2[1]) < 0)])
    m = np.abs(c1[0]-c2[0])+(expansion-1)*(expansion1) + np.abs(c1[1]-c2[1])+(expansion-1)*(expansion2)
    return m

galaxies = np.transpose((lines=="#").nonzero()).tolist()
print(sum([custom_manhattan(c1,c2, int(1e6)) for c1, c2 in list(combinations(galaxies, 2))]))
